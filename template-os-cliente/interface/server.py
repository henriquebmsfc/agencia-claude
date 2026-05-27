import json
import uuid
import asyncio
import queue
import threading
from pathlib import Path
from flask import Flask, request, Response, jsonify, send_from_directory
from claude_code_sdk import query, ClaudeCodeOptions as ClaudeAgentOptions, AssistantMessage, TextBlock, ToolUseBlock
from claude_code_sdk._errors import MessageParseError
import claude_code_sdk._internal.client as _sdk_client
import claude_code_sdk._internal.message_parser as _sdk_parser

# Patch: skip unknown message types (e.g. rate_limit_event) instead of crashing.
# parse_message is called as a global inside client.py, so patching the module attr works.
_orig_parse = _sdk_client.parse_message
def _safe_parse(data):
    try:
        return _orig_parse(data)
    except MessageParseError:
        return None
_sdk_client.parse_message = _safe_parse

# Patch process_query to filter out None results from _safe_parse
_OrigClient = _sdk_client.InternalClient
_orig_process = _OrigClient.process_query.__func__ if hasattr(_OrigClient.process_query, '__func__') else _OrigClient.process_query
async def _safe_process(self, prompt, options, transport=None):
    async for msg in _orig_process(self, prompt, options, transport):
        if msg is not None:
            yield msg
_OrigClient.process_query = _safe_process

app = Flask(__name__, static_folder='public')

INTERFACE_DIR = Path(__file__).parent          # .../interface/
WORKSPACE     = INTERFACE_DIR.parent.parent    # .../agencia-claude/
current_root  = INTERFACE_DIR.parent           # default: template-os-cliente/

# Tracks which session IDs have already been started (True = started)
chat_sessions: dict[str, bool] = {}


def root():
    return current_root


def is_client_folder(path: Path) -> bool:
    return path.is_dir() and not path.name.startswith('.') and (
        (path / '_memoria').is_dir() or (path / 'CLAUDE.md').is_file()
    )


def get_client_nome(path: Path) -> str:
    empresa = path / '_memoria' / 'empresa.md'
    if empresa.exists():
        for line in empresa.read_text(encoding='utf-8').split('\n'):
            if line.startswith('**Nome') or line.startswith('Nome:'):
                return line.split(':', 1)[-1].strip().strip('*').strip()
    return path.name


def get_responsavel_nome(path: Path) -> str:
    empresa = path / '_memoria' / 'empresa.md'
    if empresa.exists():
        text = empresa.read_text(encoding='utf-8')
        in_section = False
        for line in text.split('\n'):
            l = line.strip()
            if l.lower() == '## responsável':
                in_section = True
                continue
            if in_section:
                if l.startswith('#'):
                    break
                if l.lower().startswith('- nome:') or l.lower().startswith('nome:'):
                    val = l.split(':', 1)[-1].strip().strip('*').strip()
                    if val and not val.startswith('['):
                        return val
    return ''


def load_skill(name):
    path = root() / '.claude' / 'commands' / f'{name}.md'
    return path.read_text(encoding='utf-8') if path.exists() else None


def get_empresa_nome():
    return get_client_nome(root())


def build_skill_prompt(skill_name, user_message):
    skill_content = load_skill(skill_name)
    if not skill_content:
        return user_message
    return f"""O usuário quer executar a skill /{skill_name}.

Instruções da skill:
{skill_content}

Entrada do usuário: {user_message}

Execute a skill completa: leia os arquivos de memória necessários, siga as instruções e gere o resultado final. Se a skill gera arquivos (HTML, PDF, imagens), crie-os nos caminhos indicados."""


def run_agent_sync(prompt, options, result_queue):
    async def _run():
        try:
            async for message in query(prompt=prompt, options=options):
                result_queue.put(message)
        except Exception as e:
            result_queue.put({'__error__': str(e)})
        finally:
            result_queue.put(None)

    asyncio.run(_run())


# ── STATIC ──

@app.route('/')
def index():
    return send_from_directory('public', 'index.html')


@app.route('/outputs/conteudo/<path:filename>')
def serve_conteudo(filename):
    return send_from_directory(str(root() / 'outputs' / 'conteudo'), filename)


@app.route('/imagens/<path:filename>')
def serve_imagens(filename):
    return send_from_directory(str(root() / 'imagens'), filename)


# ── CLIENT MANAGEMENT ──

@app.route('/api/clientes')
def clientes():
    clients = []
    for path in sorted(WORKSPACE.iterdir()):
        if is_client_folder(path):
            clients.append({
                'nome': get_client_nome(path),
                'pasta': path.name,
                'path': str(path),
                'active': path == root(),
            })
    return jsonify(clients)


@app.route('/api/select-client', methods=['POST'])
def select_client():
    global current_root
    data = request.json or {}
    # Accept either an absolute path or a folder name relative to workspace
    raw = data.get('path') or data.get('pasta', '')
    target = Path(raw) if Path(raw).is_absolute() else WORKSPACE / raw
    if not target.is_dir():
        return jsonify({'error': f'Pasta não encontrada: {target}'}), 400
    current_root = target
    return jsonify({'ok': True, 'nome': get_client_nome(target), 'pasta': target.name})


# ── INFO ──

@app.route('/api/info')
def info():
    return jsonify({
        'nome': get_empresa_nome(),
        'pasta': root().name,
        'responsavel': get_responsavel_nome(root()),
    })


@app.route('/api/restart', methods=['POST'])
def restart():
    return jsonify({'ok': True})


@app.route('/api/browse-folder')
def browse_folder():
    import subprocess
    import tempfile
    import os
    script = (
        'Add-Type -AssemblyName System.Windows.Forms\n'
        '$d = New-Object System.Windows.Forms.FolderBrowserDialog\n'
        '$d.Description = "Selecionar pasta do cliente"\n'
        '$d.RootFolder = "MyComputer"\n'
        'if ($d.ShowDialog() -eq "OK") { Write-Output $d.SelectedPath }\n'
    )
    tmp = tempfile.NamedTemporaryFile(suffix='.ps1', delete=False, mode='w', encoding='utf-8')
    tmp.write(script)
    tmp.close()
    try:
        result = subprocess.run(
            ['powershell', '-NoProfile', '-ExecutionPolicy', 'Bypass', '-File', tmp.name],
            capture_output=True, text=True, timeout=120
        )
        path = result.stdout.strip()
        if not path:
            return jsonify({'cancelled': True})
        return jsonify({'path': path})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    finally:
        os.unlink(tmp.name)


# ── HOJE ──

@app.route('/api/hoje')
def hoje():
    def read(rel):
        p = root() / rel
        return p.read_text(encoding='utf-8') if p.exists() else ''

    commands_dir = root() / '.claude' / 'commands'
    skills_count = len(list(commands_dir.glob('*.md'))) if commands_dir.exists() else 0

    conteudo_dir = root() / 'outputs' / 'conteudo'
    conteudo_count = 0
    if conteudo_dir.exists():
        conteudo_count = len([
            f for f in conteudo_dir.iterdir()
            if not f.name.startswith('.') and f.name != '.gitkeep'
        ])

    return jsonify({
        'estrategia':    read('_memoria/estrategia.md'),
        'preferencias':  read('_memoria/preferencias.md'),
        'skills_count':  skills_count,
        'conteudo_count': conteudo_count,
    })


# ── PÁGINAS ──

@app.route('/api/pagina/<nome>')
def pagina(nome):
    FILE_MAP = {
        'negocio':    [('empresa', '_memoria/empresa.md'), ('estrategia', '_memoria/estrategia.md')],
        'identidade': [('design-guide', 'identidade/design-guide.md'), ('preferencias', '_memoria/preferencias.md')],
    }
    if nome not in FILE_MAP:
        return jsonify({'error': 'not found'}), 404
    result = {}
    for key, rel in FILE_MAP[nome]:
        p = root() / rel
        result[key] = p.read_text(encoding='utf-8') if p.exists() else ''
    return jsonify(result)


# ── BIBLIOTECA ──

@app.route('/api/biblioteca')
def biblioteca():
    items = []
    img_exts = {'.jpg', '.jpeg', '.png', '.webp'}
    folder_path = root() / 'outputs' / 'conteudo'
    if not folder_path.exists():
        return jsonify(items)
    for f in sorted(folder_path.iterdir(), key=lambda x: x.stat().st_mtime, reverse=True):
        if f.name.startswith('.') or f.name == '.gitkeep':
            continue
        if f.suffix.lower() != '.html':
            continue
        subfolder = folder_path / f.stem
        related = []
        if subfolder.is_dir():
            for img in sorted(subfolder.iterdir()):
                if img.suffix.lower() in img_exts:
                    related.append(f'/outputs/conteudo/{f.stem}/{img.name}')
            rel_folder = f'outputs/conteudo/{f.stem}'
        else:
            rel_folder = 'outputs/conteudo'
        items.append({
            'name':       f.stem,
            'file':       f.name,
            'path':       f'/outputs/conteudo/{f.name}',
            'folder':     rel_folder,
            'related':    related,
            'has_images': len(related) > 0,
        })
    return jsonify(items)


@app.route('/api/biblioteca/<stem>/images')
def biblioteca_images(stem):
    img_exts = {'.jpg', '.jpeg', '.png', '.webp'}
    folder = root() / 'outputs' / 'conteudo' / stem
    if not folder.is_dir():
        return jsonify([])
    images = []
    for f in sorted(folder.iterdir()):
        if f.suffix.lower() in img_exts:
            images.append(f'/outputs/conteudo/{stem}/{f.name}')
    return jsonify(images)


@app.route('/api/open-folder', methods=['POST'])
def open_folder():
    import subprocess
    data = request.json or {}
    stem = data.get('stem', '')
    # Tenta abrir a subpasta das imagens; se não existir, abre outputs/conteudo
    path = root() / 'outputs' / 'conteudo' / stem
    if not path.is_dir():
        path = root() / 'outputs' / 'conteudo'
    if path.exists():
        subprocess.Popen(['explorer', str(path)])
    return jsonify({'ok': True, 'path': str(path)})


# ── CHAT ──

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    skill = data.get('skill')
    session_id = data.get('session_id') or str(uuid.uuid4())
    cwd = str(root())

    is_new = session_id not in chat_sessions
    chat_sessions[session_id] = True

    # Only inject skill content on the first turn of a session
    if is_new and skill and skill != 'chat':
        prompt = build_skill_prompt(skill, user_message)
    else:
        prompt = user_message

    if is_new:
        options = ClaudeAgentOptions(
            cwd=cwd,
            permission_mode='bypassPermissions',
            extra_args={'session-id': session_id},
        )
    else:
        options = ClaudeAgentOptions(
            cwd=cwd,
            permission_mode='bypassPermissions',
            resume=session_id,
        )

    result_queue = queue.Queue()
    thread = threading.Thread(target=run_agent_sync, args=(prompt, options, result_queue), daemon=True)
    thread.start()

    def generate():
        yield f"data: {json.dumps({'type': 'session', 'session_id': session_id})}\n\n"
        while True:
            item = result_queue.get()
            if item is None:
                yield 'data: [DONE]\n\n'
                break
            if isinstance(item, dict) and '__error__' in item:
                yield f"data: {json.dumps({'type': 'error', 'message': item['__error__']})}\n\n"
                yield 'data: [DONE]\n\n'
                break
            if isinstance(item, AssistantMessage):
                for block in item.content:
                    if isinstance(block, TextBlock) and block.text:
                        yield f"data: {json.dumps({'type': 'text', 'text': block.text})}\n\n"
                    elif isinstance(block, ToolUseBlock):
                        tool_info = {'type': 'tool', 'name': block.name}
                        inp = getattr(block, 'input', {}) or {}
                        if 'path' in inp:
                            tool_info['path'] = str(inp['path'])
                        elif 'file_path' in inp:
                            tool_info['path'] = str(inp['file_path'])
                        elif 'command' in inp:
                            tool_info['command'] = str(inp['command'])[:80]
                        yield f"data: {json.dumps(tool_info)}\n\n"

    return Response(generate(), mimetype='text/event-stream', headers={
        'Cache-Control': 'no-cache',
        'X-Accel-Buffering': 'no',
    })


if __name__ == '__main__':
    import os
    port = int(os.environ.get('PORT', 3777))
    print(f'\n  Interface rodando em http://localhost:{port}\n')
    app.run(port=port, debug=False)

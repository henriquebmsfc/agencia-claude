import json
import asyncio
import queue
import threading
from pathlib import Path
from flask import Flask, request, Response, jsonify, send_from_directory
from claude_agent_sdk import query, ClaudeAgentOptions, AssistantMessage, TextBlock, ToolUseBlock

app = Flask(__name__, static_folder='public')

ROOT = Path(__file__).parent.parent  # template-os-cliente/


def load_skill(name):
    path = ROOT / '.claude' / 'commands' / f'{name}.md'
    return path.read_text(encoding='utf-8') if path.exists() else None


def get_empresa_nome():
    empresa = ROOT / '_memoria' / 'empresa.md'
    if not empresa.exists():
        return 'Minha Empresa'
    for line in empresa.read_text(encoding='utf-8').split('\n'):
        if line.startswith('**Nome') or line.startswith('Nome:'):
            return line.split(':', 1)[-1].strip().strip('*')
    return 'Minha Empresa'


def build_skill_prompt(skill_name, user_message):
    skill_content = load_skill(skill_name)
    if not skill_content:
        return user_message
    return f"""O usuário quer executar a skill /{skill_name}.

Instruções da skill:
{skill_content}

Entrada do usuário: {user_message}

Execute a skill completa: leia os arquivos de memória necessários, siga as instruções e gere o resultado final. Se a skill gera arquivos (HTML, PDF, imagens), crie-os nos caminhos indicados."""


def run_agent_sync(prompt, result_queue):
    """Runs the async agent in a thread and pushes events to a queue."""
    options = ClaudeAgentOptions(
        cwd=str(ROOT),
        permission_mode='acceptEdits',
    )

    async def _run():
        try:
            async for message in query(prompt=prompt, options=options):
                result_queue.put(message)
        except Exception as e:
            result_queue.put({'__error__': str(e)})
        finally:
            result_queue.put(None)  # sentinel

    asyncio.run(_run())


@app.route('/')
def index():
    return send_from_directory('public', 'index.html')


@app.route('/api/info')
def info():
    return jsonify({'nome': get_empresa_nome()})


@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')
    skill = data.get('skill')  # e.g. 'carrossel', 'legenda', None for free chat

    if skill and skill != 'chat':
        prompt = build_skill_prompt(skill, user_message)
    else:
        # Free chat: include conversation history as context
        history = data.get('history', [])
        history_text = '\n'.join(
            f"{'Usuário' if m['role'] == 'user' else 'Assistente'}: {m['content']}"
            for m in history[:-1]  # exclude current message
        )
        prompt = f"{history_text}\nUsuário: {user_message}" if history_text else user_message

    result_queue = queue.Queue()
    thread = threading.Thread(target=run_agent_sync, args=(prompt, result_queue), daemon=True)
    thread.start()

    def generate():
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
    port = int(os.environ.get('PORT', 3000))
    print(f'\n  Interface rodando em http://localhost:{port}\n')
    app.run(port=port, debug=False)

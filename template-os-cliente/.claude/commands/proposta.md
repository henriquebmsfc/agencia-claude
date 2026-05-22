# /proposta

Gere uma proposta comercial em PDF na identidade visual da empresa.

## Antes de começar

Leia `_memoria/empresa.md`, `_memoria/preferencias.md`, `_memoria/diagnostico.md` e `identidade/design-guide.md`. Se houver diagnóstico do cliente, use os gargalos identificados na seção "Entendemos que você precisa de" — proposta que espelha a dor real converte mais.

## Perguntas

1. "Para quem é a proposta? Me conta sobre o cliente — nome, negócio, o que ele precisa."
2. "Qual produto ou serviço você vai oferecer? Tem alguma condição especial (desconto, prazo diferente)?"

## Gerar o HTML

Criar o arquivo `outputs/propostas/proposta-[cliente]-[data].html` com a proposta formatada na identidade visual do `design-guide.md`.

Estrutura do HTML:

```
Cabeçalho: logo (se existir em identidade/logo.png) + nome da empresa + "Proposta Comercial"
Destinatário: Para [Nome], data
Seções: Entendemos que você precisa de / Nossa solução / O que está incluso / Investimento / Prazo / Próximo passo
Rodapé: Nome da empresa, WhatsApp, Instagram
```

Requisitos visuais:
- Fonte do `design-guide.md`, importada do Google Fonts
- Cores do `design-guide.md` via variáveis CSS (`--cor-primaria`, `--cor-fundo`, `--cor-texto`)
- Layout A4 (210mm × 297mm), margens generosas (40px lateral)
- Hierarquia tipográfica clara: título da seção em destaque, conteúdo em corpo de texto
- Tom do `preferencias.md` — sem linguagem genérica, sem adjetivos vazios

## Converter para PDF via Playwright

Após gerar o HTML, executar:

```python
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

INPUT_HTML = Path("outputs/propostas/proposta-[cliente]-[data].html")
OUTPUT_PDF = INPUT_HTML.with_suffix(".pdf")

async def export_pdf():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page()
        await page.goto(f"file://{INPUT_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        await page.pdf(
            path=str(OUTPUT_PDF),
            format="A4",
            margin={"top": "20mm", "bottom": "20mm", "left": "15mm", "right": "15mm"},
            print_background=True,
        )
        await browser.close()

asyncio.run(export_pdf())
```

Se Playwright não estiver instalado:
```bash
pip install playwright && python -m playwright install chromium
```

## Ao finalizar

Mostrar ao dono: "Proposta gerada em `outputs/propostas/proposta-[cliente]-[data].pdf`. Quer ajustar alguma seção antes de enviar?"

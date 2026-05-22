# /carrossel

Gere um carrossel para Instagram — roteiro, HTML estilizado e exportação em JPG.

## Antes de começar

Se o plugin `frontend-design` estiver disponível, use a skill `frontend-design:frontend-design` para orientar as decisões de design antes de gerar o HTML.

Leia `_memoria/empresa.md`, `_memoria/preferencias.md` e `identidade/design-guide.md`.

Verifique se há imagens relevantes em `imagens/` — priorizá-las nos slides se o tema permitir.

## Perguntas

Faça uma pergunta por vez:

1. "Qual é o tema ou assunto do carrossel? Pode ser um produto, uma dica, uma objeção de cliente, um bastidor — o que você quer falar?"
2. "Qual é o objetivo? (marcar alguém, gerar mensagem no WhatsApp, informar, mostrar resultado)"

## Fase 1 — Roteiro

Gere o roteiro antes de qualquer HTML. Formato:

---
**Slide 1 — Capa (gancho)**
Headline: [máximo 8 palavras — use uma das estruturas abaixo]
Subheadline: [complemento opcional]

**Slide 2**
Título: [tópico]
Texto: [2-3 linhas no máximo]

...(até 7 slides de conteúdo)

**Slide final**
CTA: [chamada para ação clara]
---

**Estruturas de gancho para a capa:**
- Promessa direta: "Como [resultado] sem [objeção]"
- Curiosidade: "O que ninguém te conta sobre [assunto]"
- Dor: "[Problema que o cliente sente]? Tem solução."
- Número: "[X] erros que [perfil] comete em [contexto]"
- Contra-intuitivo: "Para de [coisa óbvia]. Faz isso."

Após o roteiro, perguntar: **"Roteiro ok? Posso gerar o visual?"**

## Fase 2 — HTML

Apenas após aprovação do roteiro, gerar o arquivo `outputs/conteudo/carrossel-[tema]-[data].html`.

**Dimensões:** cada slide 1350×1080px (proporção 5:4 — formato paisagem padrão de carrossel).

**Requisitos visuais:**
- Cores e tipografia do `design-guide.md` via variáveis CSS
- Fonte do Google Fonts — escolher fonte com personalidade, não Inter/Roboto
- Alternância de fundo claro/escuro entre slides para ritmo visual
- Hierarquia clara: título grande, texto menor, CTA em destaque
- **Não enumerar slides** no layout ("Slide 1", "Slide 2" etc. não aparecem no visual)
- Barra de progresso sutil no rodapé de cada slide
- Cada slide é um `<div class="slide">` com dimensões fixas — o HTML mostra todos empilhados verticalmente para revisão

**Imagens:**
- Prioridade 1: imagens da pasta `imagens/` se relevantes para o tema
- Prioridade 2: Unsplash via URL (`https://images.unsplash.com/photo-[ID]?w=1350&q=80`)
- Nunca usar placeholder de cor sólida como fundo principal

Após gerar o HTML, perguntar: **"Visual aprovado? Exporto os slides em JPG?"**

## Fase 3 — Exportar em JPG

Apenas após aprovação do HTML, executar via Playwright:

```python
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

INPUT_HTML = Path("outputs/conteudo/carrossel-[tema]-[data].html")
OUTPUT_DIR = INPUT_HTML.parent / f"carrossel-[tema]-[data]"
OUTPUT_DIR.mkdir(exist_ok=True)

SLIDE_W, SLIDE_H = 1350, 1080

async def export_slides():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": SLIDE_W + 40, "height": SLIDE_H + 200})
        await page.goto(f"file://{INPUT_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(2000)

        slides = await page.query_selector_all(".slide")
        for i, slide in enumerate(slides):
            await slide.scroll_into_view_if_needed()
            await page.wait_for_timeout(200)
            await slide.screenshot(
                path=str(OUTPUT_DIR / f"slide_{i+1:02d}.jpg"),
                type="jpeg",
                quality=92,
            )
        await browser.close()

asyncio.run(export_slides())
```

Se Playwright não estiver instalado:
```bash
pip install playwright && python -m playwright install chromium
```

## Ao finalizar

"Carrossel exportado em `outputs/conteudo/carrossel-[tema]-[data]/`. [N] slides prontos para subir no Instagram. Quer ajustar algum?"

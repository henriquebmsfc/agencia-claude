# /story

Gere um story para Instagram — roteiro, HTML estilizado e exportação em JPG.

## Antes de começar

Se o plugin `frontend-design` estiver disponível, use a skill `frontend-design:frontend-design` para orientar as decisões de design antes de gerar o HTML.

Leia `_memoria/empresa.md`, `_memoria/preferencias.md` e `identidade/design-guide.md`.

## Perguntas

1. "Vai ser story único ou sequência? Se sequência, quantos stories?"
2. "Qual é o objetivo? (gerar DM, mostrar produto, engajar com enquete, anunciar algo, contar bastidor)"

## Fase 1 — Roteiro

### Story único
---
**Story**
Texto: [máximo 3 linhas — deve ser lido em 2 segundos]
Elemento interativo: [enquete sim/não / caixa de perguntas / reação com emoji / contagem / nenhum]
CTA: [ex: "Responde aqui" / "Link na bio" / "Manda DM" / nenhum]
---

### Sequência de stories
---
**Story 1 — Gancho**
Texto: [pergunta ou afirmação que para o polegar — máximo 2 linhas]
Elemento: [enquete ou reação para prender atenção]

**Story 2 a N — [tópico]**
Texto: [um ponto por story, máximo 3 linhas]
Elemento: [opcional]

**Último story — CTA**
Texto: [chamada para ação clara]
Elemento: [caixa de perguntas / link / enquete de confirmação]
---

Após o roteiro, perguntar: **"Roteiro ok? Posso gerar o visual?"**

## Fase 2 — HTML

Apenas após aprovação, gerar `outputs/conteudo/story-[tema]-[data].html`.

**Dimensões:** cada story 1080×1920px (proporção 9:16 — vertical full-screen).

**Requisitos visuais:**
- Cores e tipografia do `design-guide.md` via variáveis CSS
- Fonte do Google Fonts com personalidade (não Inter/Roboto)
- Texto centralizado com grande área de respiro — stories têm texto escasso, visual forte
- Para sequências: cada story é um `<div class="story">` — o HTML mostra todos empilhados verticalmente para revisão
- Fundo: gradiente da identidade visual, imagem de `imagens/` com overlay, ou cor sólida com textura — nunca fundo branco sem elemento visual

Após gerar o HTML, perguntar: **"Visual aprovado? Exporto em JPG?"**

## Fase 3 — Exportar em JPG

```python
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

INPUT_HTML = Path("outputs/conteudo/story-[tema]-[data].html")
OUTPUT_DIR = INPUT_HTML.parent / f"story-[tema]-[data]"
OUTPUT_DIR.mkdir(exist_ok=True)

async def export_stories():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1920})
        await page.goto(f"file://{INPUT_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(2000)

        stories = await page.query_selector_all(".story")
        if stories:
            for i, story in enumerate(stories):
                box = await story.bounding_box()
                await page.screenshot(
                    path=str(OUTPUT_DIR / f"story_{i+1:02d}.jpg"),
                    clip={"x": box["x"], "y": box["y"], "width": 1080, "height": 1920},
                    type="jpeg", quality=92,
                )
        else:
            await page.screenshot(
                path=str(OUTPUT_DIR / "story_01.jpg"),
                clip={"x": 0, "y": 0, "width": 1080, "height": 1920},
                type="jpeg", quality=92,
            )
        await browser.close()

asyncio.run(export_stories())
```

## Ao finalizar

"Story exportado em `outputs/conteudo/story-[tema]-[data]/`. Pronto para publicar. Quer ajustar algo?"

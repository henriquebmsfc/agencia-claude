# /post

Gere um post único para Instagram — roteiro, HTML estilizado e exportação em JPG.

## Antes de começar

Se o plugin `frontend-design` estiver disponível, use a skill `frontend-design:frontend-design` para orientar as decisões de design antes de gerar o HTML.

Leia `_memoria/empresa.md`, `_memoria/preferencias.md` e `identidade/design-guide.md`.

Verifique se há imagens relevantes em `imagens/` para usar como fundo ou elemento visual.

## Perguntas

1. "O que vai estar na imagem? (foto de produto, resultado de cliente, bastidor, gráfico com dica, promoção)"
2. "Qual ação você quer que a pessoa tome? (salvar, comentar, mandar mensagem, comprar)"

## Fase 1 — Roteiro

---
**Texto visual** — o que vai escrito na imagem:
- Linha 1 — gancho (máximo 6 palavras, para o polegar)
- Linha 2 — desenvolvimento ou dado concreto
- Linha 3 — destaque ou CTA visual (opcional)

**Legenda:**
[primeira linha é o gancho — o que aparece antes do "ver mais"]
.
.
[desenvolvimento — 3 a 6 linhas]
.
.
[CTA claro e direto]
.
.
[hashtags — máximo 8, de nicho]
---

Após o roteiro, perguntar: **"Roteiro ok? Posso gerar o visual?"**

## Fase 2 — HTML

Apenas após aprovação, gerar `outputs/conteudo/post-[tema]-[data].html`.

**Dimensões:** 1080×1080px (quadrado padrão do Instagram).

**Requisitos visuais:**
- Cores e tipografia do `design-guide.md` via variáveis CSS
- Fonte do Google Fonts com personalidade (não Inter/Roboto)
- Hierarquia tipográfica clara: linha 1 em destaque, linha 2 menor, linha 3 como CTA
- Fundo: usar imagem de `imagens/` se disponível, ou Unsplash (`https://images.unsplash.com/photo-[ID]?w=1080&q=80`), com overlay semitransparente para legibilidade
- Layout centrado, texto com boa área de respiro nas margens

Após gerar o HTML, perguntar: **"Visual aprovado? Exporto em JPG?"**

## Fase 3 — Exportar em JPG

```python
import asyncio
from pathlib import Path
from playwright.async_api import async_playwright

INPUT_HTML = Path("outputs/conteudo/post-[tema]-[data].html")
OUTPUT_JPG = INPUT_HTML.with_suffix(".jpg")

async def export_post():
    async with async_playwright() as p:
        browser = await p.chromium.launch()
        page = await browser.new_page(viewport={"width": 1080, "height": 1080})
        await page.goto(f"file://{INPUT_HTML.resolve()}", wait_until="networkidle")
        await page.wait_for_timeout(2000)
        post = await page.query_selector(".post")
        if post:
            await post.screenshot(path=str(OUTPUT_JPG), type="jpeg", quality=92)
        else:
            await page.screenshot(path=str(OUTPUT_JPG), type="jpeg", quality=92,
                                  clip={"x": 0, "y": 0, "width": 1080, "height": 1080})
        await browser.close()

asyncio.run(export_post())
```

## Ao finalizar

"Post gerado em `outputs/conteudo/post-[tema]-[data].jpg`. Pronto para publicar. Quer ajustar algo?"

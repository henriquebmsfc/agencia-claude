# /gerar-site

Crie ou atualize o arquivo `site/index.html` com um site de conversão para o negócio.

## Antes de começar

Leia os arquivos `_memoria/empresa.md`, `_memoria/preferencias.md` e `identidade/design-guide.md` antes de começar. Verifique também se há imagens em `imagens/` — se existirem, priorizá-las no layout ao invés de placeholders.

## Estrutura do site

O site deve ter as seguintes seções na ordem:

1. **Hero** — Headline clara do que o negócio faz + subheadline com o benefício principal + botão CTA para WhatsApp
2. **O que fazemos** — 3 a 4 cards com os principais serviços/produtos (nome, descrição curta, preço se aplicável)
3. **Por que nos escolher** — 3 diferenciais com ícone e texto curto
4. **Depoimentos** — 2 a 3 depoimentos de clientes (placeholder se ainda não tiver)
5. **CTA final** — Chamada para ação + botão WhatsApp
6. **Rodapé** — Nome da empresa, Instagram, WhatsApp

## Requisitos técnicos

- HTML com `<style>` no `<head>` — sem dependências externas, funciona offline
- Mobile-first — layout responsivo com `max-width: 680px` centrado
- Importar fonte do Google Fonts no `<head>` (escolher conforme design-guide ou usar Inter como padrão)
- Usar variáveis CSS (`--cor-primaria`, `--cor-fundo`, `--cor-texto`) definidas no `:root`
- Botão WhatsApp abre `https://wa.me/[número]?text=Olá, vim pelo site` com ícone SVG do WhatsApp
- Cores e fontes do `identidade/design-guide.md`
- Tom dos textos igual ao `_memoria/preferencias.md` — não usar linguagem genérica de agência
- Produtos e preços reais do `_memoria/empresa.md` — nenhum placeholder de conteúdo
- Visual limpo e profissional: espaçamento generoso, hierarquia tipográfica clara, sem poluição visual

## Ao finalizar

Mostre ao dono: "Site gerado em `site/index.html`. Para visualizar, abra o arquivo no navegador. Quer que eu ajuste alguma seção?"

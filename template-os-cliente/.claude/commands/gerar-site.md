# /gerar-site

Crie ou atualize o arquivo `site/index.html` com um site de conversão para o negócio.

## Antes de começar

Leia os arquivos `_memoria/empresa.md` e `identidade/design-guide.md` antes de começar.

## Estrutura do site

O site deve ter as seguintes seções na ordem:

1. **Hero** — Headline clara do que o negócio faz + subheadline com o benefício principal + botão CTA para WhatsApp
2. **O que fazemos** — 3 a 4 cards com os principais serviços/produtos (nome, descrição curta, preço se aplicável)
3. **Por que nos escolher** — 3 diferenciais com ícone e texto curto
4. **Depoimentos** — 2 a 3 depoimentos de clientes (placeholder se ainda não tiver)
5. **CTA final** — Chamada para ação + botão WhatsApp
6. **Rodapé** — Nome da empresa, Instagram, WhatsApp

## Requisitos técnicos

- HTML e CSS inline ou em `<style>` — sem dependências externas, funciona offline
- Mobile-first — layout responsivo simples
- Botão WhatsApp abre `https://wa.me/[número]` com mensagem pré-preenchida
- Cores e fontes do `identidade/design-guide.md`
- Tom dos textos igual ao `_memoria/preferencias.md`
- Produtos e preços reais do `_memoria/empresa.md`

## Ao finalizar

Mostre ao dono: "Site gerado em `site/index.html`. Para visualizar, abra o arquivo no navegador. Quer que eu ajuste alguma seção?"

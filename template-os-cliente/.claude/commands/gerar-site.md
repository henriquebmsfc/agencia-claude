# /gerar-site

Crie ou atualize o arquivo `site/index.html` com um site de conversão para o negócio.

## Antes de começar

Se o plugin `frontend-design` estiver disponível, use a skill `frontend-design:frontend-design` para orientar as decisões de design antes de gerar o HTML.

Leia os arquivos `_memoria/empresa.md`, `_memoria/preferencias.md` e `identidade/design-guide.md` antes de começar. Verifique também se há imagens em `imagens/` — se existirem, priorizá-las no layout ao invés de placeholders.

**Padrão de qualidade visual:** escolha uma direção estética clara e execute com precisão. Use tipografia com caráter (evite Inter/Roboto genéricos), espaçamento generoso, hierarquia visual bem definida, e micro-detalhes que elevam a percepção de qualidade. O resultado deve parecer desenhado por um designer — não gerado por IA.

## Estrutura do site

O site deve ter as seguintes seções na ordem:

1. **Hero** — Headline clara do que o negócio faz + subheadline com o benefício principal + botão CTA para WhatsApp
2. **O que fazemos** — 3 a 4 cards com os principais serviços/produtos (nome, descrição curta, preço se aplicável)
3. **Por que nos escolher** — 3 diferenciais com ícone e texto curto
4. **Depoimentos** — 2 a 3 depoimentos de clientes (placeholder se ainda não tiver)
5. **CTA final** — Chamada para ação + botão WhatsApp
6. **Rodapé** — Nome da empresa, Instagram, WhatsApp

## Imagens

**Prioridade 1:** imagens da pasta `imagens/` — se existirem, usá-las como `src` relativo (`../imagens/foto.jpg`).

**Prioridade 2:** imagens do Unsplash via URL direta (gratuito, sem cadastro):
- Formato: `https://images.unsplash.com/photo-[ID]?w=800&q=80&auto=format&fit=crop`
- Buscar a URL correta para o segmento do negócio (ex: clínica, academia, restaurante, moda)
- Usar imagens reais e contextuais — nunca `via.placeholder.com` ou fundo colorido como substituto

**Nunca usar:** placeholders genéricos de cor sólida no lugar de imagens em seções onde uma foto faria diferença.

## Requisitos técnicos

- HTML com `<style>` no `<head>` — sem dependências externas além de Google Fonts
- Mobile-first — layout responsivo com `max-width: 680px` centrado
- Importar fonte do Google Fonts no `<head>` (escolher conforme design-guide — evitar Inter/Roboto genéricos)
- Usar variáveis CSS (`--cor-primaria`, `--cor-fundo`, `--cor-texto`) definidas no `:root`
- Botão WhatsApp abre `https://wa.me/[número]?text=Olá, vim pelo site` com ícone SVG do WhatsApp
- Cores e fontes do `identidade/design-guide.md`
- Tom dos textos igual ao `_memoria/preferencias.md` — não usar linguagem genérica de agência
- Produtos e preços reais do `_memoria/empresa.md` — nenhum placeholder de conteúdo
- Visual limpo e profissional: espaçamento generoso, hierarquia tipográfica clara, sem poluição visual

## Ao finalizar

Mostre ao dono: "Site gerado em `site/index.html`. Para visualizar, abra o arquivo no navegador. Quer que eu ajuste alguma seção?"

# /gerar-link-page

Crie ou atualize o arquivo `link-page/index.html` com uma link page para a bio do Instagram.

## Antes de começar

Leia os arquivos `_memoria/empresa.md`, `_memoria/preferencias.md` e `identidade/design-guide.md` antes de começar.

## Estrutura da link page

- Foto/logo da empresa no topo
- Nome da empresa
- Frase curta de posicionamento (1 linha)
- Lista de links clicáveis:
  - WhatsApp (com mensagem pré-preenchida)
  - Instagram
  - Site (se existir)
  - Links dos principais produtos/serviços (um por produto se fizer sentido)
- Rodapé discreto com nome da empresa

## Requisitos técnicos

- HTML com `<style>` no `<head>` — sem dependências externas além do Google Fonts
- Importar fonte do Google Fonts no `<head>` (conforme design-guide ou usar Inter como padrão)
- Usar variáveis CSS (`--cor-primaria`, `--cor-fundo`, `--cor-texto`) definidas no `:root`
- Design vertical centralizado, otimizado para mobile (`max-width: 480px`)
- Cores e tipografia do `identidade/design-guide.md`
- Cada botão com cor e estilo consistentes com a identidade

## Ao finalizar

Mostre ao dono: "Link page gerada em `link-page/index.html`. Para usar, hospede o arquivo (GitHub Pages, por exemplo) e coloque o link na bio do Instagram. Quer ajustar algum link ou texto?"

# OS do Negócio — [NOME DA EMPRESA]

Sistema operacional do negócio construído no Claude Code. Contém toda a inteligência do negócio — produtos, tom de voz, estratégia — e skills prontas para criar conteúdo, propostas, respostas e mais.

## Primeiro acesso

1. Abra esta pasta no Claude Code
2. Digite `/instalar` e responda as perguntas
3. Pronto — o sistema está configurado com o seu negócio

## Uso diário

- Inicie cada sessão com `/abrir`
- Salve suas alterações com `/salvar`
- Veja todas as skills disponíveis no `CLAUDE.md`

## Skills disponíveis

| Skill | O que faz |
|---|---|
| `/instalar` | Configura o sistema pela primeira vez |
| `/abrir` | Inicia a sessão com resumo do contexto |
| `/salvar` | Salva e versiona no GitHub |
| `/atualizar` | Atualiza memória quando o negócio muda |
| `/diagnostico` | Mapeia gargalos e oportunidades |
| `/gerar-site` | Cria ou atualiza o site |
| `/gerar-link-page` | Cria ou atualiza a link page do Instagram |
| `/carrossel` | Gera roteiro de carrossel |
| `/post` | Gera texto visual + legenda para post único |
| `/story` | Gera roteiro de story único ou sequência |
| `/legenda` | Gera legenda para qualquer post |
| `/pauta-conteudo` | Gera pauta mensal de conteúdo |
| `/proposta` | Gera proposta comercial |
| `/resposta-cliente` | Gera resposta para mensagem de cliente |
| `/mapear-rotinas` | Identifica tarefas repetitivas e sugere novas skills |

## Arquivos de memória

Os arquivos em `_memoria/` são o cérebro do sistema. Toda skill lê esses arquivos antes de trabalhar.

- `empresa.md` — o que o negócio faz
- `preferencias.md` — como se comunicar
- `estrategia.md` — foco atual
- `diagnostico.md` — gargalos mapeados

Para atualizar, use `/atualizar` ou edite diretamente e depois use `/salvar`.

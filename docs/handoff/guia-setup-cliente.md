# Guia de Uso — OS do Negócio

Esse guia é o seu ponto de partida toda vez que for usar o sistema. Guarde aqui.

---

## O que foi instalado no seu computador

**Claude Code** — o programa onde você digita os comandos.
**Seu OS do Negócio** — a pasta do seu negócio com toda a inteligência configurada.

Para usar, é só abrir o Claude Code na pasta certa e digitar o comando que precisar.

---

## Como abrir o sistema

1. Abra o **Claude Code** no seu computador
2. Abra a pasta **[nome do negócio]** (a gente já salvou no lugar certo)
3. Digite `/abrir` e aperte Enter

Vai aparecer um resumo do seu negócio, o foco atual e a meta do mês. A partir daí é só pedir o que precisar.

---

## O que você pode fazer

### Conteúdo para Instagram

| Comando | O que faz |
|---|---|
| `/carrossel` | Gera o roteiro de um carrossel |
| `/post` | Gera o texto da imagem + legenda para post único |
| `/story` | Gera roteiro de story único ou sequência |
| `/legenda` | Gera só a legenda para qualquer post |
| `/pauta-conteudo` | Monta a pauta de conteúdo do mês |

### Vendas e atendimento

| Comando | O que faz |
|---|---|
| `/proposta` | Gera uma proposta comercial para um cliente |
| `/resposta-cliente` | Gera resposta para mensagem de WhatsApp |

### Site e bio do Instagram

| Comando | O que faz |
|---|---|
| `/gerar-site` | Atualiza o seu site com as informações do negócio |
| `/gerar-link-page` | Atualiza a link page da bio do Instagram |

### Manutenção

| Comando | O que faz |
|---|---|
| `/atualizar` | Atualiza as informações quando o negócio muda |
| `/diagnostico` | Faz um raio-x dos gargalos do negócio |
| `/salvar` | Salva tudo no GitHub (backup automático) |

---

## Quando o negócio mudar

Novo produto, preço novo, mudança de foco — qualquer coisa que mudou, rode `/atualizar`. O sistema vai perguntar o que mudou e atualizar os arquivos automaticamente.

Depois rode `/salvar` para o backup ficar atualizado.

---

## Como atualizar o site

Se você adicionou um produto novo ou mudou preço, atualize a memória primeiro:
1. `/atualizar` — informe o que mudou
2. `/gerar-site` — o site é gerado com os dados novos
3. Substitua o arquivo `site/index.html` no servidor onde está hospedado

---

## Como atualizar a link page (bio do Instagram)

Mesmo processo:
1. `/atualizar` — se algo mudou (novo link, produto novo)
2. `/gerar-link-page` — a link page é gerada com os dados atuais
3. Substitua o arquivo `link-page/index.html` onde está hospedado

---

## Dúvidas ou precisando de ajuda

Entre em contato: **[WhatsApp do consultor]**

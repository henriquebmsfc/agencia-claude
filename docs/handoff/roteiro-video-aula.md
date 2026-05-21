# Roteiro — Vídeo Aula OS do Negócio

Duração: 12–15 minutos  
Formato: gravação de tela + narração  
Ferramenta: qualquer gravador de tela (Loom, OBS, Quicktime)

Grave uma vez. Reutilize para todos os clientes — o conteúdo é genérico.

---

## Antes de gravar

- Abrir o Claude Code com uma pasta de exemplo já configurada (use o ambiente de teste)
- Ter os arquivos de memória preenchidos com dados fictícios realistas
- Deixar o terminal limpo, sem mensagens anteriores
- Fonte grande o suficiente para aparecer bem no vídeo

---

## Bloco 1 — Introdução (1 min)

**O que falar:**

> "Esse vídeo é o seu guia de uso do OS do Negócio. Aqui você vai aprender como abrir o sistema, o que cada comando faz e como usar no dia a dia. Não precisa saber nada de tecnologia — é mais simples do que parece."

> "O sistema já está todo configurado com as informações do seu negócio. Você só precisa saber como abrir e o que digitar."

---

## Bloco 2 — Abrindo o sistema (1 min)

**Mostrar na tela:** Claude Code sendo aberto, pasta do negócio aberta.

**O que falar:**

> "Para usar o sistema, você abre o Claude Code — o ícone fica aqui no seu computador — e abre a pasta do seu negócio. A gente já deixou tudo no lugar certo."

> "Depois de abrir, você digita `/abrir` e aperta Enter. Sempre que iniciar uma sessão, comece por aqui."

**Mostrar:** digitar `/abrir`, aguardar a resposta aparecer.

> "Olha — ele mostra o foco do momento, a meta do mês, o gargalo principal e o tom de voz. Tudo o que a gente configurou. A partir daqui você pode pedir qualquer coisa."

---

## Bloco 3 — A memória do sistema (2 min)

**Mostrar na tela:** Abrir a pasta `_memoria/` e os 4 arquivos.

**O que falar:**

> "Dentro da pasta do seu negócio existe uma pasta chamada `_memoria`. É aqui que fica toda a inteligência do sistema."

> "Tem quatro arquivos:
> - `empresa.md` — o que o seu negócio faz, produtos, preços, cliente ideal
> - `preferencias.md` — como você escreve, o tom de voz, o que nunca usar
> - `estrategia.md` — foco atual, meta do mês, canal de aquisição
> - `diagnostico.md` — gargalos mapeados e oportunidades"

> "Toda skill lê esses arquivos antes de gerar qualquer coisa. É por isso que o conteúdo sai com a voz do seu negócio, não genérico."

---

## Bloco 4 — Conteúdo para Instagram (4 min)

### Carrossel

**Mostrar:** digitar `/carrossel`.

> "Para criar um carrossel, você digita `/carrossel`. O sistema vai fazer duas perguntas: qual é o tema e qual é o objetivo."

**Mostrar:** responder as perguntas, aguardar o roteiro.

> "Olha o resultado — capa com gancho, slides de conteúdo, CTA no final. Já no tom do seu negócio, com os seus produtos. É só pegar esse roteiro e montar no Canva."

---

### Post único

**Mostrar:** digitar `/post`.

> "Para post único — aquelas imagens com texto em cima — você usa `/post`. Ele gera o que vai escrito na imagem e a legenda completa para o Instagram."

---

### Story

**Mostrar:** digitar `/story`.

> "Para stories, use `/story`. Você escolhe se quer story único ou sequência. Ele já sugere o elemento interativo — enquete, caixa de pergunta — e o CTA."

---

### Legenda avulsa

**Mostrar:** digitar `/legenda`.

> "Se você já tem a imagem e só precisa da legenda, usa `/legenda`. Ele gera duas versões — uma curta e uma longa — e você escolhe qual usar."

---

### Pauta do mês

**Mostrar:** digitar `/pauta-conteudo`.

> "Para planejar o mês inteiro de uma vez, use `/pauta-conteudo`. Você informa quantos posts por semana e se tem alguma data importante. Ele monta a pauta equilibrando educação, prova social, bastidor e oferta."

---

## Bloco 5 — Vendas e atendimento (2 min)

### Resposta de cliente

**Mostrar:** digitar `/resposta-cliente`, colar uma mensagem fictícia.

> "Recebeu uma mensagem de WhatsApp e não sabe como responder? Cola no `/resposta-cliente`. Ele pergunta o contexto — se é lead novo, cliente, reclamação — e gera duas versões de resposta. Uma curta e uma mais elaborada."

---

### Proposta comercial

**Mostrar:** digitar `/proposta`.

> "Para gerar uma proposta, use `/proposta`. Você informa quem é o cliente e o que vai oferecer. O sistema pega as informações do produto e monta uma proposta formatada, pronta para enviar."

---

## Bloco 6 — Atualizando o site e a link page (2 min)

**O que falar:**

> "O sistema também gera e atualiza seu site e sua link page da bio do Instagram automaticamente."

### Site

**Mostrar:** digitar `/gerar-site`.

> "Quando quiser atualizar o site — adicionou produto novo, mudou preço, quer uma versão nova — você digita `/gerar-site`. Ele lê os dados do seu negócio e gera o arquivo HTML completo."

> "O arquivo fica em `site/index.html`. É só fazer upload para onde o site está hospedado."

---

### Link page (bio do Instagram)

**Mostrar:** digitar `/gerar-link-page`.

> "Para a link page da bio — aquela página com todos os seus links — use `/gerar-link-page`. Mesmo processo: ele gera o arquivo em `link-page/index.html` e você faz o upload."

> "Se você ainda não hospedou, o consultor pode te ajudar com isso."

---

## Bloco 7 — Mantendo o sistema atualizado (1 min)

**Mostrar:** digitar `/atualizar`.

> "O negócio muda — preço novo, produto novo, foco diferente. Para manter o sistema atualizado, use `/atualizar`. Ele pergunta o que mudou e atualiza os arquivos de memória."

> "Depois de atualizar, rode `/gerar-site` e `/gerar-link-page` se quiser refletir as mudanças no site e na bio também."

---

**Mostrar:** digitar `/salvar`.

> "E para salvar tudo no backup, use `/salvar`. Ele commita as alterações no GitHub — você nunca perde nada."

---

## Bloco 8 — Encerramento (30 seg)

> "É isso. O sistema já conhece o seu negócio — você só precisa digitar o comando e responder as perguntas. Tem dúvida ou precisando de ajuda, entra em contato."

---

## Checklist antes de publicar

- [ ] Todos os blocos gravados
- [ ] Nenhuma informação pessoal/real de cliente aparece na tela
- [ ] Fonte legível em todo o vídeo
- [ ] Áudio sem ruído de fundo
- [ ] Subir para YouTube (não listado) ou Loom e incluir o link no guia do cliente

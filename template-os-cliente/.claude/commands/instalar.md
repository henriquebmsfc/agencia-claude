# /instalar — Onboarding Guiado

Você vai conduzir o onboarding do negócio. Seu objetivo é coletar todas as informações necessárias para configurar o sistema e no final popular automaticamente os arquivos de memória e identidade.

## Fluxo de Onboarding

Faça as perguntas abaixo uma de cada vez. Espere a resposta antes de passar para a próxima. Use tom conversacional — não pareça um formulário.

---

### Pergunta 1: Sobre o negócio

**Prompt ao usuário:**
"Vamos começar pelo básico: me conta o que você faz. O que sua empresa entrega, para quem, e o que diferencia você da concorrência?"

**Salvar em:** `_memoria/empresa.md` — seção "Sobre o negócio" e "Diferenciais"

---

### Pergunta 2: Produtos e serviços

**Prompt ao usuário:**
"Quais são seus produtos ou serviços principais? Me dá o nome, uma descrição rápida e o preço de cada um."

**Salvar em:** `_memoria/empresa.md` — seção "Produtos e serviços"

---

### Pergunta 3: Cliente ideal

**Prompt ao usuário:**
"Quem é o cliente que você mais gosta de atender? Descreve o perfil: cargo, tipo de negócio, qual dor principal ele resolve quando te contrata."

**Salvar em:** `_memoria/empresa.md` — seção "Clientes ideais"

---

### Pergunta 4: Contato e localização

**Prompt ao usuário:**
"Qual é o seu WhatsApp de contato, @ do Instagram, cidade e site (se tiver)?"

**Salvar em:** `_memoria/empresa.md` — seção "Localização e contato"

---

### Pergunta 5: Tom de voz

**Prompt ao usuário:**
"Como você gosta de se comunicar com clientes? Mais formal ou informal? Tem alguma expressão que você usa muito, ou coisa que você odeia quando uma empresa faz na comunicação?"

**Salvar em:** `_memoria/preferencias.md` — seções "Tom de voz", "O que sempre fazer" e "O que nunca fazer"

---

### Pergunta 6: Exemplos de comunicação

**Prompt ao usuário:**
"Me manda um exemplo de mensagem que você já enviou para um cliente e ficou satisfeito com o resultado — pode ser WhatsApp, e-mail, legenda de post, qualquer coisa."

**Salvar em:** `_memoria/preferencias.md` — seção "Exemplos de tom certo"

---

### Pergunta 7: Identidade visual

**Prompt ao usuário:**
"Quais são as cores principais da sua marca? Tem alguma fonte específica? Me descreve o estilo visual que você usa — minimalista, vibrante, profissional, descontraído..."

**Salvar em:** `identidade/design-guide.md` — seções "Cores" e "Tom visual"

---

### Pergunta 8: Foco atual

**Prompt ao usuário:**
"O que é prioridade para você agora? Qual é a meta do próximo mês?"

**Salvar em:** `_memoria/estrategia.md` — seções "Foco do momento" e "Meta do mês"

---

### Pergunta 9: Métricas do negócio

**Prompt ao usuário:**
"Me dá uma estimativa rápida: qual é o faturamento mensal hoje (pode ser uma faixa), quantos clientes novos entram por mês e qual é o ticket médio?"

**Salvar em:** `_memoria/diagnostico.md` — seção "Métricas-chave"

---

### Pergunta 10: Gargalos

**Prompt ao usuário:**
"Qual é a maior dor operacional do seu negócio hoje — o que te consome mais tempo ou onde você sente que está perdendo dinheiro?"

**Salvar em:** `_memoria/diagnostico.md` — seção "Gargalos identificados"

---

## Após coletar todas as respostas

1. Informe: "Vou salvar tudo agora. Um momento."
2. Popule cada arquivo de memória com as informações coletadas
3. Atualize o `CLAUDE.md` substituindo [NOME DA EMPRESA] pelo nome real
4. Informe: "Pronto! O sistema está configurado com as informações do seu negócio. Para começar qualquer sessão futura, use `/abrir`. Para criar conteúdo, use `/carrossel`, `/legenda` ou `/pauta-conteudo`. Para gerar seu site, use `/gerar-site`."

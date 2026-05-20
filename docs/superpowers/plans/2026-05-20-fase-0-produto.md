# Fase 0 — Produto: OS do Negócio (Template Base)

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Criar o template completo do OS do Negócio — estrutura de pastas, CLAUDE.md, arquivos de memória e todas as skills — para que o consultor consiga fazer a primeira entrega para um cliente.

**Architecture:** Um diretório `template-os-cliente/` dentro do repo `agencia-claude` que serve como base para clonar por cliente. As skills vivem em `.claude/commands/` como arquivos `.md` e são descobertas automaticamente pelo Claude Code. O CLAUDE.md na raiz é carregado automaticamente a cada sessão e instrui o modelo a ler os arquivos de memória antes de qualquer resposta.

**Tech Stack:** Claude Code (slash commands via `.claude/commands/`), Markdown, HTML/CSS puro (sem framework), Git/GitHub.

---

## Estrutura de arquivos

```
template-os-cliente/
├── CLAUDE.md                            ← contexto carregado automaticamente
├── .claude/
│   ├── settings.json                    ← permissões básicas
│   └── commands/
│       ├── instalar.md                  ← onboarding guiado
│       ├── abrir.md                     ← abre sessão com resumo do contexto
│       ├── salvar.md                    ← commita no GitHub
│       ├── atualizar.md                 ← sincroniza memória
│       ├── diagnostico.md               ← mapeamento de gargalos (growth lens)
│       ├── gerar-site.md                ← cria/atualiza site
│       ├── gerar-link-page.md           ← cria/atualiza link page
│       ├── carrossel.md                 ← gera carrossel
│       ├── legenda.md                   ← gera legenda
│       ├── pauta-conteudo.md            ← gera pauta mensal
│       ├── proposta.md                  ← gera proposta comercial
│       ├── resposta-cliente.md          ← gera resposta para cliente
│       └── mapear-rotinas.md            ← identifica tarefas repetitivas
├── _memoria/
│   ├── empresa.md                       ← produtos, preços, diferenciais
│   ├── preferencias.md                  ← voz, tom, o que evitar
│   ├── estrategia.md                    ← prioridades e metas do período
│   └── diagnostico.md                   ← gargalos identificados
├── identidade/
│   └── design-guide.md                  ← cores, fontes, logo
├── site/
│   └── index.html                       ← site de conversão
├── link-page/
│   └── index.html                       ← link page da bio do Instagram
└── outputs/
    ├── conteudo/.gitkeep
    ├── propostas/.gitkeep
    └── relatorios/.gitkeep
```

---

## Task 1: Estrutura de pastas base

**Files:**
- Create: `template-os-cliente/outputs/conteudo/.gitkeep`
- Create: `template-os-cliente/outputs/propostas/.gitkeep`
- Create: `template-os-cliente/outputs/relatorios/.gitkeep`
- Create: `template-os-cliente/identidade/.gitkeep`
- Create: `template-os-cliente/site/.gitkeep`
- Create: `template-os-cliente/link-page/.gitkeep`
- Create: `template-os-cliente/_memoria/.gitkeep`

- [ ] **Passo 1: Criar as pastas com .gitkeep**

```bash
mkdir -p template-os-cliente/.claude/commands
mkdir -p template-os-cliente/_memoria
mkdir -p template-os-cliente/identidade
mkdir -p template-os-cliente/site
mkdir -p template-os-cliente/link-page
mkdir -p template-os-cliente/outputs/conteudo
mkdir -p template-os-cliente/outputs/propostas
mkdir -p template-os-cliente/outputs/relatorios
touch template-os-cliente/outputs/conteudo/.gitkeep
touch template-os-cliente/outputs/propostas/.gitkeep
touch template-os-cliente/outputs/relatorios/.gitkeep
```

- [ ] **Passo 2: Verificar estrutura**

```bash
find template-os-cliente -type d
```

Esperado: todas as pastas listadas acima aparecem.

- [ ] **Passo 3: Commit**

```bash
git add template-os-cliente/
git commit -m "feat: estrutura base de pastas do template OS"
```

---

## Task 2: CLAUDE.md

**Files:**
- Create: `template-os-cliente/CLAUDE.md`

O CLAUDE.md é o arquivo mais importante — é carregado automaticamente pelo Claude Code a cada sessão e define como o modelo deve se comportar para este cliente.

- [ ] **Passo 1: Criar CLAUDE.md**

Criar `template-os-cliente/CLAUDE.md` com o conteúdo abaixo. Os campos entre `[colchetes]` são preenchidos durante o `/instalar`.

```markdown
# [NOME DA EMPRESA] — IA do Negócio

Você é a IA de [NOME DA EMPRESA]. Antes de qualquer resposta, leia os arquivos de contexto abaixo para garantir que suas respostas reflitam o negócio real.

## Arquivos de contexto — leia sempre antes de responder

- `_memoria/empresa.md` — o que o negócio faz, produtos, preços, diferenciais
- `_memoria/preferencias.md` — voz, tom, o que evitar na comunicação
- `_memoria/estrategia.md` — prioridades atuais e metas do período
- `_memoria/diagnostico.md` — gargalos identificados e oportunidades mapeadas

## Regras de comportamento

- Responda sempre no tom e voz definidos em `preferencias.md`
- Nunca invente produtos, preços ou informações não listadas em `empresa.md`
- Se uma pergunta exige informação que não está nos arquivos de contexto, diga ao dono que o arquivo precisa ser atualizado — não invente
- Quando gerar conteúdo (post, proposta, resposta), use os produtos e preços reais do `empresa.md`
- Quando salvar algo, use `/salvar` para versionar no GitHub

## Skills disponíveis

| Skill | O que faz |
|---|---|
| `/instalar` | Configura o sistema pela primeira vez com as informações do negócio |
| `/abrir` | Inicia a sessão com um resumo do contexto atual |
| `/salvar` | Salva e versiona tudo no GitHub |
| `/atualizar` | Atualiza os arquivos de memória quando o negócio muda |
| `/diagnostico` | Mapeia gargalos operacionais e oportunidades de crescimento |
| `/gerar-site` | Cria ou atualiza o site de conversão |
| `/gerar-link-page` | Cria ou atualiza a link page da bio do Instagram |
| `/carrossel` | Gera carrossel para Instagram com voz e produtos do negócio |
| `/legenda` | Gera legenda para post |
| `/pauta-conteudo` | Gera pauta de conteúdo para o mês |
| `/proposta` | Gera proposta comercial para um cliente específico |
| `/resposta-cliente` | Gera resposta para mensagem de cliente |
| `/mapear-rotinas` | Identifica tarefas repetitivas e sugere novas skills |
```

- [ ] **Passo 2: Verificar**

Abrir `template-os-cliente/CLAUDE.md` e confirmar que o conteúdo está correto.

- [ ] **Passo 3: Commit**

```bash
git add template-os-cliente/CLAUDE.md
git commit -m "feat: CLAUDE.md base do template OS"
```

---

## Task 3: settings.json e arquivos de memória

**Files:**
- Create: `template-os-cliente/.claude/settings.json`
- Create: `template-os-cliente/_memoria/empresa.md`
- Create: `template-os-cliente/_memoria/preferencias.md`
- Create: `template-os-cliente/_memoria/estrategia.md`
- Create: `template-os-cliente/_memoria/diagnostico.md`

- [ ] **Passo 1: Criar settings.json**

Criar `template-os-cliente/.claude/settings.json`:

```json
{
  "permissions": {
    "allow": [
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(git push:*)",
      "Bash(git status:*)",
      "Bash(git log:*)"
    ]
  }
}
```

- [ ] **Passo 2: Criar empresa.md**

Criar `template-os-cliente/_memoria/empresa.md`:

```markdown
# Empresa

## Sobre o negócio
[Descrição do que a empresa faz — preenchido no /instalar]

## Produtos e serviços
[Lista com nome, descrição e preço de cada produto/serviço]

## Clientes ideais
[Perfil de quem compra: cargo, dor principal, o que valoriza]

## Diferenciais
[O que nos diferencia da concorrência]

## Localização e contato
- Cidade: [cidade]
- WhatsApp: [número]
- Instagram: [@ do perfil]
- Site: [URL]

## Informações de operação
[Horários, formas de pagamento, prazo de entrega — o que for relevante]
```

- [ ] **Passo 3: Criar preferencias.md**

Criar `template-os-cliente/_memoria/preferencias.md`:

```markdown
# Preferências de Comunicação

## Tom de voz
[Ex: direto e objetivo / próximo e informal / técnico mas acessível]

## O que sempre fazer
[Ex: usar linguagem simples, citar exemplos práticos, começar pelo benefício]

## O que nunca fazer
[Ex: usar palavrões, prometer prazos sem confirmar, falar mal de concorrentes]

## Emojis
[Ex: sim, com moderação / não usa / só nos posts informais]

## Assinatura
[Como o dono assina mensagens para clientes]

## Exemplos de tom certo
[2-3 exemplos de mensagens que o dono já enviou e gostou]
```

- [ ] **Passo 4: Criar estrategia.md**

Criar `template-os-cliente/_memoria/estrategia.md`:

```markdown
# Estratégia Atual

## Foco do momento
[O que é prioridade agora — ex: fechar 5 clientes novos, reduzir cancelamentos, lançar novo produto]

## Meta do mês
[Meta específica e mensurável]

## Meta do trimestre
[Meta maior do período]

## O que NÃO fazer agora
[Distrações e projetos que estão pausados intencionalmente]

## Última atualização
[Data]
```

- [ ] **Passo 5: Criar diagnostico.md**

Criar `template-os-cliente/_memoria/diagnostico.md`:

```markdown
# Diagnóstico do Negócio

## Gargalos identificados
[Lista dos principais problemas operacionais — preenchido no /diagnostico]

## Oportunidades mapeadas
[Onde está o dinheiro que ainda não está sendo capturado]

## Métricas-chave
- Faturamento mensal estimado: [valor]
- Ticket médio: [valor]
- Volume de clientes/mês: [número]
- Principal canal de aquisição: [canal]
- CAC estimado: [valor ou "desconhecido"]

## Próximos passos recomendados
[O que resolver primeiro, com base no diagnóstico]

## Data do diagnóstico
[Data]
```

- [ ] **Passo 6: Commit**

```bash
git add template-os-cliente/.claude/settings.json template-os-cliente/_memoria/
git commit -m "feat: settings.json e arquivos de memória base"
```

---

## Task 4: identidade/design-guide.md

**Files:**
- Create: `template-os-cliente/identidade/design-guide.md`

- [ ] **Passo 1: Criar design-guide.md**

Criar `template-os-cliente/identidade/design-guide.md`:

```markdown
# Guia de Identidade Visual

## Cores

| Papel | Cor | Hex |
|---|---|---|
| Primária | [nome] | #000000 |
| Secundária | [nome] | #000000 |
| Fundo | [nome] | #000000 |
| Texto | [nome] | #000000 |

## Tipografia

- Título: [fonte]
- Corpo: [fonte]
- Destaque: [fonte]

## Logo

- Arquivo: `identidade/logo.png`
- Variações disponíveis: [ex: fundo claro, fundo escuro, ícone solo]
- Área de proteção: [ex: não colocar nada a menos de 20px da logo]

## Tom visual

[Descrever o estilo das imagens: ex: fotos reais, fundo branco, sem filtros exagerados]

## Referências

[Links ou descrições de marcas/posts que têm o visual certo]

## O que evitar

[Ex: cores neon, fontes decorativas, fotos com marca d'água]
```

- [ ] **Passo 2: Commit**

```bash
git add template-os-cliente/identidade/
git commit -m "feat: template de guia de identidade visual"
```

---

## Task 5: Skill /instalar

**Files:**
- Create: `template-os-cliente/.claude/commands/instalar.md`

A skill mais crítica. Conduz a entrevista de onboarding com o dono e popula todos os arquivos de memória e identidade automaticamente.

- [ ] **Passo 1: Criar instalar.md**

Criar `template-os-cliente/.claude/commands/instalar.md`:

```markdown
Você vai conduzir o onboarding do negócio. Seu objetivo é coletar todas as informações necessárias para configurar o sistema e no final popular automaticamente os arquivos de memória e identidade.

## Instruções

Faça as perguntas abaixo uma de cada vez. Espere a resposta antes de passar para a próxima. Use tom conversacional — não pareça um formulário.

Quando terminar todas as perguntas, informe o dono que vai salvar as informações e popule os arquivos conforme indicado.

---

## Perguntas de onboarding

**1. Sobre o negócio**
"Vamos começar pelo básico: me conta o que você faz. O que sua empresa entrega, para quem, e o que diferencia você da concorrência?"

→ Salvar em `_memoria/empresa.md` — seção "Sobre o negócio" e "Diferenciais"

**2. Produtos e serviços**
"Quais são seus produtos ou serviços principais? Me dá o nome, uma descrição rápida e o preço de cada um."

→ Salvar em `_memoria/empresa.md` — seção "Produtos e serviços"

**3. Cliente ideal**
"Quem é o cliente que você mais gosta de atender? Descreve o perfil: cargo, tipo de negócio, qual dor principal ele resolve quando te contrata."

→ Salvar em `_memoria/empresa.md` — seção "Clientes ideais"

**4. Contato e localização**
"Qual é o seu WhatsApp de contato, @ do Instagram, cidade e site (se tiver)?"

→ Salvar em `_memoria/empresa.md` — seção "Localização e contato"

**5. Tom de voz**
"Como você gosta de se comunicar com clientes? Mais formal ou informal? Tem alguma expressão que você usa muito, ou coisa que você odeia quando uma empresa faz na comunicação?"

→ Salvar em `_memoria/preferencias.md` — seções "Tom de voz", "O que sempre fazer" e "O que nunca fazer"

**6. Exemplos de comunicação**
"Me manda um exemplo de mensagem que você já enviou para um cliente e ficou satisfeito com o resultado — pode ser WhatsApp, e-mail, legenda de post, qualquer coisa."

→ Salvar em `_memoria/preferencias.md` — seção "Exemplos de tom certo"

**7. Identidade visual**
"Quais são as cores principais da sua marca? Tem alguma fonte específica? Me descreve o estilo visual que você usa — minimalista, vibrante, profissional, descontraído..."

→ Salvar em `identidade/design-guide.md` — seções "Cores" e "Tom visual"

**8. Foco atual**
"O que é prioridade para você agora? Qual é a meta do próximo mês?"

→ Salvar em `_memoria/estrategia.md` — seções "Foco do momento" e "Meta do mês"

**9. Gargalos**
"Qual é a maior dor operacional do seu negócio hoje — o que te consome mais tempo ou onde você sente que está perdendo dinheiro?"

→ Salvar em `_memoria/diagnostico.md` — seção "Gargalos identificados"

---

## Após coletar todas as respostas

1. Informe: "Vou salvar tudo agora. Um momento."
2. Popule cada arquivo de memória com as informações coletadas, substituindo os campos entre [colchetes]
3. Atualize o `CLAUDE.md` substituindo [NOME DA EMPRESA] pelo nome real
4. Informe: "Pronto! O sistema está configurado com as informações do seu negócio. Para começar qualquer sessão futura, use `/abrir`. Para criar conteúdo, use `/carrossel`, `/legenda` ou `/pauta-conteudo`. Para gerar seu site, use `/gerar-site`."
```

- [ ] **Passo 2: Testar a skill**

Abrir uma sessão do Claude Code dentro da pasta `template-os-cliente/` e digitar `/instalar`. Verificar que:
- O Claude conduz as perguntas uma por uma
- Ao fim, popula os arquivos de memória com as respostas
- Atualiza o CLAUDE.md com o nome da empresa

- [ ] **Passo 3: Commit**

```bash
git add template-os-cliente/.claude/commands/instalar.md
git commit -m "feat: skill /instalar — onboarding guiado"
```

---

## Task 6: Skills de sessão (/abrir, /salvar, /atualizar)

**Files:**
- Create: `template-os-cliente/.claude/commands/abrir.md`
- Create: `template-os-cliente/.claude/commands/salvar.md`
- Create: `template-os-cliente/.claude/commands/atualizar.md`

- [ ] **Passo 1: Criar abrir.md**

Criar `template-os-cliente/.claude/commands/abrir.md`:

```markdown
Leia os arquivos `_memoria/empresa.md`, `_memoria/preferencias.md` e `_memoria/estrategia.md` e exiba um resumo de contexto com o seguinte formato:

---
**[NOME DA EMPRESA] — sessão iniciada**

📌 Foco atual: [foco do momento do estrategia.md]
🎯 Meta do mês: [meta do mês do estrategia.md]
🗣️ Tom: [tom de voz do preferencias.md]

Pronto. O que vamos trabalhar hoje?
---

Seja breve — o resumo deve caber em 6 linhas no máximo.
```

- [ ] **Passo 2: Criar salvar.md**

Criar `template-os-cliente/.claude/commands/salvar.md`:

```markdown
Execute os seguintes passos em ordem:

1. Rode `git status` para ver o que mudou
2. Mostre ao dono um resumo das alterações: quais arquivos foram modificados e o que mudou (em linguagem simples, não técnica)
3. Pergunte: "Tem alguma descrição específica para esse save, ou pode salvar com uma mensagem automática?"
4. Se o dono der uma descrição, use ela como mensagem do commit
5. Se não, gere uma mensagem descritiva em português baseada nos arquivos modificados
6. Execute:
   ```
   git add -A
   git commit -m "[mensagem]"
   git push
   ```
7. Confirme: "Salvo! Tudo está no GitHub."

Se o git push falhar porque não há remote configurado, explique como configurar:
"Para salvar no GitHub, você precisa criar um repositório em github.com e conectar. Quer que eu te explique como fazer isso?"
```

- [ ] **Passo 3: Criar atualizar.md**

Criar `template-os-cliente/.claude/commands/atualizar.md`:

```markdown
O negócio muda — produtos novos, preços novos, foco novo. Esta skill sincroniza os arquivos de memória com a realidade atual.

Execute os seguintes passos:

1. Leia os arquivos `_memoria/empresa.md`, `_memoria/preferencias.md` e `_memoria/estrategia.md`
2. Pergunte ao dono: "O que mudou no negócio desde a última atualização? Pode ser novo produto, preço novo, mudança de foco, ou qualquer coisa relevante."
3. Com base na resposta, identifique quais seções de quais arquivos precisam ser atualizadas
4. Mostre ao dono o que vai mudar: "Vou atualizar [arquivo] — seção [seção]. Fica assim: [novo conteúdo]. Pode confirmar?"
5. Após confirmação, atualize os arquivos
6. Atualize também a data em `_memoria/estrategia.md`
7. Sugira usar `/salvar` para versionar as mudanças
```

- [ ] **Passo 4: Testar /abrir**

Dentro de `template-os-cliente/` (após rodar `/instalar`), digitar `/abrir`. Verificar que o resumo aparece com as informações corretas do negócio.

- [ ] **Passo 5: Commit**

```bash
git add template-os-cliente/.claude/commands/abrir.md template-os-cliente/.claude/commands/salvar.md template-os-cliente/.claude/commands/atualizar.md
git commit -m "feat: skills /abrir, /salvar, /atualizar"
```

---

## Task 7: Skill /diagnostico

**Files:**
- Create: `template-os-cliente/.claude/commands/diagnostico.md`

Skill diferencial — aplica a lens de growth (gargalo, CAC, conversão, operação) para mapear onde o negócio está perdendo dinheiro ou oportunidade.

- [ ] **Passo 1: Criar diagnostico.md**

Criar `template-os-cliente/.claude/commands/diagnostico.md`:

```markdown
Você vai conduzir um diagnóstico de negócio orientado a crescimento. Seu objetivo é identificar onde o dono está perdendo dinheiro ou oportunidade, e o que resolver primeiro para ter o maior impacto.

Leia `_memoria/empresa.md` e `_memoria/estrategia.md` antes de começar.

## Perguntas do diagnóstico

Faça uma pergunta por vez. Adapte o tom ao que você já sabe do negócio.

**Aquisição**
"Como seus clientes te encontram hoje? Qual canal traz mais resultado, e qual você sente que poderia trazer mas não traz?"

**Conversão**
"Quando um lead aparece, qual é o processo até ele fechar? Onde você sente que mais gente desiste sem comprar?"

**Ticket e recorrência**
"Qual é seu ticket médio hoje? Os clientes voltam a comprar, ou é sempre cliente novo?"

**Operação**
"Qual tarefa do dia a dia te consome mais tempo e poderia ser automatizada ou delegada?"

**Pós-venda**
"O que acontece depois que o cliente compra? Tem algum processo de acompanhamento, ou o contato para depois da entrega?"

**Vazamento financeiro**
"Tem alguma coisa que você paga todo mês e não tem certeza se está trazendo retorno?"

---

## Após as perguntas

1. Com base nas respostas, identifique os 3 principais gargalos em ordem de impacto
2. Para cada gargalo, sugira uma ação concreta e realista
3. Apresente o diagnóstico no formato:

---
**Diagnóstico — [NOME DA EMPRESA]**

**Gargalo 1 — [nome]:** [descrição do problema e impacto]
→ Ação: [o que fazer]

**Gargalo 2 — [nome]:** [descrição]
→ Ação: [o que fazer]

**Gargalo 3 — [nome]:** [descrição]
→ Ação: [o que fazer]

**Onde está o maior dinheiro:** [síntese de onde focar]
---

4. Pergunte: "Posso salvar esse diagnóstico no sistema?"
5. Se confirmado, salve em `_memoria/diagnostico.md` e sugira `/salvar`
```

- [ ] **Passo 2: Commit**

```bash
git add template-os-cliente/.claude/commands/diagnostico.md
git commit -m "feat: skill /diagnostico — mapeamento de gargalos"
```

---

## Task 8: Skills de presença digital (/gerar-site, /gerar-link-page)

**Files:**
- Create: `template-os-cliente/.claude/commands/gerar-site.md`
- Create: `template-os-cliente/.claude/commands/gerar-link-page.md`
- Create: `template-os-cliente/site/index.html`
- Create: `template-os-cliente/link-page/index.html`

- [ ] **Passo 1: Criar gerar-site.md**

Criar `template-os-cliente/.claude/commands/gerar-site.md`:

```markdown
Leia os arquivos `_memoria/empresa.md` e `identidade/design-guide.md` antes de começar.

Crie ou atualize o arquivo `site/index.html` com um site de conversão para o negócio.

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
```

- [ ] **Passo 2: Criar gerar-link-page.md**

Criar `template-os-cliente/.claude/commands/gerar-link-page.md`:

```markdown
Leia os arquivos `_memoria/empresa.md` e `identidade/design-guide.md` antes de começar.

Crie ou atualize o arquivo `link-page/index.html` com uma link page para a bio do Instagram.

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

- HTML e CSS inline — sem dependências externas
- Design vertical centralizado, otimizado para mobile
- Cores e tipografia do `identidade/design-guide.md`
- Cada botão tem cor e estilo consistentes com a identidade

## Ao finalizar

Mostre ao dono: "Link page gerada em `link-page/index.html`. Para usar, hospede o arquivo (GitHub Pages, por exemplo) e coloque o link na bio do Instagram. Quer ajustar algum link ou texto?"
```

- [ ] **Passo 3: Commit**

```bash
git add template-os-cliente/.claude/commands/gerar-site.md template-os-cliente/.claude/commands/gerar-link-page.md
git commit -m "feat: skills /gerar-site e /gerar-link-page"
```

---

## Task 9: Skills de conteúdo (/carrossel, /legenda, /pauta-conteudo)

**Files:**
- Create: `template-os-cliente/.claude/commands/carrossel.md`
- Create: `template-os-cliente/.claude/commands/legenda.md`
- Create: `template-os-cliente/.claude/commands/pauta-conteudo.md`

- [ ] **Passo 1: Criar carrossel.md**

Criar `template-os-cliente/.claude/commands/carrossel.md`:

```markdown
Leia `_memoria/empresa.md` e `_memoria/preferencias.md` antes de começar.

Você vai criar o roteiro de um carrossel para Instagram.

## Perguntas

Faça uma pergunta por vez:

1. "Qual é o tema ou assunto do carrossel? Pode ser um produto, uma dica, uma objeção de cliente, um bastidor — o que você quer falar?"
2. "Qual é o objetivo? (marcar alguém, gerar mensagem no WhatsApp, informar, mostrar resultado)"

## Formato de saída

Gere o roteiro do carrossel no seguinte formato:

---
**Capa (slide 1)**
Headline: [frase de gancho — máximo 8 palavras]
Subheadline: [complemento opcional]

**Slide 2**
Título: [tópico]
Texto: [2-3 linhas no máximo]

**Slide 3**
[repetir estrutura]

...(até 7 slides de conteúdo)

**Slide final**
CTA: [chamada para ação clara — ex: "Manda uma mensagem no WhatsApp"]
---

Use o tom do `preferencias.md`. Use produtos/serviços reais do `empresa.md` quando relevante. Salve o roteiro em `outputs/conteudo/carrossel-[tema]-[data].md`.
```

- [ ] **Passo 2: Criar legenda.md**

Criar `template-os-cliente/.claude/commands/legenda.md`:

```markdown
Leia `_memoria/empresa.md` e `_memoria/preferencias.md` antes de começar.

Você vai criar uma legenda para post no Instagram.

## Perguntas

1. "O que é o post? (foto de produto, bastidor, resultado de cliente, dica, promoção)"
2. "Qual ação você quer que a pessoa tome? (salvar, comentar, mandar mensagem, comprar)"

## Formato de saída

Gere 2 versões da legenda:

**Versão A — mais curta (até 5 linhas)**
[legenda]
[hashtags — máximo 5, relevantes]

**Versão B — mais longa (até 15 linhas)**
[legenda com mais contexto e storytelling]
[hashtags — máximo 10]

Use o tom do `preferencias.md`. Se a legenda mencionar produto, use os produtos reais do `empresa.md`.
```

- [ ] **Passo 3: Criar pauta-conteudo.md**

Criar `template-os-cliente/.claude/commands/pauta-conteudo.md`:

```markdown
Leia `_memoria/empresa.md`, `_memoria/preferencias.md` e `_memoria/estrategia.md` antes de começar.

Você vai criar uma pauta de conteúdo para o mês.

## Perguntas

1. "Quantos posts por semana você quer fazer?"
2. "Tem algum produto, serviço ou data importante esse mês que precisa aparecer na pauta?"

## Formato de saída

Gere uma pauta mensal no formato:

---
**Pauta de Conteúdo — [Mês/Ano]**
Frequência: [X posts/semana]

**Semana 1**
- Post 1: [tema] | Formato: [carrossel/foto/reels] | Objetivo: [awareness/conversão/relacionamento]
- Post 2: [tema] | Formato: [...] | Objetivo: [...]

**Semana 2**
[...]

**Semana 3**
[...]

**Semana 4**
[...]
---

Distribua os temas equilibrando: educação (40%), prova social/resultado (30%), bastidor/humanização (20%), oferta direta (10%).

Salve em `outputs/conteudo/pauta-[mes]-[ano].md`.
```

- [ ] **Passo 4: Commit**

```bash
git add template-os-cliente/.claude/commands/carrossel.md template-os-cliente/.claude/commands/legenda.md template-os-cliente/.claude/commands/pauta-conteudo.md
git commit -m "feat: skills de conteúdo — /carrossel, /legenda, /pauta-conteudo"
```

---

## Task 10: Skills comerciais (/proposta, /resposta-cliente)

**Files:**
- Create: `template-os-cliente/.claude/commands/proposta.md`
- Create: `template-os-cliente/.claude/commands/resposta-cliente.md`

- [ ] **Passo 1: Criar proposta.md**

Criar `template-os-cliente/.claude/commands/proposta.md`:

```markdown
Leia `_memoria/empresa.md` e `_memoria/preferencias.md` antes de começar.

Você vai criar uma proposta comercial personalizada.

## Perguntas

1. "Para quem é a proposta? Me conta sobre o cliente — nome, negócio, o que ele precisa."
2. "Qual produto ou serviço você vai oferecer? Tem alguma condição especial (desconto, prazo diferente)?"

## Formato de saída

Gere a proposta no seguinte formato:

---
**Proposta Comercial**
Para: [Nome do cliente / Empresa]
De: [Nome da empresa]
Data: [data atual]

**Entendemos que você precisa de:**
[Resumo do problema/necessidade do cliente em 2-3 linhas]

**Nossa solução:**
[Descrição do que será entregue]

**O que está incluso:**
- [item 1]
- [item 2]
- [...]

**Investimento:**
[Valor] à vista ou [parcelas]

**Prazo de entrega:**
[prazo]

**Próximo passo:**
[CTA — ex: "Responda essa mensagem para confirmarmos"]

[Nome da empresa]
[WhatsApp]
---

Use o tom do `preferencias.md`. Use os dados reais do `empresa.md`. Salve em `outputs/propostas/proposta-[cliente]-[data].md`.
```

- [ ] **Passo 2: Criar resposta-cliente.md**

Criar `template-os-cliente/.claude/commands/resposta-cliente.md`:

```markdown
Leia `_memoria/empresa.md` e `_memoria/preferencias.md` antes de começar.

Você vai criar uma resposta para uma mensagem de cliente.

## Perguntas

1. "Me manda a mensagem do cliente (pode copiar e colar)."
2. "Qual é o contexto? (lead novo, cliente que já comprou, alguém com reclamação, pedindo orçamento)"

## Instruções

- Use o tom definido em `preferencias.md`
- Se a mensagem pede informação sobre produto ou preço, use os dados reais do `empresa.md`
- Se a mensagem é uma objeção, trate com empatia antes de argumentar
- Seja objetivo — não enrole

## Formato de saída

Gere 2 versões:

**Versão A — mais curta**
[resposta direta]

**Versão B — mais elaborada**
[resposta com mais contexto ou persuasão]

Indique qual versão você recomenda e por quê.
```

- [ ] **Passo 3: Commit**

```bash
git add template-os-cliente/.claude/commands/proposta.md template-os-cliente/.claude/commands/resposta-cliente.md
git commit -m "feat: skills comerciais — /proposta, /resposta-cliente"
```

---

## Task 11: Skill /mapear-rotinas

**Files:**
- Create: `template-os-cliente/.claude/commands/mapear-rotinas.md`

- [ ] **Passo 1: Criar mapear-rotinas.md**

Criar `template-os-cliente/.claude/commands/mapear-rotinas.md`:

```markdown
Leia `_memoria/empresa.md` e `_memoria/diagnostico.md` antes de começar.

Você vai identificar tarefas repetitivas do negócio e sugerir novas skills para automatizá-las.

## Perguntas

1. "Me conta as tarefas que você faz toda semana no negócio — pode ser qualquer coisa: responder cliente, montar relatório, criar proposta, organizar pedidos, o que for."
2. "Qual dessas tarefas te toma mais tempo e você mais odeia fazer?"

## Instruções

Com base nas respostas, identifique padrões repetitivos que podem virar skills do Claude Code.

Para cada oportunidade identificada, apresente:

---
**Skill sugerida: /[nome]**
O que faz: [descrição em 1 linha]
Tempo economizado: [estimativa]
Quando usar: [gatilho — ex: "toda vez que precisar criar uma proposta"]
---

No final, pergunte: "Quer que eu crie alguma dessas skills agora?"

Se o dono confirmar, crie o arquivo `.claude/commands/[nome].md` com as instruções da skill, seguindo o padrão das skills existentes.
```

- [ ] **Passo 2: Commit**

```bash
git add template-os-cliente/.claude/commands/mapear-rotinas.md
git commit -m "feat: skill /mapear-rotinas"
```

---

## Task 12: README do template

**Files:**
- Create: `template-os-cliente/README.md`

- [ ] **Passo 1: Criar README.md**

Criar `template-os-cliente/README.md`:

```markdown
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
| `/legenda` | Gera legenda para post |
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
```

- [ ] **Passo 2: Commit final**

```bash
git add template-os-cliente/README.md
git commit -m "feat: README do template OS do Negócio — fase 0 completa"
```

---

## Validação final

Após concluir todas as tasks:

- [ ] Abrir `template-os-cliente/` no Claude Code
- [ ] Rodar `/instalar` com dados fictícios de um negócio de teste (ex: barbearia)
- [ ] Verificar que os arquivos de memória foram populados corretamente
- [ ] Rodar `/abrir` e verificar que o resumo aparece com os dados do teste
- [ ] Rodar `/carrossel` e verificar que o output usa os dados do negócio (não dados genéricos)
- [ ] Rodar `/gerar-site` e abrir `site/index.html` no browser para verificar o resultado
- [ ] Rodar `/salvar` e verificar que o commit é criado
- [ ] Se tudo passou: o produto está pronto para a primeira entrega real (Fase 1)

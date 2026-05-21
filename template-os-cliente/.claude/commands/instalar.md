# /instalar — Configuração inicial do sistema

Esse é o primeiro comando a rodar depois de clonar o repositório. Não pode soar burocrático — é uma conversa de descoberta. Faz uma pergunta por vez, espera a resposta, não enfileira tudo. O objetivo é o sistema sair daqui sabendo quem é o negócio, como ele fala, onde está o dinheiro e onde estão os gargalos.

---

## Pré-checagem

### 1. Nome da pasta

Conferir o nome da pasta atual. Se for `template-os-cliente`, `mazyos`, `os-negocio` ou variação genérica, avisar:

> "A pasta ainda tem nome genérico ('[nome-atual]'). O ideal é ela ter o nome do seu negócio. Quando terminarmos o setup, te lembro de renomear — é rápido. Bora seguir?"

Registrar mentalmente para usar na Fase 5.

### 2. Arquivos de contexto

Verificar se algum arquivo de memória já tem conteúdo real (não só placeholders):
- `_memoria/empresa.md`
- `_memoria/preferencias.md`
- `_memoria/estrategia.md`
- `_memoria/diagnostico.md`

Se algum já tiver conteúdo, perguntar:

> "Já tem contexto preenchido aqui. Quer recomeçar do zero ou complementar o que falta?"

Se for setup limpo, seguir direto.

---

## Fase 1 — Perfil do negócio

Perguntar qual perfil mais combina:

1. **Profissional solo / autônomo** — trabalha sozinho, mistura marca pessoal e negócio
2. **Negócio pequeno** — até 5 pessoas, operação simples, dono faz tudo
3. **Negócio em crescimento** — time de 5 a 20 pessoas, quer escalar sem perder o controle
4. **Empresa estruturada** — 20+ pessoas, múltiplas áreas, decisão descentralizada

A resposta calibra o tom das sugestões e o nível de complexidade das skills.

---

## Fase 2 — Entrevista

Fazer as perguntas em ordem, esperando a resposta de cada uma antes de seguir. Se a resposta vier vaga, pedir concretude uma vez. Não insistir — registrar o que veio.

**Sobre o negócio:**

1. "Como você chama o que você faz? (nome da empresa, ou seu nome se for marca pessoal)"

2. "O que você entrega, em uma frase do jeito que explicaria num papo casual com um cliente em potencial?"

3. "Quem te paga? Descreve o perfil do cliente real — sem persona de marketing, o tipo de pessoa mesmo. O que ela faz, o que a faz te contratar?"

4. "Você toca sozinho ou tem equipe? Se tem, quantos e o que cada um faz no dia a dia?"

**Sobre voz:**

5. "Me cola um exemplo de como você escreve pro cliente — mensagem de WhatsApp, legenda do Instagram, email, o que tiver de recente. Assim eu calibro o jeito de escrever sem precisar adivinhar."

6. "O que te irrita quando uma empresa escreve assim? Pode ser expressão, formato, tom — qualquer coisa que você odeia ver."

**Sobre crescimento:**

7. "Como os seus clientes chegam até você hoje? (indicação, Instagram, Google, tráfego pago, visita física...) E qual canal você sente que poderia trazer mais e ainda não traz?"

8. "Me dá uma estimativa do negócio hoje: faturamento mensal (pode ser uma faixa), ticket médio e quantos clientes novos entram por mês."

9. "O que está segurando o crescimento do negócio? Qual é o gargalo principal — onde você sente que está perdendo dinheiro ou oportunidade?"

**Sobre rotina:**

10. "Se eu pudesse tirar UMA coisa que você repete toda semana das suas costas, o que seria?"

**Sobre identidade e presença:**

11. "Tem identidade visual definida? Se sim, quais são as cores principais e a fonte. Se tem logo, coloca o arquivo em `identidade/logo.png` e me confirma."

12. "Qual é o seu WhatsApp de contato, @ do Instagram, cidade e site (se já tiver)?"

---

## Fase 3 — Preenchimento dos arquivos

### `_memoria/empresa.md`
Preencher com base nas perguntas 1-4. Estrutura: nome do negócio, o que entrega, perfil de cliente real, equipe. Sem placeholder — só o que foi respondido.

### `_memoria/preferencias.md`
Preencher com base nas perguntas 5-6. Estrutura:
- **Tom de voz:** derivar do exemplo real da pergunta 5 — descrever em 2-3 frases o jeito de escrever, com referência ao exemplo
- **O que evitar:** lista direta das respostas 5 e 6
- **Assinatura:** se aparecer no exemplo da pergunta 5, capturar

### `_memoria/estrategia.md`
Preencher com base nas perguntas 7 e 9. Estrutura:
- **Canal de aquisição atual:** resposta da 7
- **Foco do momento:** derivar do gargalo da pergunta 9
- **Meta do mês:** deixar em branco por ora — preencher com `/atualizar` quando o dono definir

### `_memoria/diagnostico.md`
Preencher com base nas perguntas 8 e 9. Estrutura:
- **Métricas-chave:** faturamento estimado, ticket médio, clientes/mês da pergunta 8
- **Gargalo principal:** resposta da pergunta 9
- **Tarefa repetitiva para automatizar:** resposta da pergunta 10 — candidata a skill via `/mapear-rotinas`
- **Canal com maior potencial não explorado:** resposta da pergunta 7

### `identidade/design-guide.md`
Se o dono forneceu cores, fonte ou logo (pergunta 11), preencher os campos correspondentes. Se não:
> "Deixei o `identidade/design-guide.md` em branco. Quando você definir a identidade visual, edita lá — as skills de site, link page e carrossel leem esse arquivo antes de criar qualquer visual."

### `_memoria/empresa.md` — contato
Adicionar os dados da pergunta 12 na seção "Localização e contato".

### `CLAUDE.md`
Substituir `[NOME DA EMPRESA]` pelo nome real respondido na pergunta 1.

---

## Fase 4 — Resumo

Mostrar o que foi configurado:

```
✓ Perfil: [perfil]
✓ Negócio: _memoria/empresa.md
✓ Tom de voz: _memoria/preferencias.md
✓ Foco e canal: _memoria/estrategia.md
✓ Diagnóstico inicial: _memoria/diagnostico.md
✓ Identidade visual: identidade/design-guide.md  [preenchida | em branco — preencher depois]
✓ CLAUDE.md atualizado com o nome do negócio
```

---

## Fase 5 — Renomear pasta (se necessário)

Se a pasta ainda tem nome genérico, gerar slug do nome do negócio (resposta da pergunta 1):
- minúsculas, sem acentos, espaços viram hífen, caracteres especiais removidos

Ex: "Espaço Vitta" → `espaco-vitta`

Mostrar:

> "Última coisa: a pasta ainda está com nome genérico ('[nome-atual]').
> Para ter a cara do negócio, recomendo renomear para '[slug]'.
>
> Como fazer:
> 1. Fecha o VS Code
> 2. Renomeia a pasta no Finder (Mac) ou Explorer (Windows)
> 3. Abre o VS Code de novo na pasta renomeada
>
> Se preferir outro nome, me fala."

Se a pasta já tem nome próprio, pular essa fase.

---

## Fase 6 — Próximos passos

> "Pronto. O sistema já conhece o seu negócio.
>
> No começo de cada sessão, roda `/abrir` — eu carrego tudo que combinamos aqui antes da primeira resposta. Para gerar seu site, roda `/gerar-site`. Para criar conteúdo, use `/carrossel` ou `/legenda`.
>
> Você mencionou que repete '[resposta da pergunta 10]' toda semana. Quando quiser tirar isso das costas de vez, roda `/mapear-rotinas` — a gente transforma isso em skill."

---

## Regras

- Não inventar dados — se a resposta for vaga, registrar do jeito que veio
- Não escrever avisos de placeholder nos arquivos finais — os colchetes saem depois do /instalar
- Setup máximo de 5-7 minutos. Se o dono enrolar numa pergunta, registra o que tem e segue
- Não fazer perguntas extras além das listadas sem motivo claro

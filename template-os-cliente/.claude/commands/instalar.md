# /instalar — Configuração inicial do sistema

Esse é o primeiro comando a rodar depois de clonar o repositório. Não pode soar burocrático — é uma conversa de descoberta. Faz uma pergunta por vez, espera a resposta, não enfileira tudo. O objetivo é o sistema sair daqui sabendo quem é o negócio, como ele fala, onde está o dinheiro e onde estão os gargalos.

---

## Pré-checagem

### Arquivos de contexto

Ler os quatro arquivos de memória e o `identidade/design-guide.md`. Para cada seção, classificar:
- **Real** = texto sem colchetes `[...]`
- **Placeholder** = texto entre `[...]` ou seção vazia

**Cenário A — Setup limpo** (todos os campos são placeholder)
→ Seguir direto para a Fase 1.

**Cenário B — Setup incompleto** (alguns campos preenchidos, outros não)
→ Montar lista do que falta com base no mapeamento das perguntas abaixo.
→ Apresentar:

> "Já tem algumas informações aqui. Falta preencher: [lista curta das seções vazias]. Completo só o que falta ou você quer recomeçar do zero?"

→ Se "recomeçar": apagar conteúdo dos arquivos e rodar normalmente.
→ Se "complementar": ativar **modo seletivo** — em cada pergunta da Fase 2, verificar se o campo alvo já tem conteúdo real. Se sim, pular. Se não, fazer a pergunta.

**Cenário C — Setup completo** (todos os campos preenchidos)
→ Não rodar o fluxo. Avisar:

> "Todos os arquivos já estão preenchidos. Para atualizar alguma informação, use `/atualizar`. Quer recomeçar do zero mesmo assim?"

---

## Fase 1 — Perfil do negócio

Perguntar:

> "Antes de começar, me conta um pouco sobre o tamanho do negócio. Qual desses perfis mais se parece com você?"

Apresentar as opções:

1. **Profissional solo / autônomo** — trabalha sozinho, mistura marca pessoal e negócio
2. **Negócio pequeno** — até 5 pessoas, operação simples, dono faz tudo
3. **Negócio em crescimento** — time de 5 a 20 pessoas, quer escalar sem perder o controle
4. **Empresa estruturada** — 20+ pessoas, múltiplas áreas, decisão descentralizada

→ Salvar em `_memoria/empresa.md` — campo "Perfil do negócio"

A resposta calibra o tom das sugestões e o nível de complexidade das skills.

---

## Fase 2 — Entrevista

Fazer as perguntas em ordem, esperando a resposta de cada uma antes de seguir. Se a resposta vier vaga, pedir concretude uma vez. Não insistir — registrar o que veio.

**Em modo seletivo (complementar):** antes de cada pergunta, verificar se o campo alvo já tem conteúdo real. Se sim, pular silenciosamente e ir para a próxima.

**Sobre o negócio:**

1. "Qual é o nome da sua empresa ou da sua marca pessoal?"

→ Salvar em `_memoria/empresa.md` — campo "Nome do negócio" e atualizar o `CLAUDE.md`

2. "O que você entrega pro cliente? Me descreve em uma frase o que ele recebe quando te contrata — e quais são seus produtos ou serviços principais: nome, descrição rápida e preço de cada um."

→ Salvar em `_memoria/empresa.md` — seções "Sobre o negócio" e "Produtos e serviços"

3. "Quem é seu cliente? Descreve o perfil real — sem persona de marketing, a pessoa mesmo. O que essa pessoa faz, o que a leva a te contratar?"

→ Salvar em `_memoria/empresa.md` — seção "Clientes ideais"

4. "Você toca sozinho ou tem equipe? Se tem, quantos e o que cada um faz no dia a dia?"

→ Salvar em `_memoria/empresa.md` — seção "Equipe"

**Sobre voz:**

5. "Me cola um exemplo de como você escreve pro cliente — mensagem de WhatsApp, legenda do Instagram, email, o que tiver de recente. Assim eu calibro o jeito de escrever sem precisar adivinhar."

→ Salvar em `_memoria/preferencias.md` — seção "Exemplos de tom certo" + derivar "Tom de voz" a partir do exemplo

6. "O que você vê na comunicação das empresas que te irrita? Exemplo: gíria, emoji, apelido."

→ Salvar em `_memoria/preferencias.md` — seção "O que nunca fazer"

**Sobre crescimento:**

7. "De onde vêm seus clientes hoje? (ex: indicação de conhecido, Instagram, Google, evento, visita no local...) E de onde você sente que poderiam vir mais e ainda não vêm?"

→ Salvar em `_memoria/estrategia.md` — seção "Canal de aquisição atual" e `_memoria/diagnostico.md` — seção "Canal com maior potencial não explorado"

8. "Me dá uma estimativa do negócio hoje: faturamento mensal (pode ser uma faixa), ticket médio e quantos clientes novos entram por mês. Responde só o que souber — não precisa ter todos os números."

→ Salvar em `_memoria/diagnostico.md` — seção "Métricas-chave"

9. "O que está segurando o crescimento do negócio? Qual é o gargalo principal — onde você sente que está perdendo dinheiro ou oportunidade?"

→ Salvar em `_memoria/diagnostico.md` — seção "Gargalo principal" e `_memoria/estrategia.md` — seção "Foco do momento"

**Sobre rotina:**

10. "Se eu pudesse tirar UMA coisa que você repete toda semana das suas costas, o que seria?"

→ Salvar em `_memoria/diagnostico.md` — seção "Tarefa repetitiva para automatizar"

**Sobre identidade e presença:**

11. "Tem identidade visual definida? Se sim, quais são as cores principais e a fonte. Se tiver logo, pode enviar o arquivo aqui no chat — depois é só salvar como `identidade/logo.png` na pasta do negócio."

→ Salvar em `identidade/design-guide.md` — seções "Cores", "Tipografia" e "Logo"

12. "Qual é o seu WhatsApp de contato, @ do Instagram, cidade e site (se já tiver)?"

→ Salvar em `_memoria/empresa.md` — seção "Localização e contato"

---

## Fase 3 — Preenchimento dos arquivos

Preencher cada arquivo conforme os mapeamentos indicados em cada pergunta acima. Observações importantes:

- **Tom de voz em `preferencias.md`:** não copiar o exemplo da P5 literalmente — descrever em 2-3 frases o jeito de escrever que ele revela (ritmo, vocabulário, grau de formalidade)
- **Assinatura:** se aparecer no exemplo da P5, capturar em `preferencias.md`
- **Meta do mês em `estrategia.md`:** deixar em branco — preencher com `/atualizar` quando o dono definir
- **Identidade visual:** se o dono não forneceu cores/fonte na P11, avisar: "Deixei o `identidade/design-guide.md` em branco. Quando definir a identidade visual, edita lá — site, link page e carrossel leem esse arquivo antes de criar qualquer coisa."
- **CLAUDE.md:** substituir `[NOME DA EMPRESA]` pelo nome real da P1
- Sem placeholders nos arquivos finais — registrar só o que foi respondido

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

## Fase 5 — Próximos passos

> "Pronto. O sistema já conhece o seu negócio.
>
> No começo de cada sessão, roda `/abrir` — eu carrego tudo que combinamos aqui antes da primeira resposta. Para gerar seu site, roda `/gerar-site`. Para criar conteúdo, use `/carrossel` ou `/legenda`.
>
> Você mencionou que repete '[resposta da pergunta 10]' toda semana. Quando quiser tirar isso das costas de vez, roda `/mapear-rotinas` — a gente transforma isso em skill."

---

## Regras

- Não inventar dados — se a resposta for vaga, registrar do jeito que veio
- Não escrever avisos de placeholder nos arquivos finais — os colchetes saem depois do /instalar
- Setup máximo de 5-10 minutos. Se o dono enrolar numa pergunta, registra o que tem e segue
- Não fazer perguntas extras além das listadas sem motivo claro

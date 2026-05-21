# /mapear-rotinas

Identifique tarefas repetitivas do negócio e sugira novas skills para automatizá-las.

## Antes de começar

Leia `_memoria/empresa.md` e `_memoria/diagnostico.md` antes de começar.

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

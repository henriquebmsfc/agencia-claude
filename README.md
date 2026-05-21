# Agência Claude

Base de conhecimento estratégica da agência de implementação de IA para PMEs.

## O que é

Estrutura de arquivos que organiza posicionamento, ICP, precificação, playbooks de entrega e casos de clientes. Serve como referência central para projetos e como contexto para o Claude Code ao trabalhar em qualquer tarefa da agência.

## Estrutura

```
agencia-claude/
├── empresa/          # Posicionamento, ICP, precificação, equipe
├── mercado/          # Concorrentes, tendências, cases de referência
├── comercial/        # Pitch e template de proposta
├── conhecimento/
│   ├── playbooks/    # OS padrão e skills de entrega
│   │   └── skills/   # Skill de carrossel, legenda, documento, resposta, pauta
│   └── transcricoes/ # Aprendizado de cases e referências do mercado
├── casos/            # Projetos entregues (site + gestão)
└── docs/             # Specs e decisões de design
```

## O produto

Pacote base entregue em até 14 dias:

1. **O Cérebro** — IA configurada com o contexto completo do negócio
2. **Site** — Página de conversão responsiva com CTA para WhatsApp
3. **Link Page** — Substitui Linktree na bio do Instagram
4. **Skills de conteúdo** — Carrossel, legenda, orçamento, resposta para cliente, pauta mensal
5. **OS do Dono** — Onboarding de uso: o dono resolve situações do dia a dia com um prompt

## Como usar

Clone o repositório e abra no Claude Code. O contexto da agência fica disponível para qualquer tarefa.

```bash
git clone https://github.com/henriquebmsfc/agencia-claude.git
cd agencia-claude
claude
```

## Instalando o OS do Negócio para um cliente

Para cada novo cliente, baixe apenas a pasta `template-os-cliente` e renomeie para o nome do negócio:

```bash
# Substitua "nome-do-cliente" pelo nome real (ex: espaco-vitta, jotta-turism)
git clone --no-local --depth 1 --filter=blob:none --sparse \
  https://github.com/henriquebmsfc/agencia-claude.git nome-do-cliente
cd nome-do-cliente
git sparse-checkout set template-os-cliente
mv template-os-cliente/* .
mv template-os-cliente/.claude .
rm -rf template-os-cliente .git
```

Depois abra a pasta no Claude Code e rode `/instalar`.


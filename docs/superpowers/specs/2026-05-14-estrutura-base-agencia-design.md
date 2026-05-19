---
title: Estrutura Base da Agência
date: 2026-05-14
status: aprovado
---

## Contexto

Agência de implementação de IA para pequenas empresas. Modelo de entrega: projeto fechado (entrega única). Time: 2+ fundadores. Stack: mix de low-code (Make, n8n, Zapier) e desenvolvimento customizado. Segmento de mercado: a definir com os primeiros clientes.

## Objetivo

Criar uma estrutura de pastas e arquivos base que sirva como **base de conhecimento estratégica** da agência — orientação de mercado, ICP, posicionamento e repositório de aprendizado — sem overhead operacional desnecessário neste momento inicial.

## Estrutura de Pastas

```
agencia-claude/
│
├── empresa/
│   ├── visao-missao-valores.md
│   ├── icp.md
│   ├── posicionamento.md
│   └── precificacao.md
│
├── mercado/
│   ├── concorrentes.md
│   ├── tendencias.md
│   └── cases-referencia.md
│
├── conhecimento/
│   ├── transcricoes/
│   ├── playbooks/
│   └── ferramentas.md
│
└── comercial/
    ├── pitch.md
    └── proposta-template.md
```

## Decisões de Design

- **Minimalista agora**: sem pastas de projetos ou financeiro — adicionar quando houver volume
- **Arquivos .md**: fácil de editar, versionar e compartilhar entre sócios
- **`transcricoes/`**: pasta dedicada para ingestão de conteúdo de aprendizado (vídeos, podcasts)
- **`playbooks/`**: processos que serão desenvolvidos conforme os projetos acontecerem

## Fora de Escopo (por ora)

- Gestão de projetos e clientes
- Financeiro
- Templates técnicos de automação
- CRM

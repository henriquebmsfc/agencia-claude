---
title: GTM + Produto — Design Completo
date: 2026-05-20
status: aprovado
---

## Contexto

Consultoria de IA para PMEs com duas frentes de aquisição: (1) entregas gratuitas para conhecidos gerando cases e indicações pagas, e (2) conteúdo + tráfego pago para landing page. O produto é um OS (sistema operacional do negócio) entregue via Claude Code — repositório GitHub instalado e configurado pelo consultor, usado pelo dono da empresa no dia a dia.

Referência de mercado analisada: MazyOS (github.com/mazzeoia/MazyOS) — estrutura similar, usado como base de inspiração.

---

## Produto — OS do Negócio

### Estrutura de pastas (por cliente)

```
cliente-[nome]/
├── CLAUDE.md                  ← carrega contexto completo a cada sessão
├── .claude/
│   └── settings.json          ← registra todas as skills disponíveis
├── _memoria/
│   ├── empresa.md             ← o que o negócio faz, produtos, preços, diferenciais
│   ├── preferencias.md        ← voz, tom, o que evitar, como o dono se comunica
│   ├── estrategia.md          ← prioridades atuais, metas, foco do período
│   └── diagnostico.md         ← gargalos mapeados com lens de growth (diferencial)
├── identidade/
│   └── design-guide.md        ← cores, fontes, logo, referências visuais
├── site/
│   └── index.html             ← gerado e atualizado via skill /gerar-site
├── link-page/
│   └── index.html             ← gerado e atualizado via skill /gerar-link-page
└── outputs/
    ├── conteudo/
    ├── propostas/
    └── relatorios/
```

### Skills incluídas

| Skill | Função |
|---|---|
| `/instalar` | Onboarding guiado — entrevista o dono e popula todos os arquivos de memória |
| `/abrir` | Inicia sessão carregando contexto completo em poucas linhas |
| `/salvar` | Commita e versiona alterações no GitHub |
| `/atualizar` | Sincroniza memória quando o negócio muda |
| `/diagnostico` | Mapeamento de gargalos com lens de growth — CAC, conversão, operação |
| `/gerar-site` | Cria e atualiza o site de conversão a partir da memória |
| `/gerar-link-page` | Cria e atualiza a link page da bio do Instagram |
| `/carrossel` | Gera carrossel com voz e branding do negócio |
| `/legenda` | Gera legenda para post nas redes |
| `/pauta-conteudo` | Gera pauta mensal de conteúdo |
| `/proposta` | Gera proposta comercial personalizada para prospect |
| `/resposta-cliente` | Gera resposta para mensagens de clientes |
| `/mapear-rotinas` | Identifica tarefas repetitivas e sugere novas skills |

### O que o `/instalar` coleta

Entrevista guiada conduzida pelo consultor no onboarding. Popula automaticamente os arquivos de memória. Perguntas cobrindo:

- Descrição do negócio e o que entrega
- Produtos/serviços com preços
- Perfil do cliente ideal
- Tom de voz e o que evitar na comunicação
- Identidade visual (cores, fontes, logo)
- Maiores gargalos operacionais hoje
- Metas e prioridades do período
- Estrutura de time

### Diferencial em relação ao MazyOS

| MazyOS | Nossa consultoria |
|---|---|
| Diagnóstico via perguntas gerais | Diagnóstico com lens de growth — gargalo, CAC, conversão |
| Site/link page como extras | Site e link page como parte central da entrega |
| Sem segmentação por setor | Templates por segmento (saúde, educação, turismo…) |
| Cliente usa Claude Code sozinho após compra | Consultor instala, configura e faz handoff estruturado |
| Sem interface própria (por ora) | Web app no roadmap — elimina dependência de Claude Code |

---

## Fases do GTM

### Fase 0 — Construir o produto *(bloqueante para tudo)*

Montar a estrutura base completa do OS: CLAUDE.md, settings.json, arquivos de memória, todas as skills, templates de site e link page, estrutura de outputs.

**Entregáveis:**
- CLAUDE.md base
- settings.json com todas as skills registradas
- Todos os arquivos de memória com estrutura definida
- 13 skills implementadas (listadas acima)
- Template base de site (HTML/CSS)
- Template base de link page (HTML/CSS)
- identidade/design-guide.md
- README de uso para o dono

**Resultado:** consegue fazer a primeira entrega completa para qualquer cliente.

---

### Fase 1 — Frente conhecidos *(inicia após Fase 0)*

Entregas gratuitas para os 5 contatos identificados, em troca de case documentado + depoimento + 2 indicações pagas por cliente.

**Contatos:**
- Vitor — Seed (Educação)
- Elisangela — Jotta Turism (Turismo)
- Pedro — Espaço Vitta (Odonto)
- Sara — Sara Carvalho (Estética)
- Amanda (Medicina)

**Entregáveis desta fase:**
- Script de abordagem (como propor o deal: entrega gratuita em troca de case + indicações)
- Execução das 5 entregas (2–3 em paralelo)
- Documentação dos cases: antes/depois, depoimento, print de resultado
- Coleta estruturada de indicações ao fim de cada entrega

**Meta:** 3+ cases documentados, 5+ leads indicados prontos para proposta paga.

---

### Fase 2 — Identidade + landing page *(em paralelo com Fase 1)*

Construir a presença da consultoria enquanto executa as primeiras entregas.

**Entregáveis:**
- Nome da consultoria (não "agência" — consultoria com entrega de produto)
- Identidade visual mínima: logo, cor primária, tipografia
- Landing page: oferta clara, cases (adicionados conforme ficam prontos), CTA para WhatsApp ou formulário

**Resultado:** quando o tráfego pago ligar, a página já tem prova social.

---

### Fase 3 — Tráfego pago *(só com 2+ cases prontos)*

Conteúdo + anúncios direcionando para a landing page.

**Entregáveis:**
- Estratégia de conteúdo (plataforma, formato, frequência)
- Criativos baseados nos cases reais
- Setup de campanha Meta Ads
- Monitoramento e otimização de CAC

---

### Sequência

```
Fase 0 → produto pronto
         ↓
Fase 1 → cases + indicações (primeiros clientes pagos via referral)
Fase 1 ║ Fase 2 → identidade + landing page em paralelo
         ↓
Fase 3 → tráfego pago com cases e landing page prontos
```

---

## Roadmap futuro — Web App

Após validar o produto via Claude Code, a próxima fase de produto é uma **interface web própria**.

**Por que:** o dono da PME não deve precisar instalar Claude Code, usar terminal ou navegar em GitHub. O acesso precisa ser simples — browser, login, clicar numa skill, receber o output.

**O que é:** web app que chama a API do Claude por baixo, com as mesmas skills e memória do OS, mas com UX simplificada. O consultor ainda faz o onboarding e a configuração inicial, mas o cliente usa o app no dia a dia.

**Impacto no modelo de negócio:** abre receita recorrente (assinatura mensal do app) além do projeto inicial — transforma a consultoria de projeto fechado em produto SaaS com entrega guiada.

**Quem constrói:** Henrique (produto e IA) + sócio (dados e engenharia).

---

## Fora de escopo por ora

- CRM de clientes
- Financeiro e faturamento
- Templates técnicos de automação além das skills base
- Expansão para time do cliente (pós-validação do pacote base)

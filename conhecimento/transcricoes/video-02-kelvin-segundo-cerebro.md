# Video 02 — Kelvin: Segundo Cérebro e Grow OS Skills

**Criador:** Kelvin Clet (Acelera 360)
**Tema:** Construindo um segundo cérebro para alimentar IAs com inteligência do negócio

---

## Conceito de Segundo Cérebro

Prática dos maiores empresários (Gary Tan - CEO YCombinator, Karpathy - fundador OpenAI): condensar toda informação gerada no dia a dia em texto estruturado e alimentar uma IA com isso.

### O que alimenta o cérebro
- Reuniões e transcrições de calls
- Conversas de WhatsApp
- Artigos lidos e vídeos assistidos
- Ideias e anotações
- Decisões tomadas

### Estrutura utilizada
Arquivos Markdown organizados por fonte:
```
/cerebro
  /whatsapp
  /meetings
  /youtube
  /conceitos
  /pessoas
  /empresas
```

### Ferramentas
- **Git/GitHub** como storage inicial (acessível e versionado)
- **Obsidian** serve para humanos lerem — o segundo cérebro é 100% pensado para ser consumido por LLM
- **Zep** para memória temporal com timestamps (decisões rastreadas no tempo)
- Migração para banco vetorizado no futuro

---

## Processo de Ingestão

```
Informação bruta (áudio/reunião/artigo)
    ↓
Ingestão + processamento
    ↓
Extração de insights, temas, decisões, objeções
    ↓
Armazenamento estruturado no cérebro
    ↓
LLM conectada ao cérebro → gera outputs de qualidade
```

### Exemplo prático (WhatsApp de alunos)
Arquivo organizado por:
- Data
- Temas tratados (posicionamento, geração de lead, pipeline, etc.)
- Quem perguntou + texto da pergunta
- Quem respondeu
- Celebrações, objeções, insights do Kelvin

---

## Aplicações no Negócio

- CS Helper para atendimento de alunos (N1/N2)
- Geração de roteiros para YouTube
- Geração de thumbnails por agente com referências
- Geração de pitch decks e go-to-market para clientes

---

## Grow OS Skills (package gratuito no GitHub)

Skills estruturadas para funcionar como funcionários digitais:
- Pesquisa e mapeamento de nicho
- Perfil de cliente (ICP)
- Preparação para reunião
- Criação de landing pages
- Pitch deck
- Go-to-market
- Playbook de vendas
- Auditoria de negócio

### Como usar
Instalar via Claude Code, pedir para mapear nicho, estudar empresa, gerar pitch deck. Usa Nano (Gemini) para geração de PDF.

---

## Princípios

- **Não terceirize a visão** — só o fundador pode criar e nutrir o cérebro da empresa
- **Dog fooding** — use nas suas próprias operações primeiro antes de vender para clientes
- **Nutrição contínua** — o cérebro precisa ser atualizado todo dia, não é setup único
- **Dependência estratégica** — criar dependência de uma empresa séria (Anthropic) é diferente de vendor lock-in problemático

---

## Insights para a Agência

- O cérebro do negócio conectado ao Claude substitui múltiplos funcionários
- Quanto mais contexto, melhor a qualidade das outputs
- Skills customizadas + cérebro = diferencial competitivo difícil de copiar
- Modelo de entrega: implementa o cérebro + treina o cliente a nutrir ele

# OS Padrão — Estrutura de Entrega

Esse documento define o que é construído em todo projeto base. Serve como checklist de produção e referência para onboarding de novos projetos.

---

## O Produto

**Como vender:** "A IA da sua empresa" — não é o ChatGPT genérico. É uma IA que só existe para o negócio do cliente: conhece os produtos, os preços, o público, o tom de voz, os processos. O dono abre e já tem um assistente que entende o negócio como um sócio veterano.

**O que o cliente sai tendo:**
- Uma IA configurada com tudo que importa no negócio dele
- Site funcional que ele consegue atualizar sem depender de ninguém
- Link page (estilo Linktree) para a bio do Instagram — centraliza todos os links da marca
- Um criador de conteúdo que já sabe como a marca fala

---

## Componente 1 — O Cérebro (Knowledge Base)

O cérebro é o arquivo central que transforma uma IA genérica na IA da empresa do cliente.

### O que coletar no onboarding (intake padrão)

```
EMPRESA
- Nome, segmento, cidade/região
- O que faz (produtos e serviços com preços)
- História resumida (quanto tempo existe, como começou)
- Diferenciais declarados pelo dono

PÚBLICO
- Quem compra (perfil, faixa etária, poder aquisitivo)
- Onde encontra esses clientes (Google, Instagram, indicação...)
- Principal dor / motivo de compra
- Objeções mais comuns

COMUNICAÇÃO
- Tom de voz (formal/informal, exemplos de como falam)
- O que NÃO pode falar / evitar
- Cores e identidade visual (se tiver)
- Hashtags ou expressões da marca

OPERAÇÃO
- Horário de funcionamento
- Formas de pagamento aceitas
- Como o cliente entra em contato (WhatsApp, telefone, site)
- Processo de atendimento (como funciona da primeira mensagem até a entrega)

HISTÓRICO
- Posts que mais engajaram (se tiver Instagram ativo)
- Perguntas que mais recebe dos clientes
```

### Estrutura de pastas do projeto

```
/[nome-cliente]
  /cerebro
    empresa.md          ← contexto geral do negócio
    produtos.md         ← lista completa com preços e descrições
    publico.md          ← ICP e dores mapeadas
    tom-de-voz.md       ← como a marca fala
    faq.md              ← perguntas frequentes e respostas padrão
  /site
    index.html
    link-page.html
  /conteudo
    /carrosseis         ← carrosseis gerados
    /posts              ← legendas e posts
  /calls
    [data]-onboarding.md
```

---

## Componente 2 — Site

Site funcional, responsivo, simples de manter. Não é portfólio — é conversão.

### Estrutura padrão de toda página

- Hero com proposta de valor clara e CTA para WhatsApp
- Seção de serviços/produtos com preços (quando possível)
- Prova social (avaliações, número de clientes atendidos)
- CTA final (WhatsApp ou formulário)
- Rodapé com endereço, horário, redes

### O que o cliente consegue fazer sozinho depois

- Atualizar texto de qualquer seção com um prompt no Claude
- Adicionar novo produto ou serviço
- Trocar foto e descrição

---

## Componente 3 — Link Page (Bio do Instagram)

Página leve, mobile-first, hospedada junto ao site. Centraliza todos os links da marca num lugar só — substitui o Linktree sem custo de assinatura.

### Estrutura padrão

- Logo ou nome da marca no topo
- Foto ou imagem de capa (opcional)
- Botões para: WhatsApp, Site, Instagram, cardápio/catálogo (se tiver)
- Frase curta de posicionamento embaixo do nome

### O que o cliente consegue fazer sozinho depois

- Pedir para adicionar ou remover link com um prompt no Claude
- Atualizar o número de WhatsApp ou link de promoção

---

## Componente 4 — Criador de Conteúdo

Skills de conteúdo treinadas com o contexto do negócio.

### O que o cliente consegue fazer com um prompt

- Criar carrossel sobre qualquer produto ou tema
- Gerar legenda com CTA para WhatsApp
- Adaptar um conteúdo para o formato de post único
- Gerar pauta de conteúdo para o mês

### Padrão de carrossel entregue

- Slide 1: gancho (dor ou curiosidade)
- Slides 2–5: conteúdo/argumento
- Slide final: CTA com contato

---

## Componente 5 — OS do Dono

O que o dono consegue resolver com a IA da empresa instalada.

### Exemplos de uso imediato (mostrar na entrega)

| Situação | O que o dono faz |
|----------|-----------------|
| Cliente mandou mensagem difícil | Cola a mensagem + "como respondo isso?" |
| Precisa de orçamento rápido | "Monta orçamento para [produto] para [perfil de cliente]" |
| Vai postar no Instagram | "Cria post sobre [tema] para hoje" |
| Quer saber se o negócio está crescendo | Cola os números do mês + "analisa isso para mim" |
| Funcionário com dúvida de processo | "Como a gente faz [processo]?" |

### O que diferencia de usar o ChatGPT direto

ChatGPT genérico não sabe que o cliente se chama João, que o produto custa R$89, que a empresa não trabalha com parcelamento, que o tom é informal mas não usa gíria, e que o diferencial é atendimento em 2 horas. A IA da empresa sabe tudo isso sem precisar explicar toda vez.

---

## Fluxo de Entrega

```
Dia 1-2    → Onboarding (coleta de intake + calls gravadas)
Dia 3-5    → Construção do cérebro + estrutura de pastas
Dia 5-7    → Site + link page
Dia 10-14  → Skills de conteúdo + primeiros carrosseis gerados
Dia 14     → Entrega + onboarding do dono (como usar tudo)
```

---

## Diagnóstico de Expansão (pós-entrega)

Depois que o pacote base está funcionando, revisitar com o cliente:

**Front office (vendas / aquisição)**
- Tem script de vendas? Consegue treinar o time?
- Tem funil de aquisição ou depende de indicação?
- Tem CS estruturado ou pós-venda inexistente?

**Back office (operação)**
- Tem controle financeiro ou tudo na planilha do dono?
- Tem processo de cobrança ou inadimplência alta?
- Documentação interna existe ou está na cabeça do dono?

Cada item identificado como gargalo é uma solução nova — pode virar projeto adicional ou, para clientes maiores, o argumento para retainer.

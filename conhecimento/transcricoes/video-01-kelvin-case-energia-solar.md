# Video 01 — Kelvin: Case Empresa de Energia Solar

**Criador:** Kelvin Clet (Acelera 360)
**Tema:** Estruturando Claude como sistema operacional de uma empresa de energia solar

---

## Contexto do Case

Cliente de energia solar (B2B e B2C), faturamento de R$6M/ano (~R$500k/mês). Domina vendas e marketing digital, mas o operacional não dá conta de entregar o que vende. Chegou ao Kelvin querendo "implementar IA no negócio para ir pro próximo nível".

---

## Framework: Core Business vs Backoffice

### Core Business (Front Office)
Critério: ligado à receita, impacta aquisição/conversão/retenção de clientes.
- Marketing
- Vendas e pipeline
- Customer Success
- Precificação e oferta

### Backoffice
Critério: infraestrutura operacional, não impacta diretamente na venda.
- Financeiro
- Jurídico
- RH
- Contábil
- Processos internos
- Tecnologia

**Relação:** Core Business depende do Backoffice para escalar. Backoffice depende do Core Business para existir.

---

## Diagnóstico do Cliente (Energia Solar)

### Core Business
| Área | Status | Detalhe |
|------|--------|---------|
| Marketing | ✅ 7/10 | Terceirizado, orgânico forte (YouTube), básico bem feito |
| Atração/Captação | ✅ Bom | Geração de demanda orgânica funcionando |
| Conversão | ✅ Bom | CRM no Kommo, bem configurado |
| Proposta técnica | 🔴 Gargalo | Time não consegue montar proposta técnica e vender ROI |
| Customer Success | 🔴 Gargalo | Praticamente inexistente — nenhum pós-venda, nenhuma indicação sendo solicitada |

### Backoffice
| Área | Status | Detalhe |
|------|--------|---------|
| Financeiro | 🔴 Gargalo | Inadimplência altíssima, time não dá conta do controle |
| Jurídico | Terceirizado | Sem ação necessária |
| Gestão | 🔴 Gargalo | Não está sendo feita |
| RH | 🔴 Gargalo | Inexistente |
| Tecnologia | 🔴 Gargalo | Não tem, e precisa |
| Administrativo | 🔴 Gargalo | Controle de documentação, organização interna, suporte ao time — nada estruturado |

**Diagnóstico geral:** Empresa cresceu muito pelo talento técnico do fundador, chegou no teto. Se vender mais, quebra. Precisa de produtividade operacional antes de abrir o funil de vendas novamente.

---

## Solução Proposta

### Abordagem
1. Entrevistar stakeholders e pessoas-chave para absorver os processos
2. Criar skills específicas para cada área da operação
3. Distribuir licenças Claude para 6 colaboradores iniciais
4. Conectar todas as instâncias a um cérebro central (GitHub)
5. Treinar o time com pessoa exclusiva dedicada ao onboarding

### Stack Técnica
- **Claude Teams** (~R$490/usuário/mês)
- **GitHub** como knowledge base inicial (migração para banco vetorizado no futuro)
- **Skills com guardrails** para proteger informações sensíveis
- Custo inicial: ~R$6.000/mês em licenças (rollout gradativo)

### Plano
- **90 dias** de implementação gradativa
- Começar com 6 colaboradores na licença 5x
- Skills cobrindo: projetos técnicos, atendimento ao cliente, conciliação bancária, cobrança de inadimplentes, customer success

---

## Modelo de Negócio / Precificação

- R$30k a R$100k por projeto, dependendo do porte e resultado gerado
- Posicionamento: consultor estratégico de resultado, não vendedor de ferramenta
- Não forçou troca de CRM (manteve Kommo por ser adequado ao cliente)

---

## Insights Chave

- Empresário sabe usar IA, mas só ele usa — time não adota
- Solução não é desenvolver software próprio, é estruturar o que existe com IA
- CS inexistente = dinheiro vazando: indicações e recompra não estão sendo capturadas
- Gargalo operacional impede escalar vendas — resolver backoffice primeiro
- "Marketing não resolve o problema — vamos dar produtividade"

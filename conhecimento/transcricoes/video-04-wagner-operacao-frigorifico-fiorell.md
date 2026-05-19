# Video 04 — Wagner: Operação Dia a Dia com Cliente Frigorífico (Fiorell)

**Criador:** Wagner (Xmaz IA)
**Tema:** Como opera um cliente real (frigorífico) no dia a dia usando Claude Code

---

## Perfil do Cliente (Fiorell)

- **Segmento:** Frigorífico — pertences para feijoada e carnes salgadas (Santo André/SP)
- **Foco:** Venda para restaurantes, atacado e B2C
- **Antes da contratação:** Sem site, sem Instagram, sem Google Meu Negócio, sem presença digital nenhuma
- **Resultado:** Primeira venda online em 5 dias

---

## Organização do Projeto

### Estrutura de Pastas
```
/fiorell
  /produtos          ← fotos e specs dos produtos
  /financeiro        ← DRE, fluxo de caixa, estoque, contas a pagar
  /ads               ← criativos e campanhas Google Ads
  /calls             ← transcrições de reuniões
  /site              ← código do site
```

**Convenção:** Cada projeto tem uma cor diferente no VS Code para não confundir quando há múltiplos projetos abertos.

---

## Entregáveis Construídos

| Entregável | Detalhe |
|-----------|---------|
| Site principal | Produtos, formulário, WhatsApp |
| LPs por produto | Carne seca, costela suína, pernil — cada anúncio vai para LP específica |
| Dashboard (painel) | Visão geral, financeiro, clientes, produtos com margem, estoque, Google Ads |
| Feijoadômetro | Calculadora interativa: seleciona nº de pessoas + miúdos → calcula quantidade → cai no WhatsApp |
| Blog SEO | Posts como "Feijoada para 50 pessoas" linkando para o Feijoadômetro |
| Google Meu Negócio | Setup completo, produtos adicionados, posts, respostas de avaliação |
| Carrosséis Instagram | Gerados automaticamente via skill de carrossel |
| Personagem da marca | Criado com IA para posts |

---

## Workflow de Atualização (mostrado ao vivo)

1. Cliente manda fotos novas dos produtos (dianteiro em cubos, lombo, orelha, pé cortado, rabo)
2. Wagner adiciona na pasta `/produtos`
3. Claude atualiza site, página de ads e gera carrossel automaticamente
4. Wagner faz ajustes pontuais no carrossel via chat
5. Agenda post para meio-dia do dia seguinte via **Routines** (mesmo com PC desligado)

---

## Skill de Avaliação Google

Processo:
1. Abre Google Meu Negócio → "Não respondido"
2. Copia todas as avaliações
3. Abre novo chat: `responder essas avaliações do Google. Use a skill avaliação.`
4. Claude gera resposta personalizada por avaliação
5. Cola cada resposta no Google

**Tempo total:** Minutos. Sem abrir Canva, sem escrever texto manualmente.

---

## Routines do Claude Code

Funcionalidade para agendar tarefas futuras. Exemplo:
> "Utilizar routines para amanhã meio-dia postar no Facebook e Instagram esse carrossel"

Executa mesmo com o PC desligado.

---

## Práticas de Contexto

- Toda call é gravada e transcrita
- Transcrição é adicionada à pasta `calls/` do cliente
- Alimenta o contexto da IA com tudo que foi discutido
- Resultado: Claude sabe o histórico de decisões, ideias e pendências do cliente

---

## Modelo de Negócio

- Perfil mais acessível/grassroots (diferentes de Kelvin)
- Começa com clientes menores, boca a boca, trabalhos gratuitos para amigos
- Entrega site + presença digital + automação de conteúdo + Google Ads + dashboard
- Estratégia baseada em Google Ads como canal principal de aquisição

---

## Insights para a Agência

- Dashboard personalizado para o dono = diferencial de retenção (cliente vê valor todo dia)
- LP específica por produto/anúncio converte melhor que jogar pro site principal
- Feijoadômetro (calculadora interativa) = geração de lead qualificado com contexto
- Skill especializada por tarefa (avaliação, carrossel) acelera muito o dia a dia
- Google Meu Negócio bem mantido é parte essencial da estratégia Google Ads
- Rotinas agendadas = entrega de valor assíncrona (cliente vê resultado sem o prestador estar online)

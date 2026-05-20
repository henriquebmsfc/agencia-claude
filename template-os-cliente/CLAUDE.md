# [NOME DA EMPRESA] — IA do Negócio

Esse arquivo é o sistema operacional do negócio. Ele define como a IA lê o contexto, aprende com o uso e evolui conforme a operação cresce.

Quando o `/instalar` rodar, ele preenche esse arquivo com as informações reais do negócio.

---

## Contexto do negócio

No início de toda conversa, ler os seguintes arquivos (quando existirem e estiverem preenchidos):

1. `_memoria/empresa.md` — o que o negócio faz, produtos, preços, diferenciais
2. `_memoria/preferencias.md` — voz, tom, o que evitar na comunicação
3. `_memoria/estrategia.md` — foco atual, prioridades, metas
4. `_memoria/diagnostico.md` — gargalos identificados e oportunidades mapeadas

Usar essas informações como base para qualquer resposta ou decisão. Ao sugerir abordagens ou formatos, considerar o foco atual do `estrategia.md`.

Para qualquer tarefa visual (site, link page, carrossel), consultar `identidade/design-guide.md`.

**Não listar o que foi lido nem confirmar a leitura. Usar o contexto naturalmente.**

Nunca inventar produtos, preços ou informações não listadas em `empresa.md`. Se uma pergunta exige algo que não está nos arquivos, dizer ao dono que o arquivo precisa ser atualizado.

---

## Fluxo de trabalho

Antes de executar qualquer tarefa, verificar se existe skill relevante em `.claude/commands/`. Se encontrar, seguir as instruções da skill. Se não, executar normalmente.

Ao concluir uma tarefa que não tinha skill mas parece repetível, perguntar:

> "Isso pode virar uma skill pra próxima vez. Quer que eu crie?"

Não perguntar para tarefas pontuais ou perguntas simples — só quando o padrão de repetição for claro.

---

## Aprender com correções

Quando o dono corrigir algo, melhorar uma resposta ou dar uma instrução que parece permanente (frases como "na verdade é assim", "não faça mais isso", "prefiro assim", "sempre que...", "evita...", "da próxima vez..."), perguntar:

> "Quer que eu salve isso pra não precisar repetir?"

Se sim, identificar onde salvar:

- **Sobre o negócio** (produtos, clientes, serviços, mercado) → `_memoria/empresa.md`
- **Sobre preferências e estilo** (tom, formato, o que evitar) → `_memoria/preferencias.md`
- **Sobre prioridades e foco** (projetos, metas, prazos) → `_memoria/estrategia.md`
- **Sobre gargalos e oportunidades** → `_memoria/diagnostico.md`
- **Regra de comportamento geral** → próprio `CLAUDE.md`

Mostrar a linha que será adicionada antes de salvar. Não reformatar o arquivo inteiro — só adicionar ou editar o trecho relevante.

Não perguntar se a correção for óbvia de contexto imediato. Só quando a informação tiver valor duradouro.

---

## Manter contexto atualizado

Ao terminar uma tarefa que mudou algo relevante (novo produto, mudança de foco, processo novo, cliente novo), perguntar:

> "Isso mudou algo no negócio. Quer que eu atualize a memória?"

Se sim, identificar o que atualizar seguindo o mesmo roteamento acima. Mostrar o que vai mudar antes de salvar.

**Quando NÃO perguntar:**
- Tarefas pontuais sem impacto no contexto (escrever uma legenda avulsa, responder uma mensagem)
- Perguntas simples ou conversas sem ação
- Mudanças já salvas pelo bloco "Aprender com correções"

Use `/atualizar` para uma varredura completa quando houver dúvida.

---

## Skills disponíveis

| Skill | O que faz |
|---|---|
| `/instalar` | Configura o sistema pela primeira vez com as informações do negócio |
| `/abrir` | Inicia a sessão com um resumo do contexto atual |
| `/salvar` | Salva e versiona tudo no GitHub |
| `/atualizar` | Atualiza os arquivos de memória quando o negócio muda |
| `/diagnostico` | Mapeia gargalos operacionais e oportunidades de crescimento |
| `/gerar-site` | Cria ou atualiza o site de conversão |
| `/gerar-link-page` | Cria ou atualiza a link page da bio do Instagram |
| `/carrossel` | Gera carrossel para Instagram com voz e produtos do negócio |
| `/legenda` | Gera legenda para post |
| `/pauta-conteudo` | Gera pauta de conteúdo para o mês |
| `/proposta` | Gera proposta comercial para um cliente específico |
| `/resposta-cliente` | Gera resposta para mensagem de cliente |
| `/mapear-rotinas` | Identifica tarefas repetitivas e sugere novas skills |

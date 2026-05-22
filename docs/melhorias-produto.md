# Melhorias Futuras — OS do Negócio

Backlog de decisões adiadas e comportamentos que precisam de definição. Não são bugs — são escolhas que precisam de mais contexto antes de implementar.

Itens marcados com ✅ estão concluídos — apagar na próxima limpeza do arquivo.

---

## ✅ 1. Pré-checagem: comportamento no caminho "complementar"

**Onde:** `/instalar` — seção "Pré-checagem / Arquivos de contexto"

**O problema:**
Quando os arquivos de memória já têm conteúdo real (de um setup anterior ou parcial), o `/instalar` pergunta:

> "Já tem contexto preenchido aqui. Quer recomeçar do zero ou complementar o que falta?"

O comportamento de **recomeçar do zero** está implícito: apaga os conteúdos e refaz tudo.

O comportamento de **complementar** não está definido. O sistema não sabe:
- Quais perguntas pular (as que já têm resposta preenchida)?
- Quais campos estão "em falta" (como detectar placeholder vs conteúdo real)?
- Se deve mostrar o que já existe antes de perguntar, ou perguntar e só sobrescrever o que for respondido diferente?

**Opções possíveis:**
- **A) Leitura prévia + perguntas seletivas:** ler os arquivos, identificar campos vazios ou com placeholder, fazer só as perguntas correspondentes. Mais inteligente, mais complexo de implementar.
- **B) Fazer tudo de novo e mesclar:** rodar o fluxo normal, mas ao salvar comparar com o que já existe e só sobrescrever campos que vieram preenchidos na entrevista. Mais simples, mas pode sobrescrever coisas boas.
- **C) Mostrar o que existe e perguntar por seção:** apresentar o conteúdo atual de cada arquivo e perguntar "isso ainda está certo?" antes de cada bloco. Mais trabalhoso para o dono, mas mais transparente.

**Recomendação a avaliar:** Opção A para o caminho feliz (maioria dos casos é um setup parcial com campos óbvios em branco). Opção C como fallback quando os arquivos têm conteúdo real mas desatualizado.

**Impacto:** médio — só afeta clientes que rodaram o `/instalar` antes ou que editaram os arquivos manualmente.

---

## ✅ 2. Fase 5 removida — pasta renomeada pelo consultor

**Contexto:** A fase de renomear a pasta foi removida do `/instalar` porque o consultor faz o setup inicial antes de entregar ao cliente. Quando o dono rodar `/instalar`, a pasta já terá o nome correto.

**Ponto de atenção futuro:** Se o produto evoluir para um modelo self-service (cliente clona e configura sozinho, sem o consultor), essa fase precisa voltar. Guardar a lógica comentada ou numa branch separada.

---

## ✅ 3. Pasta de imagens no template

Criar pasta `imagens/` no template para o cliente salvar fotos usadas em carrossel, site e link page. As skills visuais devem referenciar essa pasta ao gerar conteúdo.

---

## 4. Vícios de linguagem de IA

Adicionar instrução no CLAUDE.md e/ou `preferencias.md` proibindo vícios comuns: "mergulhar", "navegar", "no mundo de hoje", "é fundamental", "vale ressaltar", "em um mundo cada vez mais", listas excessivas, aberturas com "Claro!".

**Pesquisar:** se existe skill ou plugin que detecta e corrige esse padrão automaticamente antes de entregar qualquer output.

---

## 5. /proposta — gerar PDF formatado

Atualmente gera `.md`. Precisa gerar PDF na identidade visual da empresa (cores, tipografia do design-guide). Avaliar: HTML→PDF via Playwright, ou HTML intermediário que o cliente imprime como PDF.

---

## 6. Skills visuais — integração com frontend-design skill

Verificar se `/gerar-site`, `/gerar-link-page`, `/carrossel`, `/post` e `/story` estão chamando `frontend-design:frontend-design` antes de gerar HTML. Se não, adicionar a chamada.

**Pesquisar também:** skills ou plugins que elevam qualidade visual para designs mais ousados.

---

## 7. /gerar-site — referências visuais e imagens

- Buscar referências de imagens reais (Unsplash, Pexels) — priorizar imagens sobre placeholders genéricos
- Buscar referências de design no Dribbble antes de gerar (pesquisar como integrar ou simular na skill)
- Instrução explícita para priorizar seções com foto no layout

---

## 8. /carrossel — formato, geração e entrega em JPG

- Fluxo atual: gera `.md` → gera HTML → precisa entregar JPG. Automatizar HTML→JPG via Playwright
- Formato fixo: **1350x1080px**
- Não enumerar slides no output visual ("Slide 1", "Slide 2" etc.)
- Integrar `frontend-design` skill obrigatoriamente
- Buscar referência de imagens em banco (Unsplash, Pexels) quando relevante para o tema

---

## 9. /pauta-conteudo — revisão geral

Revisar para sair mais acionável: cada post com briefing suficiente para executar, equilíbrio 40/30/20/10 respeitado, formatos /post e /story sugeridos adequadamente.

---

## 10. /post e /story — formato visual e entrega em JPG

- Integrar `frontend-design` skill obrigatoriamente
- Dimensões fixas: post **1080x1080**, story **1080x1920**
- Automatizar entrega em JPG via Playwright (HTML→screenshot→JPG)
- Buscar referência de imagens em banco quando relevante

---

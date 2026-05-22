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

## ✅ 4. Vícios de linguagem de IA

Adicionada lista de expressões proibidas no `CLAUDE.md` e no template `_memoria/preferencias.md`. Não existe skill/plugin disponível para detecção automática — a instrução no CLAUDE.md já carrega em toda sessão.

---

## ✅ 5. /proposta — gerar PDF formatado

Skill reescrita: gera HTML estilizado com identidade visual do design-guide, depois converte para PDF via Playwright (`page.pdf()`). Saída em `outputs/propostas/proposta-[cliente]-[data].pdf`.

---

## ✅ 6. Skills visuais — integração com frontend-design skill

Adicionada referência condicional ao `frontend-design:frontend-design` em `/gerar-site` e `/gerar-link-page` + diretrizes de qualidade visual inline (funciona mesmo sem o plugin). `/carrossel`, `/post` e `/story` receberão a integração quando forem convertidas para HTML (melhorias #8 e #10).

---

## ✅ 7. /gerar-site — referências visuais e imagens

Adicionada seção "Imagens" na skill: prioridade 1 = pasta `imagens/`, prioridade 2 = Unsplash via URL direta, proibido placeholder de cor sólida. Dribbble não é integrável automaticamente (sem API pública) — instrução de qualidade visual cobre isso via padrão de design no "Antes de começar".

---

## ✅ 8. /carrossel — formato, geração e entrega em JPG

Skill reescrita em 3 fases: roteiro → HTML (1350×1080px, sem enumeração, frontend-design, Unsplash) → JPG via Playwright. Cada slide exportado como `slide_NN.jpg` em subpasta.

---

## ✅ 9. /pauta-conteudo — revisão geral

Skill reescrita: cada item agora tem Tema + Formato + Objetivo + Ângulo + Referência visual + Skill para executar. Meta do mês no topo. Equilíbrio 40/30/20/10 mantido.

---

## ✅ 10. /post e /story — formato visual e entrega em JPG

Skills reescritas em 3 fases: roteiro → HTML (post 1080×1080, story 1080×1920, frontend-design, Unsplash) → JPG via Playwright. Dimensões fixas, frontend-design integrado, Unsplash para imagens.

---

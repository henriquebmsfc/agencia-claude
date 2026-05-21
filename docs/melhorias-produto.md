# Melhorias Futuras — OS do Negócio

Backlog de decisões adiadas e comportamentos que precisam de definição. Não são bugs — são escolhas que precisam de mais contexto antes de implementar.

---

## 1. Pré-checagem: comportamento no caminho "complementar"

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

## 2. Fase 5 removida — pasta renomeada pelo consultor

**Contexto:** A fase de renomear a pasta foi removida do `/instalar` porque o consultor faz o setup inicial antes de entregar ao cliente. Quando o dono rodar `/instalar`, a pasta já terá o nome correto.

**Ponto de atenção futuro:** Se o produto evoluir para um modelo self-service (cliente clona e configura sozinho, sem o consultor), essa fase precisa voltar. Guardar a lógica comentada ou numa branch separada.

---

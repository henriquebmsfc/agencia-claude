# /salvar — Versionar Alterações

Sincroniza as alterações feitas nos arquivos de memória com o repositório Git.

## Instruções

Execute os seguintes passos em ordem:

1. **Verificar status:** 
   - Rode `git status` para ver o que mudou
   - Se não houver nada para commitar, informar: "Nada para salvar — tudo já está atualizado no GitHub." e encerrar

2. **Apresentar resumo:** 
   - Mostre ao dono um resumo das alterações em linguagem simples
   - Quais arquivos foram modificados e o que mudou (não técnico)

3. **Coletar descrição:** 
   - Pergunte: "Tem alguma descrição específica para esse save, ou pode salvar com uma mensagem automática?"

4. **Gerar mensagem de commit:** 
   - Se o dono der uma descrição, use-a como mensagem
   - Se não, gere uma mensagem descritiva em português baseada nos arquivos modificados

5. **Executar commit e push:**
   ```
   git add -A
   git commit -m "[mensagem]"
   git push
   ```

6. **Confirmar sucesso:** 
   - "Salvo! Tudo está no GitHub."

## Se falhar

Se `git push` falhar porque não há remote configurado:

"Para salvar no GitHub, você precisa criar um repositório em github.com e conectar. Quer que eu te explique como fazer isso?"

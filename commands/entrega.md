---
description: Confere a entrega contra o ESCOPO.md com o agente auditor-entrega e prepara a nota de entrega
argument-hint: "[cliente ou projeto]"
---

Para: $ARGUMENTS
1. Localize `ESCOPO.md`. Sem escopo, pare e ofereça criar um com `${CLAUDE_PLUGIN_ROOT}/modelos/cliente/ESCOPO.md`.
2. Rode o agente `auditor-entrega` (contexto limpo; não verifique você mesmo o que implementou).
3. `NÃO VERIFICADO`: mostre as lacunas e a próxima ação de cada uma; não marque como entregue.
4. `VERIFICADO`: preencha `entrega.md` do cliente e escreva um rascunho de mensagem ao cliente para o usuário revisar. Não envie nada.

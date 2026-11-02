---
name: diario-e-decisoes
description: Diário curto do dia e registro de decisões (data, decisão, motivo, resultado esperado, quando revisar). A revisão semanal lê as decisões vencidas. Use com /diario no fim do dia ou ao tomar uma decisão importante.
---

# Diário e decisões

## Diário (2 min)
Acrescente ao arquivo do dia (`dia/AAAA-MM-DD.md`): saiu, travou, energia 1 a 5, amanhã começo por. Se a pessoa só escrever uma frase, está ótimo.

## Decisão
Quando a pessoa disser "decidi", "vou fazer", "parei de":
1. Registre em `decisoes.md` (formato `${CLAUDE_PLUGIN_ROOT}/modelos/voce/decisoes.md`): número `P-NNN`, data, decisão, motivo, resultado esperado, revisar em (padrão: 30 dias).
2. **Motivo nunca fica vazio:** se a pessoa não disse, escreva o motivo provável pelo contexto com "(provável, confirme)". O mesmo para o resultado esperado.
3. **Revisar em:** sempre uma data concreta (padrão: hoje + 30 dias).
4. Na revisão, preencha "Como foi".

## Regras
- Formato da decisão inspirado em registros de decisão (contexto, alternativas, consequência), ver CREDITOS.md.
Tudo na pasta pessoal (`${CLAUDE_PLUGIN_ROOT}/rules/privacidade-pessoal.md`). Nunca na pasta de cliente.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

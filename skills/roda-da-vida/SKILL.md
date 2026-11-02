---
name: roda-da-vida
description: Roda da vida em 5 minutos - nota de 0 a 10 para cada uma das 8 áreas, comparação com a última roda e escolha de no máximo 2 áreas de foco para o trimestre. Use com /roda, no começo do trimestre, depois do /comecar ou quando a pessoa sentir que a vida está desequilibrada.
---

# Roda da vida

## Passo a passo
1. Leia `perfil.md` e a última roda em `roda/` (se existirem).
2. Peça uma nota de 0 a 10 para cada área, todas de uma vez, em formato de lista (é mais rápido):
   Trabalho e negócio · Dinheiro · Saúde e energia · Estudo e carreira · Relacionamentos · Casa e rotina · Propósito · Criação
   Nota é sensação, não prova. "Não se aplica" vale.
3. Mostre a roda como barras de texto:
   `Dinheiro      ███░░░░░░░ 3`
4. Se houver roda anterior, mostre a diferença por área (↑ ↓ =).
5. Pergunte: em qual área **1 ponto a mais** mudaria mais a sua vida? Escolha no máximo **2** áreas de foco. Não mencione uma 3ª área como alternativa ou sugestão.
6. Para cada área de foco, uma ação de até 30 minutos para esta semana e a skill que ajuda.

## Gravar
`roda/AAAA-MM-DD.md` na pasta pessoal: notas, áreas de foco, ações. Atualize "Áreas ativas" no `perfil.md` se mudaram (mostre antes).

## Regras
- Nota baixa não é fracasso; não comente "isso é preocupante". Pergunte o que pesa.
- Nota 0 a 2 em saúde com relato de sofrimento: siga `${CLAUDE_PLUGIN_ROOT}/rules/limites.md`.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

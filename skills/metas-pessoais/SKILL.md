---
name: metas-pessoais
description: Metas do trimestre para até 3 áreas da vida (as áreas de foco da roda da vida), cada uma com indicador, valor de hoje, alvo e data de revisão. Use no começo do trimestre, depois da /roda ou quando a pessoa disser que quer mudar algo e não sabe por onde começar.
---

# Metas do trimestre

1. Pergunte, uma área por vez: o que mudaria sua vida/negócio nos próximos 90 dias?
2. Para cada área, **uma** meta com **indicador mensurável** (número, sim/não, frequência), numa tabela: área · meta · indicador · hoje · alvo · revisão.
3. **Alvo sempre numérico:** se a pessoa não deu números, proponha um alvo provisório concreto (ex.: "3 caminhadas/semana", "guardar R$ 300/mês" ou "10% do que entra") marcado "provisório, ajuste". Nunca deixe o alvo como `SEM DADO`.
4. Valor de hoje: registre; sem ele, a primeira tarefa da semana é medir.
5. Defina a data de revisão (a revisão semanal olha as metas toda sexta).

Formato de apoio: `${CLAUDE_PLUGIN_ROOT}/modelos/voce/metas-do-trimestre.md`. Grave em `metas.md` na pasta pessoal. Use as áreas de foco da última `roda-da-vida`; no máximo 3 metas no trimestre.

Regras: meta de saúde é hábito (ex.: caminhar 3x por semana), nunca peso ou exame como alvo sem acompanhamento profissional. Meta de dinheiro é comportamento ou valor guardado, nunca rentabilidade de investimento. Siga `${CLAUDE_PLUGIN_ROOT}/rules/limites.md`.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

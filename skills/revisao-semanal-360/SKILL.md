---
name: revisao-semanal-360
description: Revisão da semana cruzando todas as áreas ativas do perfil - 1 vitória e 1 trava por área, energia, decisões vencidas, metas e 3 compromissos para a próxima semana em áreas diferentes. Use com /semana (no dia de revisão escolhido no perfil, de preferência sexta) ou no último dia do mês.
---

# Revisão semanal 360

## Insumos (leia da pasta pessoal, se existirem)
`perfil.md` (áreas ativas), `dia/` da semana, `decisoes.md` (revisões vencidas), `metas.md`, última `roda/`, `saude/` (check-ins de energia).

## Roteiro (com o agente `coach-360`, uma pergunta por vez)
1. **Panorama:** mostre o que já leu dos arquivos em até 5 linhas (dias registrados, energia média, decisões vencidas). Sem arquivos, pergunte direto.
2. **Por área ativa:** uma vitória (mesmo pequena) e uma trava. Até 3 áreas; não percorra as 8.
3. **Energia:** de 1 a 5; o que drenou e o que recarregou.
4. **Decisões vencidas:** como foram? Preencha "Como foi" em `decisoes.md`.
5. **Metas:** andou, parou ou mudou?
6. **Próxima semana:** exatamente **3 compromissos**, cada um de uma área diferente, e **1 coisa para parar** (proponha uma se a pessoa não disse). Não acrescente tarefas além dos 3 (nada de "vale também..."); lembrete de fim de mês entra como um dos 3 ou fica de fora.

## Mensal (último dia do mês)
Acrescente: `/caixa` ou `/orcamento`, e pergunte se vale atualizar a `/roda`.

## Saída
`semana/AAAA-Www.md` na pasta pessoal, até 15 linhas:
```
# Semana AAAA-Www
Vitórias: ...
Travas: ...
Energia: n/5 · drenou ... · recarregou ...
Decisões revistas: ...
Compromissos: 1) [área] ... 2) [área] ... 3) [área] ...
Parar: ...
```

## Regras
Sem sermão. Semana ruim: registre e escolha compromissos menores. Esgotamento sério: `${CLAUDE_PLUGIN_ROOT}/rules/limites.md`.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

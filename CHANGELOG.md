# Mudanças

## 0.2.0 · Ofício da Codetrade (grátis)

### Ajustes após a avaliação com/sem plugin
- `rede-de-seguranca` também reconhece pedido de "onde investir" e reforça o limite (sem ativo, sem corretora, consultor CVM).
- Crise e emergência apontam para `pausa-e-estresse` (segurança primeiro); dica de sessão com atalhos para `mapa-do-oficio`, `memoria-local`, `tutor-socratico`.
- Formatos mais firmes: post completo em 5 blocos sem número derivado (`marca-pessoal`); plano por mês com até 3 itens e exercício no trabalho (`plano-de-estudo`); primeira resposta curta e com pergunta (`tutor-socratico`); registro da semana antes de tudo e sem explicação clínica (`energia-e-tempo`); "Depois" com todo o resto (`rotina-do-dia`); exatamente 3 compromissos (`revisao-semanal-360`); sem 3ª área (`roda-da-vida`); motivo e data sempre preenchidos (`diario-e-decisoes`); alvo numérico provisório (`metas-pessoais`); dia da trilha em 3 linhas (`trilha-7-dias`); roteador sem nomes de produto (`mapa-do-oficio`).
- Evals: regex `nao-parecer` aceita "não parecer jurídico" (antes exigia "não é"); critério `pedaco-pequeno` do tutor aceita resposta só com pergunta.

- Evals refeitos: 1 critério por arquivo (nota parcial), regex onde dá para verificar, indicador `skill-acionada` (só informativo), `runs: 1`, `timeout_seconds: 180`, `max_turns: 8`. Gerados por `scripts/gerar-evals.py`.
- Hook `lembrete-do-dia` passa a injetar (só para o modelo) a dica de roteamento para as skills do Ofício; roda em startup, clear e compact.
- Skills ganham "Modo direto": com a informação já dada, entregam sem refazer perguntas.
- Novo nome e slug: `oficio` (antes `oficio-inteiro`). Comandos agora são `/oficio:...`.
- Vida 360: núcleo + 8 áreas. 26 skills (14 do núcleo anterior + 12 novas), 7 agentes, 17 comandos, 4 hooks.
- Novas skills: `perfil-de-vida`, `mapa-do-oficio` (substitui `mapa-do-kit`), `roda-da-vida`, `revisao-semanal-360` (substitui `revisao-semanal`), `memoria-local`, `trilha-7-dias`, `caixa-do-negocio` (substitui `saude-financeira-solo`), `orcamento-pessoal`, `pausa-e-estresse`, `sono-e-descanso`, `fluencia-em-ia`, `tutor-socratico`, `conversa-dificil`, `casa-em-ordem`, `tom-de-voz`.
- Agentes: `coach-360` (substitui `coach-semanal`) e `editor` (novo).
- Comandos novos: `/comecar`, `/semana` (substitui `/revisao-semanal`), `/roda`, `/meus-dados`, `/orcamento`, `/energia`, `/estudar`, `/conversa`, `/post`.
- Hooks novos: `lembrete-do-dia`, `rede-de-seguranca`, `proteger-dados-pessoais`.
- Pasta pessoal: `$HOME/oficio/` (variável `OFICIO_PASTA`). Cópia automática de `$HOME/oficio-inteiro-voce/`.
- Regras de limites ampliadas (SAMU 192, CVV 188, 190, sem diagnóstico, sem recomendação de investimento).
- Evals: 1 caso por skill + 3 casos de limite em `evals/`.

## 0.1.0
- Núcleo grátis do Ofício Inteiro: pilar Negócio e pilar Você.

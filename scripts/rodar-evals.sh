#!/usr/bin/env bash
# Comparação com x sem plugin (ablação): 1 rodada por caso, mesmos flags nos dois braços.
# Depois monta dist/oficio.zip só com as áreas que ganharam.
# Precisa do Claude Code com login (/login).
# Variáveis opcionais: JUIZ (padrão haiku; use sonnet para juiz mais rigoroso), TETO (US$, padrão 12), MODELO.
# Argumentos extras vão para o claude plugin eval (ex.: -j 3, --case "casa-em-ordem").
set -euo pipefail
RAIZ="$(cd "$(dirname "$0")/.." && pwd)"
SAIDA="$RAIZ/evals/results/ultimo"
rm -rf "$SAIDA"
claude plugin eval "$RAIZ" --ablation with-without --runs 1 --trust-plugin --no-publish \
  --threshold 0 --judge-model "${JUIZ:-haiku}" --max-cost-usd "${TETO:-12}" \
  --output-dir "$SAIDA" ${MODELO:+--model "$MODELO"} "$@" || true
python3 "$RAIZ/scripts/montar-build.py" "$SAIDA/aggregate-result.json"

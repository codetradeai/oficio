---
name: saude-financeira-solo
description: Painel mensal do caixa de quem trabalha sozinho - faturamento, custos, imposto estimado, pró-labore, reserva, dependência de um cliente e valor-hora real. Use com /caixa no fim do mês ou com o agente guardiao-do-caixa.
---

# Saúde financeira do negócio solo

## Coleta
Preencha `${CLAUDE_PLUGIN_ROOT}/modelos/voce/caixa-mensal.md`. Valor aproximado vale; marque como aproximado.

## Cálculos
- Sobra = faturamento − custos − imposto estimado − pró-labore.
- Meses de reserva = reserva acumulada ÷ custo mensal (negócio + pró-labore).
- Dependência = faturamento do maior cliente ÷ faturamento total.
- Valor-hora real = (faturamento − custos − imposto) ÷ horas trabalhadas.

## Sinais de atenção
- Maior cliente acima de 40%.
- Reserva abaixo de 3 meses.
- Pró-labore irregular por 2 meses seguidos.
- Valor-hora real caindo 3 meses seguidos.

## Regras
Imposto é estimativa: confirme com o contador (`${CLAUDE_PLUGIN_ROOT}/rules/limites.md`). Nunca peça senha de banco. Grave em `caixa-AAAA-MM.md` na pasta pessoal.

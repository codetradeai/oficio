---
name: caixa-do-negocio
description: Fechamento mensal do caixa de quem trabalha por conta ou tem negócio pequeno - faturamento, custos, imposto estimado, pró-labore, sobra, meses de reserva, dependência do maior cliente e valor-hora real, com até 3 alertas e 1 ação. Use com /caixa no fim do mês ou com o agente guardiao-do-caixa. Não é contabilidade.
---

# Caixa do negócio

## Coleta (valor aproximado vale; marque "aprox.")
Faturamento do mês · faturamento do maior cliente · custos do negócio · imposto pago ou estimado (DAS, ISS) · pró-labore retirado · reserva acumulada do negócio · horas trabalhadas no mês.
Formato de apoio: `${CLAUDE_PLUGIN_ROOT}/modelos/voce/caixa-mensal.md` (se não achar, use a lista acima).

## Cálculos (mostre a conta)
- Sobra = faturamento − custos − imposto − pró-labore
- Meses de reserva = reserva ÷ (custos + pró-labore)
- Dependência = maior cliente ÷ faturamento
- Valor-hora real = (faturamento − custos − imposto) ÷ horas

## Alertas (no máximo 3, com o número)
- Maior cliente acima de 40% do faturamento.
- Reserva abaixo de 3 meses.
- Sobra negativa ou pró-labore irregular 2 meses seguidos.
- Valor-hora real abaixo do que a pessoa disse que quer ganhar.

## Saída
Tabela com os números → até 3 alertas → **1 ação** para o próximo mês (quem, o quê, quando).
Grave em `dinheiro/caixa-AAAA-MM.md` na pasta pessoal, com permissão.

## Limites
Imposto é estimativa para conversar com o contador, nunca cálculo oficial. Não recomende investimento nem produto financeiro (`${CLAUDE_PLUGIN_ROOT}/rules/limites.md`). Faltou número: `SEM DADO`, não invente.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

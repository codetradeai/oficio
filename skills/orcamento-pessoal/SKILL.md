---
name: orcamento-pessoal
description: Orçamento do mês da casa em 15 minutos - entradas, gastos, dívidas e sobra ou falta, com 1 ajuste concreto. Use quando a pessoa disser que o dinheiro não fecha, não sabe para onde vai o salário, quer organizar as finanças pessoais, ou perguntar onde investir ou o que fazer com dinheiro parado (nesse caso, sem recomendar ativo: reserva, dívidas e perfil primeiro). Comando /orcamento.
---

# Orçamento pessoal

## 1. Entradas
Salário/pró-labore líquido, renda extra, benefícios. Valor do mês, aproximado vale.

## 2. Saídas (pergunte por bloco, não item por item)
| Bloco | Exemplos |
|---|---|
| Casa | aluguel/prestação, condomínio, luz, água, gás, internet |
| Comida | mercado, feira, delivery, restaurante |
| Transporte | combustível, app, ônibus, manutenção |
| Saúde | plano, farmácia |
| Dívidas | parcelas, cartão (valor pago no mês), empréstimo |
| Filhos/família | escola, ajuda a parentes |
| Assinaturas | streaming, apps, academia |
| Lazer e outros | o que sobrou |

## 3. Resultado
- Mostre tabela: bloco, valor, % da renda.
- Sobra (ou falta) = entradas − saídas.
- Destaque o maior bloco variável e as assinaturas.

## 4. Um ajuste
Proponha **um** ajuste com valor estimado (ex.: "cortar 2 deliveries por semana ≈ R$ 160/mês"). A pessoa escolhe. Se há dívida com juros altos (cartão rotativo, cheque especial), diga que priorizar sair dela costuma valer mais do que qualquer economia pequena, e sugira o plano de dívidas do Pro (em breve) ou começar listando todas as dívidas com juros.

## Gravar
`dinheiro/orcamento-AAAA-MM.md` na pasta pessoal, com permissão. Mês seguinte: compare com o anterior.

## Perguntou onde investir?
Não cite ação, fundo, cripto, título, código de ativo (ticker), banco ou corretora, nem como exemplo ou "ilustração". Explique só conceitos: dívida cara primeiro, reserva de emergência, prazo, perfil de risco, diversificação. Indique um profissional certificado e independente (ex.: consultor registrado na CVM).

## Limites
Não recomende investimento, banco, corretora, cripto ou produto financeiro; explique conceitos se pedirem (reserva de emergência, juros compostos). `${CLAUDE_PLUGIN_ROOT}/rules/limites.md`.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

---
name: sono-e-descanso
description: Diário de sono de 7 dias e ajustes de rotina possíveis (horário, luz, telas, cafeína, ritual de desligar), com sinais de quando procurar médico. Use quando a pessoa disser que dorme mal, acorda cansada, tem insônia ocasional ou quer organizar o descanso. Não diagnostica distúrbio do sono.
---

# Sono e descanso

## 1. Entender (3 perguntas)
- Que horas costuma deitar e levantar (dias úteis e fim de semana)?
- O que acontece na última hora antes de deitar?
- Café, energético ou álcool depois das 16 h?

## 2. Diário de 7 dias
Crie `saude/sono.md` (com permissão) com uma linha por dia:
`AAAA-MM-DD · deitei 23:30 · dormi ~00:15 · acordei 06:30 · acordei de noite 1x · energia ao acordar 2/5 · obs.: tela até tarde`
Peça para registrar de manhã, em 30 segundos.

## 3. Ajustes (escolha 1 ou 2 por semana, não todos)
- Mesmo horário de acordar todos os dias, inclusive fim de semana (variação de até 1 h).
- Luz do dia nos primeiros 30 min depois de acordar.
- Cafeína só até o começo da tarde.
- Ritual de desligar de 20 min: luz baixa, sem tela de trabalho, anotar pendências no papel para amanhã.
- Quarto escuro, silencioso e mais fresco.
- Sem sono depois de ~20 min deitado: levante, faça algo calmo com luz baixa, volte quando der sono.

## 4. Revisão depois de 7 dias
Média de horas, energia ao acordar e o que mudou. Mantenha o que funcionou e teste o próximo ajuste.

## Procure médico se
Ronco alto com pausas na respiração · sonolência forte durante o dia (cochila dirigindo, em reunião) · insônia por mais de 3 meses · pernas inquietas à noite · uso de remédio para dormir sem orientação.

## Limites
Não indique remédio, suplemento ou dose (nem melatonina). Não diagnostique. `${CLAUDE_PLUGIN_ROOT}/rules/limites.md`.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

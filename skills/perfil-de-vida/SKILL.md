---
name: perfil-de-vida
description: Onboarding do Ofício - entrevista curta (até 12 perguntas, uma por vez) sobre momento de vida, áreas que importam agora, horários e limites; grava perfil.md na pasta pessoal e liga só as áreas escolhidas. Use com /comecar, na primeira vez que a pessoa usa o plugin ou quando a vida mudou (emprego, mudança, filho).
---

# Perfil de vida

Objetivo: em 10 a 15 minutos, saber o suficiente para que todas as outras skills falem com **esta** pessoa, não com um usuário genérico.

## Entrevista (uma pergunta por vez, espere a resposta)
1. Como você quer ser chamado(a)?
2. Em uma frase: como está sua vida hoje? (vale "corrida", "recomeçando", "estável")
3. Trabalho: CLT, autônomo(a), dono(a) de negócio, estudante, entre trabalhos?
4. Das 8 áreas, quais pedem atenção **nos próximos 90 dias**? Mostre a lista e peça no máximo 3:
   Trabalho e negócio · Dinheiro · Saúde e energia · Estudo e carreira · Relacionamentos · Casa e rotina · Propósito · Criação e marketing
5. Para cada área escolhida: o que seria "deu certo" daqui a 90 dias? (uma frase)
6. Horários: que horas começa e termina seu dia? Qual dia da semana é melhor para revisar a semana?
7. Limites: tem algo que eu não devo sugerir? (ex.: horário sagrado, assunto delicado)
8. Tom: prefere direto e curto ou mais explicado?
Pare antes de 12 perguntas se já tiver o essencial. Nunca peça CPF, endereço, renda exata ou diagnóstico.

## O que gravar
Pasta pessoal (regra `${CLAUDE_PLUGIN_ROOT}/rules/privacidade-pessoal.md`). Pergunte antes de criar.
`perfil.md`:
```
# Perfil · atualizado em AAAA-MM-DD
Nome: ...
Momento: ...
Trabalho: ...
Áreas ativas (90 dias): ... (com "deu certo se...")
Horário: início ... fim ... · Revisão semanal: (dia)
Não sugerir: ...
Tom: direto | explicado
```
Mostre o arquivo antes de gravar e diga o caminho completo depois.

## Fechamento
1. Resuma o perfil em 3 linhas.
2. Indique a `trilha-7-dias` e qual comando usar amanhã de manhã (`/meu-dia`).
3. Se a pessoa já tinha dados do Ofício Inteiro, diga que foram copiados para a pasta nova.

## Sem acesso a arquivos (ex.: chat do Grok Bot)
Mostre o `perfil.md` pronto e peça para a pessoa guardar ou colar no início das próximas conversas.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

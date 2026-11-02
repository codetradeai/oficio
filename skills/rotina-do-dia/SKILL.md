---
name: rotina-do-dia
description: Planejamento do dia em 10 minutos para a vida inteira - aceita a lista do jeito que vier (bagunçada, em áudio transcrito, misturando trabalho e casa), fecha 3 prioridades de áreas diferentes, encaixa blocos de foco na agenda real e manda o resto para depois. Use com /meu-dia de manhã ou quando a pessoa disser que o dia não rende.
---

# Rotina do dia

## Manhã (até 10 min)
1. Leia `perfil.md` (áreas ativas, horário, limites) e o `dia/` de ontem (o que ficou para hoje), se existirem.
2. Pergunte: o que tem hora marcada hoje? (se houver acesso à agenda, leia; senão, pergunte)
3. Peça tudo que está na cabeça, do jeito que vier. Arrume você: junte repetidos, separe por área, transforme frases vagas em ações ("ver dentista" → "ligar para marcar dentista").
4. Feche **3 prioridades**, de preferência de áreas diferentes (ex.: 1 trabalho, 1 casa ou dinheiro, 1 você ou pessoas). Mais que 3 não é prioridade.
5. Encaixe 1 ou 2 **blocos de foco** (25 a 90 min) nos buracos da agenda para as duas primeiras.
6. **Só entram na agenda** as 3 prioridades e o que já tem hora marcada. **Todo o resto** vai para a lista "Depois", item por item (pode ter "se sobrar tempo"), sem culpa. Não encaixe os outros itens na agenda.

## Saída
```
Hoje (dia da semana, AAAA-MM-DD)
1. [área] ...  → bloco 9h–10h30
2. [área] ...  → bloco 14h–15h
3. [área] ...
Depois: ...
```

## Fim do dia (2 min)
Saiu? Travou em quê? Energia 1 a 5? Amanhã começo por...? Use `/diario`.

## Gravar
`dia/AAAA-MM-DD.md` na pasta pessoal (formato de apoio: `${CLAUDE_PLUGIN_ROOT}/modelos/voce/dia.md`). Primeira vez: pergunte antes de criar a pasta.

## Regras
- Respeite o horário de fim do dia e os limites do perfil.
- Mais de 5 obrigatórios no dia: aponte e sugira o que adiar ou delegar.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

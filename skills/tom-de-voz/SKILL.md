---
name: tom-de-voz
description: Monta o perfil do jeito de escrever da pessoa a partir de 3 a 10 textos reais dela (posts, mensagens, e-mails) - ritmo, palavras, como abre e fecha, o que nunca faz - e grava para que posts, mensagens e artigos saiam com a voz dela, sem cara de texto de IA. Use quando a pessoa quiser escrever "do meu jeito", antes de /post, ou disser que o texto da IA parece genérico.
---

# Tom de voz

Adaptado da skill `brand-voice` do projeto de Affaan Mustafa (MIT, ver CREDITOS.md), reescrito para pt-BR e para quem escreve post, WhatsApp e e-mail.

## 1. Coletar
Peça de 3 a 10 textos **escritos pela própria pessoa** (posts, mensagens para clientes, e-mails, legendas). Prefira os recentes e os que "deram certo". Não use texto de outra pessoa como modelo de voz.
Se houver dois jeitos (ex.: formal com cliente, solto no Instagram), faça dois perfis.

## 2. O que observar
- Tamanho das frases e dos parágrafos.
- Como abre (pergunta? fato? história?) e como fecha (chamada? frase de efeito? nada?).
- Palavras e expressões que se repetem; gírias; regionalismos.
- Emoji: usa? quais? quantos?
- Números e exemplos concretos: frequentes ou raros?
- Tom: animado, seco, acolhedor, técnico, bem-humorado.
- O que a pessoa **nunca** faz.

## 3. Perfil (até 15 linhas)
```
# Tom de voz · AAAA-MM-DD
Ritmo: ...
Abre com: ...  ·  Fecha com: ...
Palavras dela: ...
Emoji: ...
Faz: ...
Nunca: ...
Exemplo de frase no tom: ...
```
Mostre e pergunte "Isso soa como você?". Ajuste até a pessoa concordar.

## 4. Proibidos em qualquer perfil
Frases de efeito vazias, "neste artigo vamos", "no mundo de hoje", ganchos de curiosidade falsa, perguntas isca, listas de 10 itens sem conteúdo, excesso de travessões e de emoji que a pessoa não usa.

## Gravar e usar
`criacao/tom-de-voz.md` na pasta pessoal. `marca-pessoal`, `conversa-dificil` e o agente `editor` leem esse arquivo quando existir.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

---
name: diagnostico-pme
description: Diagnóstico de um pequeno negócio para automação com IA, WhatsApp e CRM - entrevista sem induzir resposta, mapa do processo atual e lista de automações por esforço e impacto. Use no primeiro contato com um cliente ou com /diagnostico.
---

# Diagnóstico de pequeno negócio

## Passo 1: preparar (10 min)
- Rode o agente `descobridor` se ainda não houver dossiê.
- Liste 3 lacunas que a conversa precisa fechar.

## Passo 2: entrevista (perguntas sobre o passado, não sobre o futuro)
1. Me conte a última vez que [a dor] aconteceu. O que você fez?
2. Quanto tempo isso tomou? Quem fez?
3. O que você já tentou para resolver? Por que parou?
4. Quanto isso custa por mês (tempo, cliente perdido, dinheiro)?
5. Se resolver, o que muda na sua semana?
Evite "você usaria...?" e "você pagaria...?": respostas sobre o futuro enganam.

## Passo 3: mapa do processo
Do primeiro contato do cliente final até o pagamento: canal → quem atende → onde registra → o que se perde. Marque cada passo como manual, planilha ou sistema.

## Passo 4: automações (esforço x impacto)
| # | Automação | Dor que resolve | Impacto (1-5) | Esforço (1-5) | Dado pessoal envolvido |
|---|---|---|---|---|---|
Comece pelo maior impacto com menor esforço. Toda linha com dado pessoal passa pela skill `lgpd-pme`.

## Saída
`diagnostico.md` na pasta do cliente: problema em uma frase, mapa, tabela, 3 recomendações e o que ficou `SEM DADO`. Siga `${CLAUDE_PLUGIN_ROOT}/rules/pt-br-pme.md`.

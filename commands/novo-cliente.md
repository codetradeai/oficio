---
description: Cria a pasta padrão de um cliente novo (ficha, escopo, decisões, entrega) a partir dos modelos do Ofício
argument-hint: "[nome do negócio]"
---

Crie a pasta do cliente "$ARGUMENTS" no diretório atual (pergunte antes se o diretório não parecer uma pasta de clientes).
Copie para ela os modelos de `${CLAUDE_PLUGIN_ROOT}/modelos/cliente/` (`ficha.md`, `ESCOPO.md`, `decisoes.md`, `entrega.md`) e preencha a ficha com o que já se sabe, marcando o resto como `SEM DADO`.
Não grave nada pessoal aqui (`${CLAUDE_PLUGIN_ROOT}/rules/privacidade-pessoal.md`). Termine dizendo a próxima etapa: `/diagnostico`.

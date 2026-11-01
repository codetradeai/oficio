---
name: mapa-do-kit
description: Mapa do Ofício Inteiro. Dado um pedido, diz se é do pilar Negócio ou Você, em que etapa a pessoa está e qual skill, agente ou comando usar a seguir. Use quando não souber por onde começar ou quando o pedido misturar cliente e vida pessoal.
---

# Ciclo do Ofício Inteiro

## Pilar Negócio (para clientes)
`diagnóstico → proposta → desenho → construção → QA → entrega → acompanhamento`

| Etapa | Use |
|---|---|
| Cliente novo | `/novo-cliente` (cria a pasta com `${CLAUDE_PLUGIN_ROOT}/modelos/cliente/`) |
| Diagnóstico | `/diagnostico` → skill `diagnostico-pme` + agente `descobridor` |
| Antes de publicar | `/deploy-check` → skill `deploy-checklist` |
| Teste | `/qa` → skill `qa-crm` + agente `revisor-lgpd` |
| Dados pessoais | skill `lgpd-pme` |
| Entrega | `/entrega` → agente `auditor-entrega` |
| Proposta, contrato, WhatsApp, CRM pronto | versão Pro (em breve) |

## Pilar Você (para quem toca o negócio)
`planejar o dia → foco → registrar → revisar a semana → ajustar metas → estudar → olhar o caixa`

| Momento | Use |
|---|---|
| Começo do dia | `/meu-dia` → `rotina-do-dia` |
| Hora de produzir | `foco-profundo` |
| Fim do dia / decisão importante | `/diario` → `diario-e-decisoes` |
| Sexta-feira | `/revisao-semanal` → agente `coach-semanal` |
| Começo do trimestre | `metas-pessoais` |
| Aprender algo | `plano-de-estudo` + agente `mentor-estudos` |
| Fim do mês | `/caixa` → `saude-financeira-solo` + agente `guardiao-do-caixa` |
| Agenda lotada | `energia-e-tempo` |
| Divulgar o trabalho | `marca-pessoal` |

## Como responder
1. Diga o pilar e a etapa em uma linha.
2. Indique a próxima skill ou comando e por quê.
3. Se o pedido mistura os dois pilares, resolva primeiro o que tem prazo com cliente.

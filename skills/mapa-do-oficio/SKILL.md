---
name: mapa-do-oficio
description: Roteador do Ofício da Codetrade. Use quando a pessoa perguntar "por onde eu começo?", "o que eu faço?", "o que o Ofício faz?", desabafar misturando assuntos (dívida e falta de tempo, trabalho e família) ou não souber qual skill usar. Responde com a área da vida, UMA skill ou comando e um próximo passo de 10 minutos.
---

# Mapa do Ofício

## Como responder
1. Diga a área (ou as duas áreas, se o pedido mistura) em uma linha.
2. Indique **uma** skill ou comando para começar e por quê (meia linha).
3. Dê um próximo passo que caiba em 10 minutos.
   Você é roteador: **não** entregue o plano completo da área e **não** cite banco, empréstimo, cartão, app, programa de renegociação ou serviço pelo nome. A skill indicada cuida do resto.
4. Se houver sinal de emergência ou crise, pare e siga `${CLAUDE_PLUGIN_ROOT}/rules/limites.md` (SAMU 192, CVV 188, 190) antes de qualquer roteamento.
5. Se uma skill indicada não existir nesta instalação, diga que está em revisão e ofereça a mais próxima.
6. Se o pedido for de algo da versão Pro, diga que está "em breve" e ofereça a skill grátis mais próxima.

## Núcleo
| Situação | Use |
|---|---|
| Primeira vez / vida mudou | `/comecar` → `perfil-de-vida` |
| Primeira semana | `trilha-7-dias` |
| Começo do dia | `/meu-dia` → `rotina-do-dia` |
| Fim de semana | `/semana` → `revisao-semanal-360` + agente `coach-360` |
| Qual área está pior? | `/roda` → `roda-da-vida` |
| Onde ficam meus dados / apagar | `/meus-dados` → `memoria-local` |

## Áreas
| Área | Grátis | Pro (em breve) |
|---|---|---|
| Trabalho e negócio | `/novo-cliente`, `/diagnostico` (`diagnostico-pme`), `lgpd-pme`, `/deploy-check`, `/qa` (`qa-crm`), `/entrega` | proposta, preço, funil de clientes, contratos |
| Dinheiro | `/caixa` (`caixa-do-negocio`), `/orcamento` (`orcamento-pessoal`) | extrato, dívidas, reserva, imposto |
| Saúde e energia | `/energia`, `energia-e-tempo`, `pausa-e-estresse`, `sono-e-descanso` | movimento, alimentação, preparar consulta |
| Estudo e carreira | `plano-de-estudo`, `fluencia-em-ia`, `/estudar` (`tutor-socratico`) | currículo, entrevista, transição |
| Relacionamentos | `/conversa` (`conversa-dificil`) | rede de pessoas, combinados da casa |
| Casa e rotina | `rotina-do-dia`, `foco-profundo`, `casa-em-ordem` | documentos e prazos, viagem, reforma |
| Propósito | `metas-pessoais`, `/diario` (`diario-e-decisoes`) | valores, hábitos, leitura ativa |
| Criação e marketing | `/post` (`marca-pessoal`), `tom-de-voz`, agente `editor` | conteúdo da semana, vídeo, lançamento |

## Exemplos
- "Tô devendo no cartão e sem tempo pra nada" → Dinheiro + Casa e rotina. Comece por `/orcamento` (10 min para ver o tamanho do buraco); depois `rotina-do-dia`.
- "Quero mudar de carreira" → Estudo e carreira. `plano-de-estudo` hoje; transição de carreira completa é Pro (em breve).

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

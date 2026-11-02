# Ofício da Codetrade · grátis

> Plugin **vida 360** em português para Claude Code. Versão 0.2.0.

A vida não cabe numa lista de tarefas. O Ofício cuida do dia, da semana e do trimestre olhando **8 áreas**: trabalho, dinheiro, saúde e energia, estudo, relacionamentos, casa, propósito e criação. Tudo fica em **arquivos no seu computador**.

## Instalar no Claude Code

```
/plugin marketplace add codetradeai/oficio
/plugin install oficio@oficio
```
Depois digite `/oficio:comecar`.

### Sem GitHub: pelo .zip
1. Baixe `oficio.zip` em https://codetradeai.github.io/oficio/ e descompacte. Vai aparecer a pasta `oficio/`.
2. Abra o terminal na pasta onde ela está e rode `claude`.
3. No Claude Code: `/plugin marketplace add ./oficio` e depois `/plugin install oficio@oficio`.
4. Reinicie o Claude Code e digite `/oficio:comecar`.

Só para testar, sem instalar: `claude --plugin-dir ./oficio`.

### Grok Bot
Cada skill funciona sozinha. Abra um `SKILL.md` (ex.: `skills/rotina-do-dia/SKILL.md`), copie e cole no chat do Grok Bot pedindo: "Salve isto como uma skill. Mostre antes de salvar." Ou envie o .zip e peça para instalar as que você escolher. Sem acesso a arquivos, o Grok Bot mostra o texto pronto para você guardar.

## O ritmo
| Quando | Comando |
|---|---|
| Primeira vez | `/comecar` (perfil + trilha de 7 dias) |
| De manhã | `/meu-dia` |
| À noite | `/diario` |
| Dia de revisão | `/semana` |
| Começo do trimestre | `/roda` |
| Fim do mês | `/caixa` (negócio) ou `/orcamento` (casa) |

No Claude Code, os comandos aparecem com prefixo: `/oficio:meu-dia`. Toda skill também pode ser chamada direto, ex.: `/oficio:sono-e-descanso`.

## O que vem dentro (26 skills, 7 agentes, 17 comandos, 4 hooks)

### Núcleo
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `perfil-de-vida` | Entrevista curta e perfil local; liga só as áreas que importam |
| skill | `mapa-do-oficio` | Diz a área, a skill e o próximo passo para qualquer pedido |
| skill | `roda-da-vida` | Notas 0 a 10 nas 8 áreas e até 2 áreas de foco |
| skill | `revisao-semanal-360` | Semana cruzando as áreas, 3 compromissos em áreas diferentes |
| skill | `memoria-local` | Onde e como seus dados ficam; exportar e apagar |
| skill | `trilha-7-dias` | Primeira semana guiada, 10 min por dia |
| agente | `coach-360` | Conduz dia, semana e trimestre |
| comando | `/comecar` `/meu-dia` `/semana` `/roda` `/meus-dados` | Ritmo e dados |

### Trabalho e negócio
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `diagnostico-pme` | Entrevista, mapa do processo, automações por esforço x impacto |
| skill | `lgpd-pme` | Dados, base legal, aviso de privacidade |
| skill | `deploy-checklist` | Conferência antes de publicar um app |
| skill | `qa-crm` | Roteiro de teste com relatório de falhas |
| agente | `descobridor` `auditor-entrega` `revisor-lgpd` | Pesquisa antes da conversa, conferência de entrega, dado exposto |
| comando | `/novo-cliente` `/diagnostico` `/qa` `/deploy-check` `/entrega` | Ciclo do cliente |

### Dinheiro
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `caixa-do-negocio` | Sobra, reserva, dependência de cliente, valor-hora |
| skill | `orcamento-pessoal` | Orçamento do mês da casa e 1 ajuste |
| agente | `guardiao-do-caixa` | Olha os números sem julgamento |
| comando | `/caixa` `/orcamento` | Fechamento do mês |

### Saúde e energia
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `energia-e-tempo` | Para onde vai seu tempo e sua energia |
| skill | `pausa-e-estresse` | Pausa de 5 min e quando pedir ajuda |
| skill | `sono-e-descanso` | Diário de sono de 7 dias e ajustes de rotina |
| comando | `/energia` | Check-in de 1 minuto |

### Estudo e carreira
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `plano-de-estudo` | Cursos gratuitos + prática |
| skill | `fluencia-em-ia` | 4 hábitos para usar IA bem |
| skill | `tutor-socratico` | Ensina perguntando, com cartões de revisão |
| agente | `mentor-estudos` | Acompanha o plano |
| comando | `/estudar` | Sessão de 25 min |

### Relacionamentos
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `conversa-dificil` | Fato, sentimento, necessidade, pedido; ensaio |
| comando | `/conversa` | Prepara a conversa |

### Casa e rotina
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `rotina-do-dia` | 3 prioridades e blocos de foco, da lista do jeito que vier |
| skill | `foco-profundo` | Protocolo de bloco de foco |
| skill | `casa-em-ordem` | Contas, vencimentos e manutenção |

### Propósito
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `metas-pessoais` | Metas do trimestre com indicador |
| skill | `diario-e-decisoes` | Diário curto e decisões com data de revisão |
| comando | `/diario` | Fecha o dia |

### Criação e marketing
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `marca-pessoal` | Post a partir do trabalho real |
| skill | `tom-de-voz` | Seu jeito de escrever, para tudo sair com a sua voz |
| agente | `editor` | Revisa texto e corta cara de IA |
| comando | `/post` | Um post do dia |

### Hooks (automáticos)
| Hook | O que faz |
|---|---|
| `lembrete-do-dia` | Ao abrir o Claude Code, mostra até 3 linhas: ritual do dia e prioridades. Copia `$HOME/oficio-inteiro-voce/` para `$HOME/oficio/` na primeira vez |
| `rede-de-seguranca` | Se a mensagem tem sinal de crise ou emergência, garante CVV 188, SAMU 192 ou 190 na resposta |
| `proteger-dados-pessoais` | Pergunta antes de gravar CPF, cartão, saúde ou dinheiro fora da pasta pessoal |
| `bloquear-segredos` | Impede gravar chave secreta em arquivo de front-end |

Também: `rules/` (linguagem, LGPD, privacidade, limites) e `modelos/`.

## Privacidade
- Seus dados ficam em `$HOME/oficio/` (ou na pasta da variável `OFICIO_PASTA`). Sem servidor, sem coleta, sem medição.
- `/meus-dados` lista, exporta ou apaga (apagar pede confirmação).
- Nada é enviado, publicado ou apagado sem sua aprovação.
- O que você escreve passa pela IA que você usa (Claude, Grok etc.), conforme os termos dela.

## Limites
O Ofício organiza e prepara. Não diagnostica, não indica remédio, não recomenda investimento e não substitui médico, psicólogo, advogado ou contador. Emergência: **SAMU 192**. Crise: **CVV 188**. Violência: **190**.

## Pro (em breve)
Proposta e preço, funil de clientes, extrato e dívidas, consulta médica preparada, currículo e entrevista, rede de pessoas, documentos e prazos, conteúdo da semana e lançamento. Avisos: contato@codetrade.me

## Testes
- `python3 -m unittest discover -s tests` (estrutura e hooks)
- `claude plugin validate .`
- `bash scripts/rodar-evals.sh -j 3` (comparação com x sem plugin, 1 caso por skill, precisa de login no Claude Code; `JUIZ=sonnet` para juiz mais rigoroso)

## Créditos e licença
MIT (ver `LICENSE`). Algumas skills foram adaptadas de projetos MIT de terceiros: ver `CREDITOS.md`.
Feito pela Codetrade / C&T.AI, Campo Grande/MS · https://codetrade.me · contato@codetrade.me

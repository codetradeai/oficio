# Ofício Inteiro · núcleo grátis

> Nome provisório. Versão 0.1.0, rascunho não publicado.

Kit de IA em português para quem toca pequeno negócio e faz tudo sozinho.
Dois pilares: **Negócio** (cliente do diagnóstico à entrega) e **Você** (dia, semana, estudo, caixa).

## Instalar no Claude Code (1 passo)

Dentro do Claude Code:

```
/plugin marketplace add codetradeai/oficio-inteiro
/plugin install oficio-inteiro@oficio-inteiro
```


### Sem GitHub: pelo .zip
1. Descompacte `oficio-inteiro-nucleo.zip`. Vai aparecer a pasta `oficio-inteiro/`.
2. Abra o terminal na pasta onde ela está e rode `claude`.
3. No Claude Code: `/plugin marketplace add ./oficio-inteiro` e depois `/plugin install oficio-inteiro@oficio-inteiro`.
4. Reinicie o Claude Code e digite `/` para ver os comandos.

Para só testar sem instalar: `claude --plugin-dir ./oficio-inteiro`.

### Grok Bot
Abra o `SKILL.md` de uma skill (ex.: `skills/rotina-do-dia/SKILL.md`), copie tudo e cole no chat do Grok Bot com o pedido: "Salve isto como uma skill. Mostre antes de salvar." Repita para cada skill que quiser. Ou envie o .zip no chat e peça para instalar as skills que você escolher.

## Comece por aqui
- Segunda de manhã: `/meu-dia`
- Todo fim de dia: `/diario`
- Sexta: `/revisao-semanal`
- Fim do mês: `/caixa`
- Cliente novo: `/novo-cliente` → `/diagnostico`

No Claude Code, os comandos de plugin também aparecem com prefixo, ex.: `/oficio-inteiro:meu-dia`.

## O que vem dentro

### Negócio
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `mapa-do-kit` | Diz o pilar, a etapa e o próximo passo |
| skill | `diagnostico-pme` | Entrevista, mapa do processo, automações por esforço x impacto |
| skill | `deploy-checklist` | Conferência antes de publicar um app |
| skill | `qa-crm` | Roteiro de teste com relatório de falhas |
| skill | `lgpd-pme` | Dados, base legal, aviso de privacidade |
| agente | `descobridor` | Pesquisa pública antes da conversa |
| agente | `auditor-entrega` | Confere a entrega contra o escopo |
| agente | `revisor-lgpd` | Procura dado pessoal exposto |
| comando | `/novo-cliente` `/diagnostico` `/deploy-check` `/qa` `/entrega` | Atalhos do ciclo |
| hook | `bloquear-segredos` | Impede gravar chave secreta em arquivo de front-end |

### Você
| Tipo | Nome | Para quê |
|---|---|---|
| skill | `rotina-do-dia` | 3 prioridades e blocos de foco em 10 min |
| skill | `foco-profundo` | Protocolo de bloco de foco |
| skill | `metas-pessoais` | Metas do trimestre com indicador |
| skill | `revisao-semanal` | Roteiro da semana e do mês |
| skill | `plano-de-estudo` | Cursos gratuitos + prática |
| skill | `marca-pessoal` | Conteúdo a partir do trabalho real |
| skill | `energia-e-tempo` | Para onde vai seu tempo |
| skill | `saude-financeira-solo` | Caixa, reserva, valor-hora |
| skill | `diario-e-decisoes` | Diário curto e decisões com data de revisão |
| agente | `coach-semanal` | Conduz a revisão da semana |
| agente | `mentor-estudos` | Acompanha o plano de estudo |
| agente | `guardiao-do-caixa` | Olha o caixa sem julgamento |
| comando | `/meu-dia` `/revisao-semanal` `/diario` `/caixa` | Atalhos do dia a dia |

Também: `rules/` (linguagem, LGPD, privacidade, limites) e `modelos/` (cliente e pessoal).

## Privacidade
- Tudo roda no seu computador. O kit não tem servidor, não coleta e não mede nada.
- Diário, metas e caixa ficam em `$HOME/oficio-inteiro-voce/` (ou na pasta de `KIT_PASTA_PESSOAL`), separados das pastas de cliente.
- Nada é enviado, publicado ou apagado sem sua aprovação.
- O texto que você escreve passa pela IA que você usa (Claude, Grok etc.), conforme os termos dela.

## Limites
Não substitui terapeuta, médico, advogado ou contador.

## Testes
`python3 -m unittest discover -s tests`

## Licença e contato
MIT (ver `LICENSE`). Feito pela Codetrade / C&T.AI, Campo Grande/MS · https://codetrade.me · contato@codetrade.me

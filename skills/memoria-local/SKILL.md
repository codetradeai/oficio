---
name: memoria-local
description: Use quando a pessoa pedir "guarde que...", "anote que...", "lembre que...", "onde ficam meus dados?" ou "apague tudo", ou antes de gravar qualquer coisa pessoal. Regras de onde o Ofício guarda a memória (pasta local $HOME/oficio ou OFICIO_PASTA, uma subpasta por área, saude/ para saúde) e de como listar, exportar ou apagar com confirmação.
---

# Memória local

Princípio: o que o Ofício lembra são **arquivos de texto no seu computador**, que você lê, edita e apaga quando quiser. Sem servidor, sem nuvem, sem telemetria.

## Onde
- Pasta pessoal: `$HOME/oficio/` ou o caminho da variável `OFICIO_PASTA`.
- Migração: se existir `$HOME/oficio-inteiro-voce/` e a pasta nova ainda não, o hook `lembrete-do-dia` copia tudo (a antiga fica intacta).

| Assunto | Arquivo |
|---|---|
| Perfil | `perfil.md` |
| Dia | `dia/AAAA-MM-DD.md` |
| Semana | `semana/AAAA-Www.md` |
| Decisões | `decisoes.md` |
| Metas | `metas.md` |
| Roda da vida | `roda/AAAA-MM-DD.md` |
| Dinheiro | `dinheiro/` |
| Saúde e energia | `saude/` |
| Estudo | `estudo/` |
| Pessoas | `pessoas/` |
| Casa | `casa/` |
| Criação | `criacao/` (ex.: `tom-de-voz.md`) |
| Clientes | na pasta do projeto do cliente, **nunca** aqui |

## Ao responder
Diga sempre o caminho exato do arquivo (ex.: "`$HOME/oficio/saude/consultas.md`") e que fica só no computador.

## Como gravar
1. Primeira vez: pergunte antes de criar a pasta.
2. Escolha o arquivo pela tabela. Nome com data `AAAA-MM-DD`.
3. **Acrescente** no fim; não reescreva histórico. Para corrigir, acrescente "Correção (data): ...".
4. Depois de gravar, diga o caminho em uma linha.
5. Saúde, dinheiro e documentos: só dentro da pasta pessoal; nunca em pasta de cliente ou repositório git.

## /meus-dados
- **Listar:** mostre as pastas, quantidade de arquivos e data do último registro.
- **Exportar:** gere `oficio-export-AAAA-MM-DD.zip` na pasta que a pessoa indicar (padrão: a própria pasta pessoal).
- **Apagar:** mostre exatamente o que será apagado e peça para a pessoa digitar `APAGAR` antes. Nunca apague sem isso. Sugira exportar antes.

## Sem acesso a arquivos (Grok Bot no chat)
Mostre o texto que seria gravado e diga em que arquivo a pessoa pode guardar.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

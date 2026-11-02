---
name: deploy-checklist
description: Checklist antes de colocar no ar um app de pequeno negócio feito com Lovable, Supabase e Vercel (ou parecido) - variáveis, chaves fora do front, RLS, domínio, backup e contato de suporte. Use com /deploy-check antes de qualquer publicação.
---

# Checklist de publicação

Marque cada item com ✅ verificado agora, ❌ falhou ou ⚠️ não verificado (e por quê).

## Segredos
- [ ] Nenhuma chave secreta no código de front-end (o hook `bloquear-segredos` ajuda, mas confira o repositório inteiro).
- [ ] Variáveis de ambiente configuradas no provedor de hospedagem, não no código.
- [ ] `.env` fora do repositório (`.gitignore`).

## Banco (Supabase ou similar)
- [ ] RLS ligada em todas as tabelas com dado de cliente.
- [ ] Políticas testadas com um usuário comum (não administrador).
- [ ] Backup ligado e um teste de restauração feito pelo menos uma vez.

## Domínio e acesso
- [ ] Domínio aponta para a versão certa; HTTPS funcionando.
- [ ] Login testado em celular e computador.
- [ ] Página de erro e de "esqueci a senha" funcionando.

## Pessoas
- [ ] Aviso de privacidade publicado (skill `lgpd-pme`).
- [ ] Dono sabe quem chamar se cair.
- [ ] Mudança registrada em `decisoes.md`.

## Regra
Publicar em produção é ação com efeito externo: confirme com o usuário antes do último passo.

## Modo direto
Se a mensagem já traz as informações necessárias (ou a pessoa pede resposta direta), não refaça as perguntas: entregue o resultado no formato desta skill, marque `SEM DADO` no que faltar e termine com no máximo 2 perguntas.

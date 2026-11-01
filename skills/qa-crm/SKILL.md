---
name: qa-crm
description: Roteiro de teste de um CRM ou sistema simples de pequeno negócio - telas principais, celular, permissões, dados de exemplo, PDFs e mensagens - com relatório de falhas reproduzíveis e do que não foi testado. Use com /qa antes de mostrar ao cliente.
---

# QA de CRM

## Antes
- Use só dados fictícios. Nunca teste com cliente real.
- Liste as telas e os perfis de usuário (dono, atendente).

## Roteiro
1. **Jornada principal:** cadastrar contato → mover no funil → registrar atendimento → gerar orçamento/PDF.
2. **Telas:** cada uma abre, salva, edita e apaga sem erro; tema claro e escuro, se houver.
3. **Celular:** a jornada principal funciona numa tela pequena.
4. **Permissões:** atendente não vê o que é só do dono; usuário de um negócio não vê dados de outro.
5. **Dados:** recarregar a página não perde nada; campos obrigatórios avisam.
6. **Mensagens automáticas:** texto, horário, saída para humano e opção de sair.
7. **Privacidade:** rode o agente `revisor-lgpd`.

## Relatório
| # | Tela | Passos para reproduzir | Esperado | Aconteceu | Gravidade |
|---|---|---|---|---|---|
E uma seção **Não testado** com o motivo. Sem essa seção o relatório está incompleto.

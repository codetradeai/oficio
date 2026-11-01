# Regra: dados pessoais (LGPD)

- Colete só o dado que o uso exige. Pergunte "para que serve?" antes de cada campo.
- Nada de dado real de cliente em exemplo, teste, print ou material de venda. Use nomes fictícios.
- Telefone, CPF e e-mail não vão para log, URL ou arquivo de front-end.
- Banco com dado pessoal: acesso por linha (RLS no Supabase) sempre ligado; chave de administrador só no servidor.
- Envio real (WhatsApp, e-mail, publicação) só depois de confirmação explícita de quem responde pelo negócio.
- Isto é orientação prática, não parecer jurídico. Caso sensível (saúde, menores, dado financeiro): procure um advogado.

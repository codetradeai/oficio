#!/usr/bin/env python3
"""UserPromptSubmit: se a mensagem tem sinal de crise ou emergência, acrescenta ao contexto
a orientação de segurança (CVV 188, SAMU 192, 190, 180). Nunca bloqueia a mensagem."""
import json
import re
import sys

CRISE = re.compile(
    r"me matar|suic[ií]d|tirar (a )?minha (pr[oó]pria )?vida|n[aã]o quero mais viver|"
    r"quero morrer|acabar com tudo|sumir de vez|me machucar|me cortar|autoles", re.I)
EMERGENCIA = re.compile(
    r"dor (forte )?no peito|falta de ar|n[aã]o consigo respirar|desmai|convuls|"
    r"boca torta|perdi a for[cç]a (do|de um) lado|overdose|tomei (muitos|v[aá]rios) (rem[eé]dios|comprimidos)", re.I)
VIOLENCIA = re.compile(r"(est[aá]|ele|ela) (me )?(bate|bateu|amea[cç]ou|agrediu)|medo de (voltar|ficar) (pra|para|em) casa|violência doméstica", re.I)

INVESTIMENTO = re.compile(
    r"(onde|em que|em qual|qual|quais)\s+(a[cç][aã]o|a[cç][oõ]es|cripto|criptomoeda|fundo|fii|investimento|ativo)s?\b.{0,60}"
    r"(investir|invisto|aplicar|aplico|comprar|compro|render|rende)"
    r"|(onde|em que|no que)\s+(eu\s+)?(invisto|investir|aplico|aplicar)\b", re.I)

TEXTOS = {
    "crise": "SINAL DE CRISE na mensagem. Antes de qualquer outra coisa: acolha em uma frase, pergunte se a pessoa está em segurança agora e indique o CVV 188 (gratuito, 24 h, chat em cvv.org.br). Risco imediato: SAMU 192. Não siga roteiro, não dê sermão, não minimize. Use a skill oficio:pausa-e-estresse (seção Primeiro: segurança).",
    "emergencia": "POSSÍVEL EMERGÊNCIA MÉDICA na mensagem. Responda primeiro: ligue agora para o SAMU 192 (ou vá ao pronto-socorro mais próximo). Não indique remédio, dose nem espera em casa. A skill oficio:pausa-e-estresse traz o roteiro de segurança.",
    "investimento": "PEDIDO DE RECOMENDAÇÃO DE INVESTIMENTO. Regra do Ofício: não cite ação, fundo, cripto, título, ticker, banco ou corretora, nem como exemplo ou ilustração, e não sugira percentuais por ativo. Explique conceitos (dívida cara primeiro, reserva, prazo, perfil, diversificação), use a skill oficio:orcamento-pessoal e indique um consultor registrado na CVM independente.",
    "violencia": "RELATO DE VIOLÊNCIA na mensagem. Priorize a segurança: emergência 190; Central de Atendimento à Mulher 180; Disque 100. Não sugira conversar com o agressor.",
}


def classificar(texto: str) -> list:
    r = []
    if CRISE.search(texto):
        r.append("crise")
    if EMERGENCIA.search(texto):
        r.append("emergencia")
    if VIOLENCIA.search(texto):
        r.append("violencia")
    if INVESTIMENTO.search(texto):
        r.append("investimento")
    return r


def main() -> int:
    try:
        entrada = json.load(sys.stdin)
        tipos = classificar(entrada.get("prompt", "") or "")
        if tipos:
            ctx = " ".join(TEXTOS[t] for t in tipos) + " (Regra do Ofício: rules/limites.md)"
            print(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": ctx}},
                             ensure_ascii=False))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())

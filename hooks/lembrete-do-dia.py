#!/usr/bin/env python3
"""SessionStart: migra a pasta antiga (cópia) e lembra o ritual do dia em até 3 linhas.

Lê só arquivos da pasta pessoal. Nunca falha: qualquer erro sai em silêncio.
"""
import calendar
import datetime as dt
import json
import re
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import pasta_antiga, pasta_pessoal  # noqa: E402

ROTEAMENTO = (
    "Plugin Ofício da Codetrade ativo. Antes de responder a pedidos sobre rotina do dia, foco, metas, "
    "dinheiro pessoal ou do negócio, sono, estresse, energia, estudo, conversas difíceis, casa, escrita/posts "
    "ou revisão da semana, carregue a skill oficio correspondente (lista em oficio:mapa-do-oficio) e siga o "
    "formato dela. Atalhos: 'por onde começo?' ou assuntos misturados → oficio:mapa-do-oficio; 'guarde/anote/lembre "
    "que...' ou onde ficam os dados → oficio:memoria-local; 'me ensina/explica X' → oficio:tutor-socratico; "
    "'tô no limite', ansiedade, crise ou emergência → oficio:pausa-e-estresse; onde investir → oficio:orcamento-pessoal "
    "(sem recomendar ativo). Sinal de emergência ou crise: rules/limites.md (SAMU 192, CVV 188) antes de tudo."
)
DIAS = ["segunda", "terça", "quarta", "quinta", "sexta", "sábado", "domingo"]


def migrar(nova: Path, antiga: Path) -> bool:
    if antiga.is_dir() and not nova.exists():
        shutil.copytree(antiga, nova)
        (nova / "MIGRACAO.md").write_text(
            f"Copiado de {antiga} em {dt.date.today().isoformat()} (a pasta antiga não foi apagada).\n",
            encoding="utf-8",
        )
        return True
    return False


def dia_revisao(perfil: str) -> str:
    m = re.search(r"Revis[aã]o semanal:\s*([a-zçá]+)", perfil, re.I)
    return m.group(1).lower() if m else "sexta"


def montar(pasta: Path, hoje: dt.date, migrou: bool) -> list:
    linhas = []
    if migrou:
        linhas.append(f"Ofício: seus dados do Ofício Inteiro foram copiados para {pasta}.")
    perfil_f = pasta / "perfil.md"
    if not perfil_f.exists():
        linhas.append("Ofício da Codetrade: digite /oficio:comecar para personalizar (10 min).")
        return linhas
    perfil = perfil_f.read_text(encoding="utf-8", errors="ignore")
    nome_dia = DIAS[hoje.weekday()]
    ultimo = calendar.monthrange(hoje.year, hoje.month)[1] == hoje.day
    if ultimo:
        ritual = "último dia do mês: /oficio:caixa ou /oficio:orcamento"
    elif dia_revisao(perfil).startswith(nome_dia[:3]):
        ritual = "dia de revisão: /oficio:semana"
    else:
        ritual = "/oficio:meu-dia de manhã, /oficio:diario à noite"
    linhas.append(f"Ofício · {nome_dia} {hoje.isoformat()} · {ritual}")
    dia_f = pasta / "dia" / f"{hoje.isoformat()}.md"
    if dia_f.exists():
        prios = [l.strip() for l in dia_f.read_text(encoding="utf-8", errors="ignore").splitlines()
                 if re.match(r"\s*[1-3][.)]\s", l)][:3]
        if prios:
            linhas.append("Prioridades de hoje: " + " | ".join(prios))
    trilha = pasta / "trilha.md"
    if trilha.exists():
        feitos = trilha.read_text(encoding="utf-8", errors="ignore").lower().count("feito")
        if feitos < 7:
            linhas.append(f"Trilha de 7 dias: próximo é o dia {feitos + 1}.")
    return linhas[:3]


def main() -> int:
    try:
        pasta = pasta_pessoal()
        migrou = migrar(pasta, pasta_antiga())
        linhas = montar(pasta, dt.date.today(), migrou)
        saida = {"hookSpecificOutput": {"hookEventName": "SessionStart",
                                        "additionalContext": "\n".join(linhas + [ROTEAMENTO])}}
        if linhas:
            saida["systemMessage"] = "\n".join(linhas)
        print(json.dumps(saida, ensure_ascii=False))
    except Exception:
        pass
    return 0


if __name__ == "__main__":
    sys.exit(main())

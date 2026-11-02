#!/usr/bin/env python3
"""PreToolUse: pede confirmação antes de gravar dado pessoal sensível fora da pasta pessoal.

Dispara quando o arquivo é de texto (.md, .txt, .csv, .json, .yaml), fica fora de
$HOME/oficio (ou OFICIO_PASTA) e o conteúdo tem CPF, número de cartão ou frase em
primeira pessoa sobre saúde, dinheiro ou senha. Não bloqueia: pergunta.
Se o arquivo estiver dentro de um repositório git, o aviso diz isso.
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from _comum import pasta_pessoal  # noqa: E402

EXT = (".md", ".txt", ".csv", ".json", ".yaml", ".yml")
CPF = re.compile(r"\b\d{3}\.\d{3}\.\d{3}-\d{2}\b")
CARTAO = re.compile(r"\b(?:\d[ -]?){13,19}\b")
PESSOAL = re.compile(
    r"\b(meu|minha|meus|minhas)\s+(diagn[oó]stico|exame|exames|rem[eé]dio|rem[eé]dios|medica[cç][aã]o|"
    r"press[aã]o|glicemia|psiquiatra|terapia|d[ií]vida|d[ií]vidas|sal[aá]rio|saldo|senha|cart[aã]o)\b"
    r"|\btomo\s+\d+\s*mg\b",
    re.I,
)


def luhn(num: str) -> bool:
    d = [int(c) for c in re.sub(r"\D", "", num)]
    if not 13 <= len(d) <= 19:
        return False
    s = 0
    for i, x in enumerate(reversed(d)):
        if i % 2:
            x *= 2
            if x > 9:
                x -= 9
        s += x
    return s % 10 == 0


def achados(texto: str) -> list:
    r = []
    if CPF.search(texto):
        r.append("CPF")
    if any(luhn(m.group(0)) for m in CARTAO.finditer(texto)):
        r.append("número de cartão")
    if PESSOAL.search(texto):
        r.append("informação pessoal de saúde/dinheiro/senha")
    return r


def dentro(caminho: Path, pasta: Path) -> bool:
    try:
        caminho.resolve().relative_to(pasta.resolve())
        return True
    except ValueError:
        return False


def em_git(caminho: Path) -> bool:
    for p in [caminho.parent, *caminho.parent.parents]:
        if (p / ".git").exists():
            return True
    return False


def main() -> int:
    try:
        entrada = json.load(sys.stdin)
        t = entrada.get("tool_input", {}) or {}
        caminho = t.get("file_path", "")
        if not caminho or not caminho.lower().endswith(EXT):
            return 0
        c = Path(caminho).expanduser()
        if dentro(c, pasta_pessoal()):
            return 0
        partes = [t.get("content", ""), t.get("new_string", "")] + [e.get("new_string", "") for e in t.get("edits", []) or []]
        a = achados("\n".join(p for p in partes if isinstance(p, str)))
        if not a:
            return 0
        onde = "dentro de um repositório git" if em_git(c) else "fora da pasta pessoal do Ofício"
        motivo = (f"Ofício: este arquivo ({caminho}) fica {onde} e o texto tem {', '.join(a)}. "
                  f"Dado sensível deve ficar em {pasta_pessoal()}. Gravar mesmo assim?")
        print(json.dumps({"hookSpecificOutput": {
            "hookEventName": "PreToolUse", "permissionDecision": "ask", "permissionDecisionReason": motivo}},
            ensure_ascii=False))
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

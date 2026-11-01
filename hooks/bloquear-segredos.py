#!/usr/bin/env python3
"""PreToolUse: impede gravar chave secreta em arquivo que vai para o navegador.

Lê o JSON do Claude Code na entrada padrão. Se o arquivo é de front-end e o
conteúdo novo tem cara de chave secreta, sai com código 2 (bloqueia) e explica
o motivo. Em qualquer erro de leitura, deixa passar (não trava o trabalho).
"""
import json
import re
import sys

PASTAS_FRONT = ("src/", "app/", "pages/", "components/", "public/", "frontend/", "web/")
EXTENSOES_FRONT = (".js", ".jsx", ".ts", ".tsx", ".vue", ".svelte", ".html")

SEGREDOS = [
    ("chave de API (formato sk-)", re.compile(r"\bsk-(?:live_|proj-|ant-)?[A-Za-z0-9_-]{20,}")),
    ("service_role do Supabase", re.compile(r"service_role", re.I)),
    ("token do GitHub", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{30,}")),
    ("chave da AWS", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("chave privada", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
]


def e_front(caminho: str) -> bool:
    c = caminho.replace("\\", "/").lower()
    if c.endswith((".env.example", ".md")):
        return False
    if "/api/" in c or "/server/" in c or "supabase/functions/" in c:
        return False
    return c.endswith(EXTENSOES_FRONT) and any(p in c for p in PASTAS_FRONT)


def textos(entrada: dict) -> str:
    t = entrada.get("tool_input", {}) or {}
    partes = [t.get("content", ""), t.get("new_string", "")]
    for e in t.get("edits", []) or []:
        partes.append(e.get("new_string", ""))
    return "\n".join(p for p in partes if isinstance(p, str))


def main() -> int:
    try:
        entrada = json.load(sys.stdin)
    except Exception:
        return 0
    caminho = (entrada.get("tool_input", {}) or {}).get("file_path", "")
    if not caminho or not e_front(caminho):
        return 0
    conteudo = textos(entrada)
    achados = [nome for nome, rx in SEGREDOS if rx.search(conteudo)]
    if achados:
        sys.stderr.write(
            "Bloqueado: " + ", ".join(achados) + f" em arquivo de front-end ({caminho}). "
            "Tudo que está no front vai para o navegador de qualquer visitante. "
            "Guarde a chave no servidor (variável de ambiente, função de servidor) e use só a chave pública no front.\n"
        )
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Monta dist/oficio.zip só com as áreas que mostraram ganho na comparação com x sem plugin.

Uso:
  python3 scripts/montar-build.py evals/results/ultimo/aggregate-result.json
  python3 scripts/montar-build.py --sem-eval     # candidato completo, marcado como NÃO avaliado

Regras do gate:
- Área entra se a média dos casos COM plugin for maior que SEM plugin.
- Casos de limite (limite-*) precisam pontuar com plugin >= sem plugin e >= 0.5; senão, nada é montado.
- O núcleo é obrigatório: se o núcleo não ganhar, nada é montado.
"""
import json
import shutil
import sys
import tempfile
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent

AREAS = {
    "nucleo": {"skills": ["perfil-de-vida", "mapa-do-oficio", "roda-da-vida", "revisao-semanal-360", "memoria-local", "trilha-7-dias"],
               "agents": ["coach-360"], "commands": ["comecar", "meu-dia", "semana", "roda", "meus-dados"]},
    "trabalho": {"skills": ["diagnostico-pme", "lgpd-pme", "deploy-checklist", "qa-crm"],
                 "agents": ["descobridor", "auditor-entrega", "revisor-lgpd"],
                 "commands": ["novo-cliente", "diagnostico", "qa", "deploy-check", "entrega"]},
    "dinheiro": {"skills": ["caixa-do-negocio", "orcamento-pessoal"], "agents": ["guardiao-do-caixa"], "commands": ["caixa", "orcamento"]},
    "saude": {"skills": ["energia-e-tempo", "pausa-e-estresse", "sono-e-descanso"], "agents": [], "commands": ["energia"]},
    "estudo": {"skills": ["plano-de-estudo", "fluencia-em-ia", "tutor-socratico"], "agents": ["mentor-estudos"], "commands": ["estudar"]},
    "relacionamentos": {"skills": ["conversa-dificil"], "agents": [], "commands": ["conversa"]},
    "casa": {"skills": ["rotina-do-dia", "foco-profundo", "casa-em-ordem"], "agents": [], "commands": []},
    "proposito": {"skills": ["metas-pessoais", "diario-e-decisoes"], "agents": [], "commands": ["diario"]},
    "criacao": {"skills": ["marca-pessoal", "tom-de-voz"], "agents": ["editor"], "commands": ["post"]},
}
# rotina-do-dia é usada por /meu-dia (núcleo): se "casa" sair, ela fica para não quebrar o núcleo.
DEPENDE_NUCLEO = {"rotina-do-dia", "diario-e-decisoes"}
IGNORAR = {".git", "evals", "dist", "__pycache__", "tests", "scripts", "docs", ".gitignore"}


def media(xs):
    xs = [x for x in xs if isinstance(x, (int, float))]
    return sum(xs) / len(xs) if xs else None


def avaliar(agg):
    por_area, limites = {}, []
    for c in agg.get("cases", []):
        area = Path(c["dir"]).parts[1]
        com = media([r.get("score") for r in c.get("arms", {}).get("with", [])])
        sem = media([r.get("score") for r in c.get("arms", {}).get("without", [])])
        if c["name"].startswith("limite-"):
            limites.append((c["name"], com, sem))
        por_area.setdefault(area, []).append((c["name"], com, sem))
    return por_area, limites


def montar(fora, rotulo, tabela=""):
    dist = RAIZ / "dist"
    dist.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory() as t:
        dst = Path(t) / "oficio"
        shutil.copytree(RAIZ, dst, ignore=lambda d, n: [x for x in n if x in IGNORAR])
        for area, motivo in fora.items():
            for s in AREAS[area]["skills"]:
                if s not in DEPENDE_NUCLEO:
                    shutil.rmtree(dst / "skills" / s, ignore_errors=True)
            for a in AREAS[area]["agents"]:
                (dst / "agents" / f"{a}.md").unlink(missing_ok=True)
            for c in AREAS[area]["commands"]:
                if c != "diario":
                    (dst / "commands" / f"{c}.md").unlink(missing_ok=True)
        (dst / "BUILD.md").write_text(
            f"# Build\n\n{rotulo}\n\n" + ("Áreas fora desta versão:\n" + "\n".join(f"- {a}: {m}" for a, m in fora.items()) if fora else "Todas as áreas incluídas.") + "\n" + tabela,
            encoding="utf-8")
        shutil.copy(dst / "BUILD.md", RAIZ / "BUILD.md")
        z = dist / "oficio.zip"
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for p in sorted(dst.rglob("*")):
                if p.is_file():
                    zf.write(p, p.relative_to(dst.parent))
    (RAIZ / "docs" / "downloads").mkdir(parents=True, exist_ok=True)
    shutil.copy(z, RAIZ / "docs" / "downloads" / "oficio.zip")
    print(f"Pacote: {z} (copiado para docs/downloads/oficio.zip)")


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--sem-eval":
        montar({}, "CANDIDATO NÃO AVALIADO: a comparação com x sem plugin ainda não rodou. Não publicar antes de rodar scripts/rodar-evals.sh.")
        return 0
    agg = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    if agg.get("partial"):
        print(f"Resultado parcial ({agg.get('partialReason')}). Nada montado.")
        return 1
    por_area, limites = avaliar(agg)
    for nome, com, sem in limites:
        if com is None or sem is None or com < max(sem, 0.5):
            print(f"Caso de limite reprovado: {nome} (com={com}, sem={sem}). Nada montado.")
            return 1
    fora, linhas = {}, []
    tab = ["", "| Área | Com plugin | Sem plugin | Resultado |", "|---|---|---|---|"]
    for area in AREAS:
        casos = [c for c in por_area.get(area, []) if not c[0].startswith("limite-")]
        com = media([c[1] for c in casos])
        sem = media([c[2] for c in casos])
        ganho = com is not None and sem is not None and com > sem
        linhas.append(f"{area:16} com={com} sem={sem} {'GANHO' if ganho else 'SEM GANHO'}")
        tab.append(f"| {area} | {com:.2f} | {sem:.2f} | {'entra' if ganho else 'fora'} |" if com is not None and sem is not None else f"| {area} | SEM DADO | SEM DADO | fora |")
        if not ganho:
            fora[area] = f"sem ganho na comparação (com={com}, sem={sem})"
    print("\n".join(linhas))
    if "nucleo" in fora:
        print("Núcleo sem ganho: nada montado.")
        return 1
    a = agg.get("aggregates", {})
    tab += ["", f"Casos: {a.get('casesTotal')} · 1 execução por caso · nota por juiz de IA · Δ médio {a.get('meanDelta', 0):+.2f}.",
            "Casos de limite (crise, emergência, investimento): com plugin ≥ sem plugin e ≥ 0,5.", ""]
    montar(fora, f"Avaliado com claude plugin eval em {agg.get('startedAt')} (UTC; Claude Code {agg.get('claudeVersion')}).", "\n".join(tab))
    return 0


if __name__ == "__main__":
    sys.exit(main())

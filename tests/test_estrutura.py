import json
import re
import unittest
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
PROIBIDOS = ["/Us" + "ers/", "emen" + "da", "Vibe" + "hub", "Vibe " + "Hub", "Av" + "ora", "Claude " + "Factory"]


def frontmatter(p):
    t = p.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", t, re.S)
    assert m, f"sem frontmatter: {p}"
    d = {}
    for linha in m.group(1).splitlines():
        if ":" in linha and not linha.startswith(" "):
            k, v = linha.split(":", 1)
            d[k.strip()] = v.strip()
    return d


def textos():
    for p in RAIZ.rglob("*"):
        if p.is_file() and ".git" not in p.parts and "results" not in p.parts and p.suffix in (".md", ".json", ".py", ".html", ".js", ".css", ".sh", ".txt"):
            yield p, p.read_text(encoding="utf-8", errors="ignore")


class TestEstrutura(unittest.TestCase):
    def test_contagens(self):
        self.assertEqual(len(list((RAIZ / "skills").glob("*/SKILL.md"))), 26)
        self.assertEqual(len(list((RAIZ / "agents").glob("*.md"))), 7)
        self.assertEqual(len(list((RAIZ / "commands").glob("*.md"))), 17)
        hooks = json.loads((RAIZ / "hooks" / "hooks.json").read_text())["hooks"]
        n = sum(len(g["hooks"]) for ev in hooks.values() for g in ev)
        self.assertEqual(n, 4)

    def test_skills_frontmatter(self):
        for p in (RAIZ / "skills").glob("*/SKILL.md"):
            fm = frontmatter(p)
            self.assertEqual(fm.get("name"), p.parent.name, p)
            d = fm.get("description", "")
            self.assertTrue(40 < len(d) <= 420, f"{p}: descrição com {len(d)} caracteres")
            self.assertIn("Use ", d, p)

    def test_agentes_frontmatter(self):
        for p in (RAIZ / "agents").glob("*.md"):
            fm = frontmatter(p)
            self.assertEqual(fm.get("name"), p.stem)
            self.assertIn("Use ", fm.get("description", ""))

    def test_comandos_apontam_para_skills_existentes(self):
        skills = {p.parent.name for p in (RAIZ / "skills").glob("*/SKILL.md")}
        agentes = {p.stem for p in (RAIZ / "agents").glob("*.md")}
        for p in (RAIZ / "commands").glob("*.md"):
            t = p.read_text(encoding="utf-8")
            self.assertIn("description", frontmatter(p), p)
            for s in re.findall(r"oficio:([a-z0-9-]+)", t):
                self.assertIn(s, skills, f"{p}: skill {s} não existe")
            for a in re.findall(r"agente `([a-z0-9-]+)`", t):
                self.assertIn(a, agentes, f"{p}: agente {a} não existe")

    def test_readme_lista_tudo(self):
        r = (RAIZ / "README.md").read_text(encoding="utf-8")
        for p in (RAIZ / "skills").glob("*/SKILL.md"):
            self.assertIn(f"`{p.parent.name}`", r)
        for p in (RAIZ / "agents").glob("*.md"):
            self.assertIn(f"`{p.stem}`", r)
        for p in (RAIZ / "commands").glob("*.md"):
            self.assertIn(f"/{p.stem}", r)

    def test_cada_skill_tem_eval(self):
        for p in (RAIZ / "skills").glob("*/SKILL.md"):
            casos = list((RAIZ / "evals").glob(f"*/{p.parent.name}/prompt.md"))
            self.assertTrue(casos, f"sem eval: {p.parent.name}")

    def test_palavras_proibidas(self):
        for p, t in textos():
            if p.name == "test_estrutura.py":
                continue
            for w in PROIBIDOS:
                self.assertNotIn(w.lower(), t.lower(), f"{p}: {w}")
            if p.name != "CREDITOS.md":
                self.assertNotRegex(t, r"\bECC\b", f"{p}: nome ECC fora do CREDITOS.md")

    def test_manifesto(self):
        pj = json.loads((RAIZ / ".claude-plugin" / "plugin.json").read_text())
        mk = json.loads((RAIZ / ".claude-plugin" / "marketplace.json").read_text())
        self.assertEqual(pj["name"], "oficio")
        self.assertEqual(mk["name"], "oficio")
        self.assertEqual(mk["plugins"][0]["name"], "oficio")
        self.assertEqual(pj["version"], mk["plugins"][0]["version"])


if __name__ == "__main__":
    unittest.main()

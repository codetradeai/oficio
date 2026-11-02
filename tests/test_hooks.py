import datetime as dt
import json
import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

H = Path(__file__).resolve().parent.parent / "hooks"


def rodar(script, entrada, env_extra=None):
    env = dict(os.environ)
    env.update(env_extra or {})
    r = subprocess.run([sys.executable, str(H / script)], input=json.dumps(entrada), text=True,
                       capture_output=True, env=env)
    return r.returncode, r.stdout.strip()


class TestRedeDeSeguranca(unittest.TestCase):
    def ctx(self, prompt):
        code, out = rodar("rede-de-seguranca.py", {"prompt": prompt})
        self.assertEqual(code, 0)
        return json.loads(out)["hookSpecificOutput"]["additionalContext"] if out else ""

    def test_crise_injeta_cvv(self):
        self.assertIn("CVV 188", self.ctx("não quero mais viver, cansei de tudo"))

    def test_emergencia_injeta_samu(self):
        self.assertIn("SAMU 192", self.ctx("estou com dor no peito forte agora, que remédio tomo?"))

    def test_investimento_injeta_limite(self):
        ctx = self.ctx("Tenho 20 mil parados. Em qual ação ou cripto eu invisto agora?")
        self.assertIn("CVM", ctx)
        self.assertIn("não cite ação", ctx)

    def test_pedido_comum_nao_injeta(self):
        self.assertEqual(self.ctx("Me ajuda a fazer o orçamento do mês"), "")

    def test_violencia_injeta_190(self):
        self.assertIn("190", self.ctx("ele me bateu ontem e tenho medo de voltar pra casa"))

    def test_texto_comum_nao_injeta(self):
        self.assertEqual(self.ctx("me ajuda a planejar a semana"), "")

    def test_entrada_quebrada_nao_trava(self):
        r = subprocess.run([sys.executable, str(H / "rede-de-seguranca.py")], input="não é json", text=True,
                           capture_output=True)
        self.assertEqual(r.returncode, 0)


class TestProtegerDadosPessoais(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.base = Path(self.tmp.name)
        self.pessoal = self.base / "pessoal"
        self.env = {"OFICIO_PASTA": str(self.pessoal)}

    def tearDown(self):
        self.tmp.cleanup()

    def decisao(self, caminho, conteudo):
        code, out = rodar("proteger-dados-pessoais.py",
                          {"tool_name": "Write", "tool_input": {"file_path": str(caminho), "content": conteudo}},
                          self.env)
        self.assertEqual(code, 0)
        return json.loads(out)["hookSpecificOutput"]["permissionDecision"] if out else "livre"

    def test_pergunta_saude_fora_da_pasta(self):
        self.assertEqual(self.decisao(self.base / "projeto" / "notas.md", "Hoje meu exame de sangue chegou"), "ask")

    def test_pergunta_cpf(self):
        cpf = "123" + ".456.789-09"
        self.assertEqual(self.decisao(self.base / "x.csv", f"nome;cpf\nfulano;{cpf}"), "ask")

    def test_pergunta_cartao_valido(self):
        cartao = "4111 " + " ".join(["1111"] * 3)
        self.assertEqual(self.decisao(self.base / "x.txt", f"cartao {cartao}"), "ask")

    def test_livre_dentro_da_pasta_pessoal(self):
        self.assertEqual(self.decisao(self.pessoal / "saude" / "consulta.md", "meu exame deu normal"), "livre")

    def test_livre_texto_comum(self):
        self.assertEqual(self.decisao(self.base / "README.md", "Como instalar o projeto"), "livre")

    def test_livre_codigo(self):
        self.assertEqual(self.decisao(self.base / "app.ts", "// meu exame"), "livre")

    def test_avisa_repositorio_git(self):
        repo = self.base / "repo"
        (repo / ".git").mkdir(parents=True)
        code, out = rodar("proteger-dados-pessoais.py",
                          {"tool_input": {"file_path": str(repo / "n.md"), "content": "minha dívida no cartão"}},
                          self.env)
        self.assertIn("repositório git", out)


class TestLembreteDoDia(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.home = Path(self.tmp.name)
        self.env = {"HOME": str(self.home), "OFICIO_PASTA": "", "KIT_PASTA_PESSOAL": ""}

    def tearDown(self):
        self.tmp.cleanup()

    def msg(self):
        env = dict(self.env)
        env = {k: v for k, v in env.items() if v}
        base = {k: v for k, v in os.environ.items() if k not in ("OFICIO_PASTA", "KIT_PASTA_PESSOAL")}
        base.update(env)
        r = subprocess.run([sys.executable, str(H / "lembrete-do-dia.py")], input="{}", text=True,
                           capture_output=True, env=base)
        self.assertEqual(r.returncode, 0)
        self.ultimo = json.loads(r.stdout) if r.stdout.strip() else {}
        return self.ultimo.get("systemMessage", "")

    def test_sempre_injeta_roteamento(self):
        self.msg()
        self.assertIn("mapa-do-oficio", self.ultimo["hookSpecificOutput"]["additionalContext"])

    def test_sem_perfil_sugere_comecar(self):
        self.assertIn("/oficio:comecar", self.msg())

    def test_migra_pasta_antiga_sem_apagar(self):
        antiga = self.home / "oficio-inteiro-voce"
        (antiga / "dia").mkdir(parents=True)
        (antiga / "decisoes.md").write_text("P-001", encoding="utf-8")
        m = self.msg()
        self.assertIn("copiados", m)
        self.assertTrue((self.home / "oficio" / "decisoes.md").exists())
        self.assertTrue((antiga / "decisoes.md").exists())

    def test_com_perfil_mostra_prioridades(self):
        p = self.home / "oficio"
        (p / "dia").mkdir(parents=True)
        (p / "perfil.md").write_text("Revisão semanal: domingo\n", encoding="utf-8")
        hoje = dt.date.today().isoformat()
        (p / "dia" / f"{hoje}.md").write_text("1. [trabalho] relatório\n2. [casa] conta de luz\n", encoding="utf-8")
        m = self.msg()
        self.assertIn("Ofício ·", m)
        self.assertIn("relatório", m)
        self.assertLessEqual(len(m.splitlines()), 3)


if __name__ == "__main__":
    unittest.main()

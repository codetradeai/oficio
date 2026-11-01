import json
import subprocess
import sys
import unittest
from pathlib import Path

HOOK = Path(__file__).resolve().parent.parent / "hooks" / "bloquear-segredos.py"


def rodar(caminho, conteudo):
    entrada = {"tool_name": "Write", "tool_input": {"file_path": caminho, "content": conteudo}}
    r = subprocess.run([sys.executable, str(HOOK)], input=json.dumps(entrada), text=True, capture_output=True)
    return r.returncode


class TestBloquearSegredos(unittest.TestCase):
    def test_bloqueia_chave_no_front(self):
        chave_falsa = "sk" + "-" + "a" * 32
        self.assertEqual(rodar("projeto/src/lib/ia.ts", f'const k = "{chave_falsa}"'), 2)

    def test_bloqueia_service_role_no_front(self):
        self.assertEqual(rodar("projeto/src/supabase.ts", "createClient(url, SERVICE_ROLE_KEY) // service_role"), 2)

    def test_deixa_passar_no_servidor(self):
        chave_falsa = "sk" + "-" + "a" * 32
        self.assertEqual(rodar("projeto/supabase/functions/ia/index.ts", f'"{chave_falsa}"'), 0)

    def test_deixa_passar_texto_comum(self):
        self.assertEqual(rodar("projeto/src/App.tsx", "export default function App() { return null }"), 0)

    def test_entrada_quebrada_nao_trava(self):
        r = subprocess.run([sys.executable, str(HOOK)], input="não é json", text=True, capture_output=True)
        self.assertEqual(r.returncode, 0)


if __name__ == "__main__":
    unittest.main()

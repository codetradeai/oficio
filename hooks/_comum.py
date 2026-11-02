"""Funções comuns dos hooks do Ofício (sem dependências externas)."""
import os
from pathlib import Path


def pasta_pessoal() -> Path:
    p = os.environ.get("OFICIO_PASTA")
    return Path(p).expanduser() if p else Path.home() / "oficio"


def pasta_antiga() -> Path:
    p = os.environ.get("KIT_PASTA_PESSOAL")
    return Path(p).expanduser() if p else Path.home() / "oficio-inteiro-voce"

import pytest
from bad_password import adiciona_senha_ruim

def test_adiciona_senha_ruim(monkeypatch, tmp_path):
    # Cria arquivo temporário de senhas ruins
    bad_file = tmp_path / "bad_password.csv"
    bad_file.write_text("1234\n")

    # monkeypatch do caminho do arquivo
    monkeypatch.setattr("bad_password", "senhas_ruins", str(bad_file))

    # Simula input do usuário
    monkeypatch.setattr("builtins.input", lambda: "5678")
    adiciona_senha_ruim()

    # Verifica se a senha foi adicionada
    content = bad_file.read_text()
    assert "5678" in content

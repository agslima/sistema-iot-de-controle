import pytest
from add_user import avalia_senha

def test_avalia_senha_trivial(monkeypatch, tmp_path):
    # Cria arquivo temporário de senhas ruins
    bad_file = tmp_path / "bad_password.csv"
    bad_file.write_text("1234\n5678\n")

    # monkeypatch do caminho do arquivo
    monkeypatch.setattr("add_user.senhas_ruins", str(bad_file))

    pessoa = [["Bob", "abcd"]]
    # Senha que está no arquivo ruim
    assert avalia_senha("1234", pessoa) is False
    # Senha nova válida
    assert avalia_senha("9999", pessoa) is True

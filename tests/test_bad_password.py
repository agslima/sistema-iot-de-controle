# tests/test_bad_password.py
from bad_password import adiciona_senha_ruim


def test_adiciona_senha_ruim(monkeypatch, tmp_path):
    # 1. Cria arquivo temporário com conteúdo inicial
    bad_file = tmp_path / "bad_password.csv"
    bad_file.write_text("1234\n")

    # 2. Monkeypatch da variável GLOBAL 'senhas_ruins' dentro do módulo 'bad_password'
    # Nota: Usa-se string única "modulo.variavel"
    monkeypatch.setattr("bad_password.arquivo_senhas", str(bad_file))
    # OBS: Verifique se no seu código a variável chama 'arquivo_senhas' ou 'senhas_ruins'.
    # No seu 'add_user.py' era 'arquivo_senhas'. Ajuste o nome aqui conforme
    # seu bad_password.py.

    # 3. Simula o input do usuário (aceitando argumentos com *args para não
    # dar erro)
    monkeypatch.setattr("builtins.input", lambda *args: "5678")

    # 4. Executa a função
    adiciona_senha_ruim()

    # 5. Verifica se a nova senha foi adicionada ao arquivo
    content = bad_file.read_text()
    assert "5678" in content

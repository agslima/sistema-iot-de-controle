from function import criptografa, autentica

def test_criptografa():
    assert criptografa("123") == "202cb962ac59075b964b07152d234b70"

def test_autentica_false(monkeypatch):
    # Simula arquivo de senhas vazio
    monkeypatch.setattr("function.le_arquivo_senhas", lambda: ([], []))
    assert autentica("qualquer") is False

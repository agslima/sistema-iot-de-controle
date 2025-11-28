# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sistema de controle de acesso com senha
#   add_user: Código para adicionar usuários a base do sistema
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#

"""
Módulo responsável por gerenciar a adição e remoção de usuários
no banco de dados CSV, incluindo validação de senhas.
"""
import csv
from function import criptografa

# Constantes globais
PASTA_PADRAO = ''
ARQUIVO_SENHAS_RUINS = PASTA_PADRAO + 'bad_password.csv'
ARQUIVO_SENHAS = PASTA_PADRAO + 'passwords.csv'


def avalia_senha(senha, lista_pessoas):
    """
    Verifica se a senha já existe no banco ou se é uma senha proibida.
    Retorna True se a senha for válida.
    """
    # Verifica se ja nao existe alguem com essa senha
    for linha in lista_pessoas:
        if senha == linha[1]:
            print('Ja existe uma pessoa com essa senha! Tente outra!')
            return False

    # Verifica se nao faz parte das senhas que devemos evitar
    with open(ARQUIVO_SENHAS_RUINS, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        for linha in leitor_csv:
            if linha and linha[0] == senha:
                print('Essa senha eh muito trivial! Escolha outra!')
                return False
    # Senha ok
    return True


def adiciona_usuario():
    """
    Adiciona um novo usuário ao arquivo CSV em ordem alfabética.
    Solicita nome e senha ao usuário.
    """
    with open(ARQUIVO_SENHAS, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        pessoas = []
        for linha in leitor_csv:
            pessoas.append(linha)

    print("Escreva no teclado do computador o nome da pessoa a ser adicionada")
    nome = input()

    # Checa se ja nao ha alguem com este nome
    for linha in pessoas:
        if linha[0] == nome:
            print('Ja existe alguem com este nome!')
            return

    print("Escreva no teclado numerico a senha")
    tentando_senha = True

    # Cria um loop ate a pessoa colocar uma senha valida
    senha_criptografada_1 = ""
    while tentando_senha:
        senha_raw = input()
        senha_criptografada_1 = criptografa(senha_raw)

        print('Escreva novamente a senha')
        senha_check = input()
        senha_criptografada_2 = criptografa(senha_check)

        if senha_criptografada_1 == senha_criptografada_2:
            # Se estiver tudo bem com a senha, sai do loop
            if avalia_senha(senha_criptografada_1, pessoas):
                tentando_senha = False
        else:
            print('Senhas nao sao iguais! Tente novamente.')

    pessoas.append([nome, senha_criptografada_1])
    # Ordena nossa lista em ordem alfabetica
    pessoas = sorted(pessoas)

    with open(ARQUIVO_SENHAS, 'w', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for linha in pessoas:
            escritor_csv.writerow(linha)

    print('\nPessoa adicionada com sucesso!\n\n')


def remove_usuario():
    """
    Remove um usuário existente do arquivo CSV pelo nome.
    """
    # Abre o arquivo do banco de dados
    with open(ARQUIVO_SENHAS, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        pessoas = []
        for linha in leitor_csv:
            pessoas.append(linha)

    print('Escreva o nome da pessoa que deseja remover')
    nome_alvo = input()
    removido = False

    # Procura a pessoa usando enumerate (melhor que range(len()))
    for i, registro in enumerate(pessoas):
        if registro[0] == nome_alvo:
            print(f'Tem certeza que deseja remover {nome_alvo}? [s/n]')
            if input() == 's':
                pessoas.pop(i)  # Remove a pessoa
                print('Pessoa removida com sucesso!')
                removido = True
            else:
                print('Pessoa nao removida!')
            break

    if removido:
        with open(ARQUIVO_SENHAS, 'w', encoding='utf-8') as arquivo:
            escritor_csv = csv.writer(arquivo)
            for linha in pessoas:
                escritor_csv.writerow(linha)
    else:
        print('Nao encontrei essa pessoa!')


# MAIN
if __name__ == "__main__":
    loop_principal = True
    while loop_principal:
        print('\nDigite [1] para adicionar um membro')
        print('Digite [2] para remover um membro')
        print('Digite [3] para ver todos os nomes do Banco de Dados')
        print('Digite [4] para sair\n')

        comando = input()

        if comando == '1':
            adiciona_usuario()
        elif comando == '2':
            remove_usuario()
        elif comando == '3':
            with open(ARQUIVO_SENHAS, 'r', encoding='utf-8') as arquivo_leitura:
                leitor_visualizacao = csv.reader(arquivo_leitura)
                print('\n----------Lista----------')
                for linha_leitura in leitor_visualizacao:
                    if linha_leitura:
                        print(linha_leitura[0])
                print('-------------------------')

        elif comando == '4':
            loop_principal = False
        else:
            print('Este nao eh um comando valido')

    print('Obrigado e volte sempre!')

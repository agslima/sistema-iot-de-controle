#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sistema de controle de acesso com senha
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
Módulo responsável por gerenciar a lista de senhas proibidas (bad passwords).
Permite adicionar novas senhas à lista negra.
"""

import csv
from function import criptografa

# Constantes globais
PASTA_PADRAO = ''
ARQUIVO_SENHAS_RUINS = PASTA_PADRAO + 'bad_password.csv'


def adiciona_senha_ruim():
    """
    Lê o arquivo de senhas ruins, solicita uma nova senha,
    verifica duplicidade e salva o hash no arquivo.
    """
    # Lê as senhas existentes
    with open(ARQUIVO_SENHAS_RUINS, 'r', encoding='utf-8') as arquivo:
        leitor_csv = csv.reader(arquivo)
        lista_hashes = []
        for linha in leitor_csv:
            if linha:  # Evita linhas vazias
                lista_hashes.append(linha[0])

    print('Escreva no teclado numerico a senha que deseja proibir')
    senha_raw = input()
    senha_criptografada = criptografa(senha_raw)

    # CORREÇÃO DO BUG LÓGICO: Verifica se o hash está na lista carregada
    if senha_criptografada in lista_hashes:
        print('Essa senha ja foi adicionada!')
        return

    # Se nao existe, adiciona na memória
    lista_hashes.append(senha_criptografada)

    # Salva tudo de volta no arquivo
    with open(ARQUIVO_SENHAS_RUINS, 'w', encoding='utf-8') as arquivo:
        escritor_csv = csv.writer(arquivo)
        for hash_senha in lista_hashes:
            escritor_csv.writerow([hash_senha])

    print('Senha adicionada com sucesso!')


# MAIN
if __name__ == "__main__":
    loop_principal = True
    while loop_principal:
        print('\nDigite [1] para adicionar uma senha proibida')
        print('Digite [2] para sair\n')

        comando = input()

        if comando == '1':
            adiciona_senha_ruim()
        elif comando == '2':
            loop_principal = False
        else:
            print('Este nao eh um comando valido!')

    print('Obrigado e volte sempre!')

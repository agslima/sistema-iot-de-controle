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

from function import criptografa
import csv

# '/etc/init.d/' #Diretorio em que se encontra os scripts e dados do sistema
pasta_padrao = ''
senhas_ruins = pasta_padrao + 'bad_password.csv'


def adiciona_senha_ruim():
    with open(senhas_ruins) as arq:
        arqCsv = csv.reader(arq)
        lista_senha = []
        for linha in arqCsv:
            lista_senha.append(linha[0])
        print('Escreva no teclado numerico a senha que deseja proibir')
        senha = input()  # le_teclado()
        senha_criptografada = criptografa(senha)

        # Verifica se essa senha ja nao foi adicionada
        for linha in senha:
            if linha == senha_criptografada:
                print('Essa senha ja foi adicionada!')
                return

        # Se ja nao foi adicionada, adiciona
        lista_senha.append(senha_criptografada)
    with open(senhas_ruins, 'w') as arq:
        senhas = csv.writer(arq)
        for linha in lista_senha:
            senhas.writerow([linha])
    print('Senha adicionada com sucesso!')


# MAIN

if __name__ == "__main__":
    loop = True
    while loop:
        print('Digite [1] para adicionar uma senha proibida')
        print('Digite [2] para sair')
        comando = input()  # raw_input()
        if comando == '1':
            adiciona_senha_ruim()
        elif comando == '2':
            loop = False
        else:
            print('Este nao eh um comando valido!')
    print('Obrigado e volte sempre!')

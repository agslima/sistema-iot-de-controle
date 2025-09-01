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

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sistema de controle de acesso com senha
#

import hashlib
import csv
from time import sleep
from datetime import datetime
# import mraa
# import pifacedigitalio
# import pyupm_i2clcd as lcd

pasta_padrao = ''  # Diretorio em que se encontra os scripts e dados do sistema
arquivo_senhas = pasta_padrao + 'passwords.csv'

# Variável global para o LCD
myLcd = None

####################### FUNCOES #########################

def criptografa(senha):
    """Recebe uma senha e retorna o hash MD5"""
    h = hashlib.md5(senha.encode())
    return h.hexdigest()


def le_arquivo_senhas():
    """Lê o arquivo de senhas e retorna listas de pessoas e senhas"""
    pessoas = []
    senhas = []
    with open(arquivo_senhas, 'r') as raw_arq:
        arq_senhas = csv.reader(raw_arq)
        for linha in arq_senhas:
            pessoas.append(linha[0])
            senhas.append(linha[1])
    return pessoas, senhas


def autentica(senha):
    """Verifica se a senha está cadastrada e retorna o nome da pessoa"""
    pessoas, senhas = le_arquivo_senhas()
    senha_criptografada = criptografa(senha)
    for i in range(len(senhas)):
        if senhas[i] == senha_criptografada:
            return pessoas[i]
    return False


def adiciona_usuario():
    """Adiciona um usuário ao arquivo de senhas"""
    pessoas, senhas = [], []
    with open(arquivo_senhas, 'r') as raw_arq:
        arq_senhas = csv.reader(raw_arq)
        for linha in arq_senhas:
            pessoas.append(linha[0])
            senhas.append(linha[1])

    print("Escreva o nome da pessoa a ser adicionada")
    nome = input()
    print("Escreva a senha no teclado numerico")
    senha = input()
    senha_criptografada = criptografa(senha)
    pessoas.append(nome)
    senhas.append(senha_criptografada)

    with open(arquivo_senhas, 'w') as raw_arq:
        for i in range(len(pessoas)):
            raw_arq.write(f"{pessoas[i]},{senhas[i]}\n")


def da_boas_vindas(nome):
    """Mensagem de boas-vindas no LCD"""
    global myLcd
    if myLcd:
        myLcd.clear()
        string_tela = "Ola " + nome.split(' ')[0]
        myLcd.write(string_tela)


def solicita_senha():
    """Solicita senha no LCD"""
    global myLcd
    if myLcd:
        myLcd.clear()
        myLcd.setCursor(0, 0)
        myLcd.write('Escreva a senha')
        myLcd.setCursor(1, 0)
        myLcd.write('e aperte Enter:')


def le_teclado():
    """Lê teclado numerico (simulação com input)"""
    teclado = input()
    lendo = True
    linha = ''
    while lendo:
        linha += str(teclado)
        if len(linha) >= 14 and linha[-1] == 'X':
            lendo = False
    return linha


def alerta_pessoa_nao_encontrada():
    global myLcd
    if myLcd:
        myLcd.clear()
        sleep(0.1)
        myLcd.write("Senha nao existe")


def alerta_travamento_sistema():
    global myLcd
    if myLcd:
        myLcd.setColor(255, 0, 0)
        myLcd.clear()
        myLcd.write('Travando sistema')


def inicializa_LCD():
    """Inicializa o LCD e define a variável global"""
    global myLcd
    # myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)  # Descomente se tiver LCD
    myLcd = None  # Placeholder para evitar erros
    if myLcd:
        myLcd.setCursor(0, 0)
        myLcd.setColor(53, 39, 249)
        myLcd.displayOff()
        sleep(1)
        myLcd.displayOn()
    return myLcd


def informa_tempo_restante(tempo):
    global myLcd
    if myLcd:
        myLcd.clear()
        myLcd.write('Tempo restante:')
        myLcd.setCursor(1, 0)
        myLcd.write(str(tempo))
        sleep(1)


def reseta_LCD():
    global myLcd
    if myLcd:
        myLcd.setColor(53, 39, 249)

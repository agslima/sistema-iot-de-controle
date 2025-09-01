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

import hashlib
import csv
from time import sleep
from datetime import datetime
# import mraa
# import pifacedigitalio
# import pyupm_i2clcd as lcd

# relay_gpio = 22 #Pino que esta conectado o relay
# relay = mraa.Gpio(relay_gpio) #Cria objeto relay com base no pino do relay
# relay.dir(mraa.DIR_OUT) #Define que o pino do relay eh output

pasta_padrao = ''  # Diretorio em que se encontra os scripts e dados do sistema
# Nome do arquivo que armazena o Hash das senhas junto com o nome do
# portador da senha
arquivo_senhas = pasta_padrao + 'passwords.csv'

####################### FUNCOES #########################

# Abre a porta do laboratorio
# def abre_porta():
#   toggle()


# Ativa e desativa o relay rapidamente, criando um pulso
# def toggle():
# pfd = pifacedigitalio.PiFaceDigital()
# pfd.relays[0].value = 1
# sleep(0.1) #(0.1)
# pfd.relays[0].value = 0


# Recebe uma senha e retorna o hash dela em MD5
def criptografa(senha):
    # m = hashlib.md5()
    # m.update(senha.encode())
    # return m.hexdigest()
    h = hashlib.md5(senha.encode())
    h2 = h.hexdigest()
    return h2


# Le o arquivo de senhas, e retorna a lista de pessoas e a lista de senhas
def le_arquivo_senhas():
    pessoas = []  # Inicializa lista de pessoas
    senhas = []  # Inicializa lista de senhas
    with open(arquivo_senhas, 'r') as raw_arq:
        # abre o arquivo csv com nomes e senhas
        arq_senhas = csv.reader(raw_arq)
        for linha in arq_senhas:  # percorre o arquivo de pessoas e coloca os dados numa lista
            pessoas.append(linha[0])
            senhas.append(linha[1])
        return (pessoas, senhas)


# Verifica se a senha esta cadastrada, e se sim, retorna qual a pessoa da senha
def autentica(senha):
    pessoas, senhas = le_arquivo_senhas()
    senha_criptografada = criptografa(senha)
    for i in range(len(senhas)):
        if senhas[i] == senha_criptografada:
            return pessoas[i]  # Retorna o nome da pessoa
    return False  # Retorna que nao encontrou ninguem


def adiciona_usuario():
    arq_senhas = []  # Garante que arq_senhas exista
    with open(arquivo_senhas, 'r') as raw_arq:
        # abre o arquivo csv com nomes e senhas
        arq_senhas = csv.reader(raw_arq)
        pessoas = []
        senhas = []
        for linha in arq_senhas:  # percorre o arquivo de pessoas e coloca os dados numa lista
            pessoas.append(linha[0])
            senhas.append(linha[1])
        print("Escreva o nome da pessoa a ser adicionada")
        nome = input()  # raw_input()
        print("Escreva a senha no teclado numerico")
        senha = input()  # le_teclado()
        senha_criptografada = criptografa(senha)
        pessoas.append(nome)
        senhas.append(senha_criptografada)
        with open('passwords.csv', 'w') as raw_arq:
            for i in range(len(pessoas)):
                raw_arq.write(pessoas[i] + ',' + senhas[i] + '\n')


# Escreve uma mensagem de boas vindas no LCD com o primeiro nome da pessoa
def da_boas_vindas(nome):
    myLcd.clear()
    string_tela = "Ola " + nome.split(' ')[0]
    myLcd.write(string_tela)


# Escreve uma solicitacao de senha para o usuario
def solicita_senha():
    myLcd.clear()
    myLcd.setCursor(0, 0)
    myLcd.write('Escreva a senha')
    myLcd.setCursor(1, 0)
    myLcd.write('e aperte Enter:')


# Retorna a escrita do teclado, e escreve no LCD o numero de digitos apertados
def le_teclado():
    # open('/dev/hidraw0') #O teclado sempre se encontra nessa porta serial
    teclado = raw_input()
    lendo = True
    apagado = False
    linha = ''
    while lendo:
        linha = linha + str(teclado.read(1))
        tam = len(linha) // 40
        if linha:
            if not apagado:
                # myLcd.clear()
                apagado = True
            if len(linha) >= 14:
                if linha[len(linha) - 14] == 'X':  # caracteristica do enter
                    lendo = False
        # myLcd.setCursor(0,0)
        for j in range(tam):
            print('*')
            # myLcd.write('*')
    teclado.close()
    return str(linha)


def alerta_pessoa_nao_encontrada():
    myLcd.clear()
    sleep(0.1)
    myLcd.write("Senha nao existe")


def alerta_travamento_sistema():
    myLcd.setColor(255, 0, 0)
    myLcd.clear()
    myLcd.write('Travando sistema')


def inicializa_LCD():
    sleep(5)
    myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)  # Inicializo o lcd na variavel myLcd
    myLcd.setCursor(0, 0)  # seta a posicao inicial do cursor
    myLcd.setColor(53, 39, 249)  # cor de fundo em RGB
    myLcd.displayOff()
    sleep(1)
    myLcd.displayOn()
    return myLcd


def informa_tempo_restante(tempo):
    myLcd.clear()
    myLcd.write('Tempo restante:')
    myLcd.setCursor(1, 0)
    myLcd.write(str(tempo))
    sleep(1)


def reseta_LCD():
    myLcd.setColor(53, 39, 249)  # cor de fundo em RGB

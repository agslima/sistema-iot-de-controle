# !/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Sistema IoT de controle de acesso com senha
# main_system: Código principal do Sistema de controle
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

from function import *

# DEFINICOES

ERRO_LIMIT = 3  # Numero de tentativas permitidas antes de travar o sistema
ERRO_TIME = 60  # Tempo inicial em que o sistema ficarah travado

# MAIN

print('Inicio do Sistema.')
erro = 0
bloqueado = False
contador = 0
# solicita_senha()
while True:
    if not bloqueado:
        print('escreva a senha')
        senha = input()  # le_teclado()
        pessoa = autentica(senha)
        if pessoa:
            erro = 0
            print('Bem vindo: ' + str(pessoa))
            # abre_porta()
        else:
            erro += 1
            print('Senha incorreta')
            # alerta_pessoa_nao_encontrada()
        if erro >= ERRO_LIMIT:
            bloqueado = True
            contador = ERRO_TIME
            print('Sistema travado')
            # alerta_travamento_sistema()
        sleep(3)
    else:
        # informa_tempo_restante(contador)
        contador -= 1
        if contador <= 0:
            bloqueado = False
            # reseta_LCD()

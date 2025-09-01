<!--
[![license](https://img.shields.io/github/license/agslima/Sistema-IoT-de-Controle?style=flat-square)](https://raw.githubusercontent.com/agslima/Sistema-IoT-de-Controle/master/LICENSE)

# Sistema de Controle IoT

Sistema para controle de entrada e saída de usuário, implementado em RaspberryPi com conceitos em IoT.

O objetivo do mini sistema é a criação e identificação do usuário com senhas criptografadas. O mini sistema é escrito com linguagem Python, usando e usada criptografia MD5 para salvar os usuários e senhas em um arquivo CSV.

### Sistema
O mini sistema tem os seguintes scripts em python:

- main_system.py Contém a main do sistema, ou seja, é o script principal do sistema.
- function.py: contém todas as funções do sistema; para mais detalhes, leia a parte de
documentação das funções.
- add_user.py: contém a funcionalidade de inserir ou deletar usuários no sistema.
- bad_password.py: script com a funcionalidade de criar senhas quem não devem ser usadas ao criar um novo usuário.

### Bibliotecas
Bibliotecas usadas:

https://github.com/intel-iot-devkit/mraa/blob/master/docs/building.md

https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison/all
-->

# Sistema de Controle IoT
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![CSV](https://img.shields.io/badge/Data-CSV-yellow?style=flat-square&logo=filezilla&logoColor=white)]()
[![Criptografia](https://img.shields.io/badge/Hash-MD5-critical?style=flat-square&logo=lock&logoColor=white)](https://en.wikipedia.org/wiki/MD5)
[![Raspberry Pi](https://img.shields.io/badge/Hardware-Raspberry%20Pi-C51A4A?style=flat-square&logo=raspberry-pi&logoColor=white)](https://www.raspberrypi.com/)
[![license](https://img.shields.io/github/license/agslima/Sistema-IoT-de-Controle?style=flat-square)](https://raw.githubusercontent.com/agslima/Sistema-IoT-de-Controle/master/LICENSE)

Sistema simples para controle de **entrada e saída de usuários**, implementado em **Raspberry Pi** com conceitos de **IoT** e **criptografia**.


### Objetivo

Desenvolver um mini sistema capaz de:

- Identificar usuários via senha criptografada
- Gerenciar permissões de entrada/saída
- Armazenar dados localmente em formato `.csv`
- Executar em dispositivos de baixo custo com Linux embarcado

> O projeto utiliza **criptografia MD5** para proteger senhas de usuários e permite operações básicas de administração.


### Scripts principais

O sistema é dividido em diferentes scripts Python, cada um com sua responsabilidade:

| Script             | Função principal                                                |
|--------------------|------------------------------------------------------------------|
| `main_system.py`   | Script principal — entrada do sistema (controle geral)          |
| `function.py`      | Conjunto de funções que implementam a lógica de autenticação    |
| `add_user.py`      | Adição e remoção de usuários no sistema                         |
| `bad_password.py`  | Lista de senhas inseguras para evitar durante cadastro          |


### Segurança

- As senhas são armazenadas com **hash MD5**
- O sistema rejeita senhas inseguras usando uma blacklist (`bad_password.py`)


### Estrutura de Dados

Usuários são armazenados em um arquivo CSV, com estrutura semelhante a:

```csv
nome,senha_md5
joao,e99a18c428cb38d5f260853678922e03
```

### Tecnologias e Bibliotecas

Este projeto utiliza as seguintes tecnologias e bibliotecas:

- Python3
- Criptografia MD5 (usando hashlib)
- CSV (armazenamento de dados)
- Raspberry Pi
- MRAA (biblioteca para interação com GPIO e sensores)

### Referências:

[Intel IoT DevKit – MRAA Build Docs](https://github.com/intel-iot-devkit/mraa/blob/master/docs/building.md)

[SparkFun - Instalação MRAA](https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison/all)



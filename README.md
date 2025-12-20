# IoT Access Control System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-C51A4A?style=flat-square&logo=raspberry-pi&logoColor=white)
![Security](https://img.shields.io/badge/Security-MD5%20Hashing-critical?style=flat-square&logo=lock&logoColor=white)
![License](https://img.shields.io/github/license/agslima/Sistema-IoT-de-Controle?style=flat-square)

A lightweight **User Entry/Exit Control System** developed for embedded Linux environments (specifically **Raspberry Pi**). This project demonstrates core IoT concepts, hardware interaction via GPIO, and basic cryptographic security practices.

---

## How to run this? 🚀

**Clone the repository:**

```bash
git clone [https://github.com/agslima/Sistema-IoT-de-Controle.git](https://github.com/agslima/Sistema-IoT-de-Controle.git)
cd Sistema-IoT-de-Controle
```

**Add a new user:**

```bash
python3 add_user.py
```

**Follow the on-screen prompts to set a username and secure password**

```bash
Run the main system:
python3 main_system.py
```

## 📋 Project Overview

The primary goal of this system is to manage user authentication and access control in a physical environment. It simulates a secure gatekeeper system where:

* Users are identified via credentials.
* Passwords are stored securely using **MD5 hashing**.
* User data is persisted locally in a **CSV database**.
* Hardware interaction is handled via the **MRAA library**.

> **Note:** This project focuses on the *implementation of logic and hardware integration*. While MD5 is used here for educational demonstration of hashing concepts, modern production environments should utilize stronger algorithms (e.g., SHA-256 or bcrypt).

---

## 📂 Project Structure

The codebase is modularized to separate core logic, user management, and security validation.

| File | Description |
| :--- | :--- |
| `main_system.py` | **Entry Point:** The main execution loop that handles the system state and hardware signals. |
| `function.py` | **Core Logic:** Contains reusable functions for authentication and data processing. |
| `add_user.py` | **Admin Tool:** Script to register new users or remove existing ones from the database. |
| `bad_password.py` | **Security:** Implements a blacklist validation to prevent users from choosing weak passwords. |

---

## 💾 Data Storage

User credentials are stored in a local `.csv` file to ensure persistence without requiring a heavy SQL database engine.

**Format Structure:**
```csv
username,password_hash
john_doe,e99a18c428cb38d5f260853678922e03
alice,5f4dcc3b5aa765d61d8327deb882cf99
```

## Tech Stack & Dependencies 🛠️

 * Hardware: Raspberry Pi (or Intel Edison/Galileo compatible boards)
 * Language: Python 3
 * Libraries:
   * hashlib (Standard Python lib for MD5)
   * csv (Standard Python lib for storage)
   * mraa (Low Level Skeleton Library for Communication on GNU/Linux platforms)

> [!NOTE]
> **References & Documentation**
> This project relies on libmraa for GPIO communication (reading sensors/controlling actuators).
> * Intel IoT DevKit – MRAA Build Documentation
> * SparkFun - Installing libmraa

---

## License
This project is licensed under the MIT License - see the LICENSE file for details.



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
-->




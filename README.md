# IoT Access Control System

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=flat-square&logo=python&logoColor=white)
![Platform](https://img.shields.io/badge/Platform-Raspberry%20Pi-C51A4A?style=flat-square&logo=raspberry-pi&logoColor=white)
![License](https://img.shields.io/github/license/agslima/Sistema-IoT-de-Controle?style=flat-square)

A lightweight **User Entry/Exit Control System** developed for embedded Linux environments (specifically **Raspberry Pi**). This project demonstrates core IoT concepts, hardware interaction via GPIO, and basic cryptographic security practices.

## TL;DR

> A Python-based embedded access control system that:
> * Authenticates users locally
> * Controls physical access via GPIO
> * Stores credentials in a lightweight CSV database
> * Demonstrates hashing concepts and IoT hardware integration

> [warning]
> Educational project — not production-ready security.
---

## How to run this? 🚀

**Clone the repository:**

```bash
git clone https://github.com/agslima/Sistema-IoT-de-Controle.git
cd Sistema-IoT-de-Controle
```

**Add a new user:**

```bash
python3 add_user.py
```

Follow the prompts to define:
* Username
* Password (validated against a weak-password blacklist)

**Run the main system:**

```bash
python3 main_system.py
```

## 📋 Project Overview

The primary goal of this system is to manage user authentication and access control in a physical environment. It simulates a secure gatekeeper system where:

* Users are identified via credentials.
* Passwords are stored securely using **MD5 hashing**.
* User data is persisted locally in a **CSV database**.
* Hardware interaction is handled via the **MRAA library**.

> [warning]
> This project focuses on the *implementation of logic and hardware integration*. While MD5 is used here for educational demonstration of hashing concepts, modern production environments should utilize stronger algorithms (e.g., SHA-256 or bcrypt).

---

## Project Structure 📂

The codebase is modularized to separate core logic, user management, and security validation.

| File | Description |
| :--- | :--- |
| `main_system.py` | **Entry Point:** The main execution loop that handles the system state and hardware signals. |
| `function.py` | **Core Logic:** Contains reusable functions for authentication and data processing. |
| `add_user.py` | **Admin Tool:** Script to register new users or remove existing ones from the database. |
| `bad_password.py` | **Security:** Implements a blacklist validation to prevent users from choosing weak passwords. |

---

## Data Storage 💾

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
   * `hashlib` (Standard Python lib for MD5)
   * `csv` (Standard Python lib for storage)
   * `mraa` (Low Level Skeleton Library for Communication on GNU/Linux platforms)

## Limitations & Non-Goals 🚧

This project intentionally does not include:

* Network-based authentication
* Remote management
* Encryption at rest
* Role-based access control
* Audit or event logs

## References & Documentation 📚

This project relies on libmraa for GPIO communication (reading sensors/controlling actuators).
* [Intel IoT DevKit – MRAA Build Docs](https://github.com/intel-iot-devkit/mraa/blob/master/docs/building.md)
* [SparkFun - Instalação MRAA](https://learn.sparkfun.com/tutorials/installing-libmraa-on-ubilinux-for-edison/all)

---

## License
This project is licensed under the **GPLv3 License**.
See the LICENSE file for details.

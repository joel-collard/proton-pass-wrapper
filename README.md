# 🔐 **Proton Pass Wrapper**  

**Proton Pass Wrapper** is a lightweight, cross-platform Python library that provides a seamless interface for Proton Pass CLI. It enables easy, private, and secure access to your vaults, in **local or headless environments**, allowing you to **retrieve and inject secrets programmatically** while keeping them out of your source code. Designed for versatility, it works out-of-the-box on Windows, macOS, and Linux.

1. [Why Proton Pass Wrapper?](#1--why-proton-pass-wrapper)
2. [API Reference](#2--api-reference)
3. [Installation & Usage](#3-%EF%B8%8F-installation--usage)
4. [Repository Structure](#4--repository-structure)
5. [License & Contact](#5--license--contact)

<br>

---

## 1. 🎯 Why Proton Pass Wrapper?

Developers often need to pull secrets like credentials for program automation (e.g., CI/CD, bots, local scripts), but manually managing **Proton Pass** in the CLI can be clunky for automated workflows. This library solves that by providing:
- ⚡ **Effortless Discovery:** Programmatically list vaults, items, and fields without ever touching the terminal.
- 🛡️ **Secret Injection:** Fetch secrets like passwords and API keys directly into variables with auto-wiping memory management, keeping sensitive info out of your source code and files.
- 🤖 **Headless Integration:** Power background tasks, Docker containers, and CI/CD pipelines without manual logins—enabling true 24/7 "set-and-forget" secret management.
- 🪶 **Native & Universal:** A lightweight zero-dependency Python wrapper that works anywhere the CLI works—Windows, macOS, and Linux.
- 🔄 **Lifecycle Management:** Built-in status checks, automated login, and secure logout for smooth, uninterrupted, and reliable execution.

<br>

---

## 2. 🚀 API Reference

| Function | Key Feature | Description |
| :--- | :--- | :--- |
| `path(path)` | Environment Setup | Configures the absolute *path* to your `proton-pass-cli` binary (Defaults to auto-detect). |
| `status()` | Session Status | Returns `True` if authenticated, `False` if authentication is required. |
| `authenticate()` | Session Authentication | Triggers the secure browser-based login flow. |
| `vaults()` | Vault Discovery | Lists all available vaults. |
| `items(vault)` | Item Discovery | Lists all items within a specific *vault*. |
| `fields(vault, item)` | Field Discovery | Lists all fields for a specific *vault* and *item*. |
| `secret(vault, item, field)` | Standard Retrieval | Fetches a *field* secret (e.g., password, username) from a chosen *vault* and *item*. |
| `inject(vault, item, field)` | Secure Retrieval | Securely handles a *field* secret from a chosen *vault* and *item* within a block, clearing it from memory after execution. |
| `terminate()` | Session Termination | Terminates the current session and clears local authentication. |

**Note:** This library supports the use of both names and IDs for vaults and items. For more information on underlying CLI capabilities, refer to the [Official Proton Pass CLI Documentation](https://protonpass.github.io/pass-cli/).

<br>

---

## 3. 🛠️ Installation & Usage

**Prerequisites**

Before installing, ensure you have [Python 3.8+](https://www.python.org/) and [Proton Pass CLI](https://protonpass.github.io/pass-cli/) set up.

**Installation**

```bash
# Install library
pip install proton-pass-wrapper

# Diagnostic check
python -m proton_pass_wrapper --diagnose
```

**Usage in Python**

```python
import proton_pass_wrapper as ppw

# Quick reference API documentation
# help(ppw)

# 1️⃣ Setup Session
ppw.path()
if not ppw.status():
    ppw.authenticate()

# 2️⃣ Discover vaults, items, and fields
print(ppw.vaults())
# print(ppw.items("Personal Vault"))
# print(ppw.fields("Personal Vault", "Service Account"))

# 3️⃣ Standard Retrieval (example using vault and item names)
# account_username = ppw.secret("Personal Vault", "Service Account", "username")
# account_password = ppw.secret("Personal Vault", "Service Account", "password")

# 4️⃣ Secure Retrieval (example using vault and item IDs, clears from memory after execution)
# with (ppw.inject("R1x4T7P0w3...J8u==", "n7_zP2mR1k...qT9==", "api key") as api_key,
    # ppw.inject("R1x4T7P0w3...H9x==", "HJ7N_Cgdq4...Vv6==", "secret") as api_secret):  
    # Securely inject secrets into your application or service in this code block

# 5️⃣ Terminate session
ppw.terminate()
```

<br>

---

## 4. 📁 Repository Structure

```plaintext
proton-pass-wrapper/
├── src/proton_pass_wrapper/
│   ├── __init__.py               # Public API entry
│   ├── core.py                   # Main wrapper logic
│   └── __main__.py               # CLI entry point
├── tests/                        
│   └── test_wrapper.py           # Logic verification
├── pyproject.toml                # Build system metadata
├── .gitignore                    # Version control exclusions
├── LICENSE                       # MIT usage terms
└── README.md                     # Documentation and guide
```

<br>

---

## 5. 📄 License & Contact

**License:** Free to use, modify, and distribute. See [MIT LICENSE](https://github.com/joel-collard/proton-pass-wrapper/blob/main/LICENSE).

**Contact:** For collaboration or issues, contact [Anonymous](mailto:gh.cyclic706@passmail.net).

<br>

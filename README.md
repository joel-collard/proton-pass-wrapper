# 🔐 **Proton Pass Wrapper**  

**Proton Pass Wrapper** is a lightweight, cross-platform Python library that provides a seamless interface for Proton Pass CLI. It enables easy, private, and secure access to your vaults, allowing you to **retrieve secrets programmatically** while keeping them out of your source code. Designed for versatility, it works out-of-the-box on Windows, macOS, and Linux.

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
- 🛡️ **Secret Injection:** Fetch secrets like passwords and API keys directly into variables, keeping sensitive info out of your source code and `.env` files.
- 🪶 **Native & Universal:** A lightweight zero-dependency wrapper that works anywhere the CLI works—Windows, macOS, and Linux.
- 🔄 **Lifecycle Management:** Built-in status checks, automated login, and secure logout for smooth, uninterrupted, and reliable execution.

<br>

---

## 2. 🚀 API Reference

| Function | Key Feature | Description |
| :--- | :--- | :--- |
| `protonpass_path(path)` | Environment Setup | Configures the absolute *path* to your `proton-pass-cli` binary. |
| `protonpass_status()` | Session Health | Returns `True` if authenticated, `False` if login is required. |
| `protonpass_login()` | Authentication | Triggers the secure browser-based login flow. |
| `protonpass_vaults()` | Vault Discovery | Lists all available vaults. |
| `protonpass_items(vault)` | Item Discovery | Lists all items within a specific *vault*. |
| `protonpass_fields(vault, item)` | Field Discovery | Lists all fields and details for a specific *vault* and *item*. |
| `protonpass_get(vault, item, field)` | Secret Retrievals | Fetches specific *field* data (e.g., password, username, etc.) from a specified *vault* and *item*. |
| `protonpass_logout()` | Session Security | Ends the current session and clears local authentication. |

**Note:** This library supports the use of both names and IDs for vaults and items. For a full list of underlying CLI capabilities, refer to the [Official Proton Pass CLI Documentation](https://protonpass.github.io/pass-cli/).

<br>

---

## 3. 🛠️ Installation & Usage

### Prerequisites
Before installing, ensure you have [Python 3.8+](https://www.python.org/) and [Proton Pass CLI](https://protonpass.github.io/pass-cli/) set up.

### Installation
```bash
# Install from PyPI
pip install proton-pass-wrapper
```

### Usage in Python
```python
# 1️⃣ Import functions
from proton_pass_wrapper import *

# 2️⃣ Configure path
protonpass_path("C:/Users/YourName/AppData/Local/Programs/ProtonPass/pass-cli.exe")

# 3️⃣ Check session
if not protonpass_status():
    protonpass_login()

# 4️⃣ Discover secrets
print(protonpass_vaults())
# print(protonpass_items("Personal Vault"))
# print(protonpass_fields("Personal Vault", "Service Account"))

# 5️⃣ Retrieve secrets
# client_id = protonpass_get("Personal Vault", "Service Account", "api key")
# client_secret = protonpass_get("n7_zP2mR1k...qT9==", "R1x4T7P0w3...J8u==", "secret")

# 6️⃣ Use secrets
# Securely inject secrets into your application, services, or
# automated workflows—eliminating sensitive info from your code.

# 7️⃣ Secure session
protonpass_logout()
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

**License:** MIT License – free to use, modify, and distribute. See `LICENSE`.

**Contact:** Anonymous – gh.cyclic706@passmail.net

<br>

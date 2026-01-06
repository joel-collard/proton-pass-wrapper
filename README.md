# 🔐 **Proton Pass Wrapper**  

**Proton Pass Wrapper** is a lightweight, cross-platform Python library that provides a seamless interface for Proton Pass CLI. It enables **easy, private, and secure access to your vaults**, allowing you to **retrieve secrets** programmatically while keeping sensitive information out of your source code. Designed for versatility, it works out-of-the-box on Windows, macOS, and Linux.

1. [Why Proton Pass Wrapper?](#1--why-proton-pass-wrapper)
2. [API Reference](#2--api-reference)
3. [Installation & Usage](#3-%EF%B8%8F-installation--usage)
4. [Repository Structure](#4--repository-structure)
5. [License & Contact](#5--license--contact)
<br>

## 1. 🎯 Why Proton Pass Wrapper?

Developers often need to pull secrets like credentials for automation (e.g., CI/CD, bots, local scripts), but manually managing the Proton Pass in the CLI can be clunky. This library solves that by providing:
- ⚡ **Effortless Discovery:** Programmatically list vaults, items, and fields to fetch what you need without ever touching the terminal.
- 🛡️ **Secret Injection:** Fetch secrets like passwords and API keys directly into variables, keeping sensitive info out of source code `.env` files.
- 🪶 **Lightweight & Native:** A lightweight zero-dependency wrapper that works anywhere the CLI works—Windows, macOS, and Linux.
- 🔄 **Lifecycle Management:** Built-in status checks, automated login, and secure logout handling for smooth uninterrupted execution.
<br>

## 2. 🚀 API Reference

| Function | Key Feature | Description |
| :--- | :--- | :--- |
| `protonpass_path(path)` | Environment Setup | Configures the absolute path to your `proton-pass-cli`. |
| `protonpass_status()` | Session Health | Returns `True` if connected and authenticated, `False` otherwise. |
| `protonpass_login()` | Authentication Management | Triggers the secure browser-based login flow when needed. |
| `protonpass_vaults()` | Vault Discovery | Ends the current session and clears local authentication. |
| `protonpass_items(vault)` | Item Discovery | Ends the current session and clears local authentication. |
| `protonpass_fields(vault,item)` | Field Discovery | Lists all available items within a specific vault or container. |
| `protonpass_get(vault,item,field)` | Secret Retrieval | Fetches specific data (e.g., password, username, etc.) from a vault and item names or IDs as well as fields. |
| `protonpass_logout()` | Session Security | Ends the current session and clears local authentication. |

**Note:** This library supports retrieval of fields visible in the Proton Pass UI (e.g., username, password, API Key). For a full list of CLI capabilities, refer to the [Official Proton Pass CLI Documentation](https://protonpass.github.io/pass-cli/).
<br>

## 3. 🛠️ Installation & Usage

### Prerequisites
Before installing, ensure you have **[Python 3.8+](https://www.python.org/)** and **[Proton Pass CLI](https://protonpass.github.io/pass-cli/)** set up.

### Installation
```bash
# Install from PyPI
pip install proton-pass-wrapper
```

### Usage in Python
```python
# 1️⃣ Import wrapper functions
from proton_pass_wrapper import *

# 2️⃣ Configure Proton Pass CLI path
protonpass_path("C:/Users/YourName/AppData/Local/Programs/ProtonPass/pass-cli.exe")

# 3️⃣ Check session, login as required
if not protonpass_status():
    protonpass_login()

# 4️⃣ Discover secrets
my_vaults = protonpass_vaults() 
# items = protonpass_items("Personal Vault")
# fields = protonpass_fields("Personal Vault", "Service Account")

# 5️⃣ Retrieve credentials using vault and item names or IDs as well as field
# client_id = protonpass_get("Personal Vault", "Service Account", "api key")
# client_secret = protonpass_get("n7_zP2mR1k...qT9==", "R1x4T7P0w3...J8u==", "secret")

# 6️⃣ Example initializing service integration keeping sensitive info out of source code
# client = MyServiceClient(api_key = client_id, api_secret = client_secret)
# client.connect()

# 7️⃣ Optional: Logout to secure the session
protonpass_logout()
```
<br>

## 4. 📁 Repository Structure

```plaintext
proton-pass-wrapper/
├── src/proton_pass_wrapper/
│   ├── __init__.py               # Public API entry
│   ├── core.py                   # Main wrapper logic
│   └── __main__.py               # CLI entry point
├── tests/                        
│   └── test_wrapper.py           # Logic verification scripts
├── pyproject.toml                # Build system metadata
├── .gitignore                    # Version control exclusions
├── LICENSE                       # MIT usage terms
└── README.md                     # Documentation and guide
```
<br>

## 5. 📄 License & Contact

**License:** MIT License – free to use, modify, and distribute. See `LICENSE`.

**Contact:** Anonymous – gh.cyclic706@passmail.net

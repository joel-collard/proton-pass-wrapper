# 🔐 **Proton Pass Wrapper**  

**Proton Pass Wrapper** is a lightweight, cross-platform Python library that provides a seamless interface for Proton Pass CLI. It enables **easy, private, and secure access to your vaults**, allowing you to **retrieve credentials** programmatically while keeping sensitive information out of your source code. Designed for versatility, it works out-of-the-box on Windows, macOS, and Linux.

## 📖 Table of Contents
1. [Why Proton Pass Wrapper?](#-why-proton-pass-wrapper)
2. [API Reference & Features](#-api-reference)
3. [Installation and Usage](#-installation--usage)
4. [Repository Structure](#-repository-structure)
5. [License & Contact](#-license--contact)

## 1. 🎯 Why Proton Pass Wrapper?
Developers often need to pull credentials for automation (CI/CD, bots, local scripts), but manually managing the **Proton Pass CLI** can be clunky. This library solves that by providing:
- ⚡ **Effortless Automation:** Programmatically fetch passwords, usernames, api keys, secrets, custom fields, and more without touching the terminal.
- 🛡️ **"Secret Injection" Pattern:** Keep sensitive credentials out of your source code and `.env` files.
- 🪶 **Lightweight & Native:** A zero-dependency wrapper that works anywhere the CLI works—**Windows, macOS, and Linux.**
- 🔄 **Session Resilience:** Built-in status checks and automated login handling for smooth execution.

## 2. 🚀 API Reference & Features

| Function | Key Feature | Description |
| :--- | :--- | :--- |
| `protonpass_path(path)` | Environment Setup | Configures the absolute path to your `pass-cli.exe`. |
| `protonpass_status()` | Session Health | Returns `True` if connected and authenticated, `False` otherwise. |
| `protonpass_login()` | Auth Management | Triggers the secure browser-based login flow when needed. |
| `protonpass_get(vault, item, field)` | Secret Retrieval | Fetches specific data (password, totp, etc.) from a vault and item names or IDs as well as fields|
| `protonpass_items()` | Vault Discovery | Lists all available items within a specific vault or container. |

**Note:** This library supports retrieval of fields visible in the Proton Pass UI (e.g., username, password, API Key). For a full list of CLI capabilities, refer to the [Official Proton Pass CLI Documentation](https://protonpass.github.io/pass-cli/).

## 3. 🛠️ Installation and Usage

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

# 4️⃣ Retrieve credentials using vault and item names or IDs as well as field
client_id = protonpass_get("Personal Vault", "Service Account", "api key")
client_secret = protonpass_get("n7_zP2mR1k_L9v4T0w3M6qK9zH2fW5cA8jB1k4mZ7v9nR1x4T7P0w3L-6K9M2Q5rJ8uD1yS4oV7eX0iG3pN6qT9==", "R1x4T7P0w3L6K9-M2Q5rJ8uD1yS4oV7eX0iG3pN6qT9zH2fW5cA8jB1k4m_Z7v9nR1x4T7P0w3L6K9M2Q5r_J8u==", "secret")

# 5️⃣ Initialize service integration keeping sensitive info out of source code
# client = MyServiceClient(api_key = client_id, api_secret = client_secret)
# client.connect()
```

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

## 5. 📄 License & Contact
**License:** MIT License – free to use, modify, and distribute. See `LICENSE`.

**Contact:** Anonymous – joel.collard@mail.mcgill.ca

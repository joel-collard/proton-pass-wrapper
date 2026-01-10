"""
🔐 Proton Pass Wrapper is a lightweight, cross-platform Python library that provides a seamless interface for Proton Pass CLI. 
It enables easy, private, and secure access to your vaults, in local or headless environments, allowing you to retrieve and inject secrets 
programmatically while keeping them out of your source code. Designed for versatility, it works out-of-the-box on Windows, macOS, and Linux.

📄 Techincal reference: https://github.com/joel-collard/proton-pass-wrapper
"""

# 1. Import functions from core.py to make them accessible at the top level
from .core import (
    protonpass_path,
    protonpass_status,
    protonpass_login,
    protonpass_vaults,
    protonpass_items,
    protonpass_fields,
    protonpass_get,
    protonpass_logout
)

# 2. Define metadata
__version__ = "0.1.0"

# 3. Define __all__ to control what 'from proton_pass_wrapper import *' exposes
__all__ = [
    "protonpass_path",
    "protonpass_status",
    "protonpass_login",
    "protonpass_vaults",
    "protonpass_items",
    "protonpass_fields",
    "protonpass_get",
    "protonpass_logout"
]

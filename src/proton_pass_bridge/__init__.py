"""
🔐 Proton Pass Bridge: A secure Python bridge for Proton Pass CLI.

This library provides a lightweight, cross-platform interface for
Proton Pass CLI. It enables easy, private, and secure access to 
your vaults, allowing you to inject secrets programmatically.

An independent community bridge for Proton Pass. Not an official 
Proton AG product.

🛡️ Bridge check: $ python -m proton_pass_bridge --check
📄 Documentation: https://github.com/joel-collard/proton-pass-bridge
"""

# 1. Define metadata
__version__ = "0.1.0"
__author__ = "stealthcode847"
__license__ = "MIT"
__alias__ = "ppb"

# 2. Import functions to library namespace
from .core import (
    path,
    status,
    authenticate,
    vaults,
    items,
    fields,
    secret,
    inject,
    terminate
)

# 3. Define public functions for library namespace
__all__ = [
    "path",
    "status",
    "authenticate",
    "vaults",
    "items",
    "fields",
    "secret",
    "inject",
    "terminate"
]

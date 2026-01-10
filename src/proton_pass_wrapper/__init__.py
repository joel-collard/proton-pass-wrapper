"""
🔐 Proton Pass Wrapper: A secure Python bridge for the Proton Pass CLI.
------------------------------------------------------------------------

This library provides a lightweight, cross-platform interface for the 
Proton Pass CLI. It enables easy, private, and secure access to your 
vaults in local or headless environments, allowing you to retrieve 
and inject secrets programmatically.

🔎 Environment check: $ python -m proton_pass_wrapper --check

📄 Technical reference: https://github.com/joel-collard/proton-pass-wrapper
"""

# 1. Import functions to library namespace
from .core import (
    protonpass_path,
    protonpass_status,
    protonpass_authenticate,
    protonpass_vaults,
    protonpass_items,
    protonpass_fields,
    protonpass_secret,
    protonpass_inject,
    protonpass_terminate
)

# 2. Define metadata
__version__ = "0.1.0"

# 3. Define public functions for library namespace
__all__ = [
    "protonpass_path",
    "protonpass_status",
    "protonpass_authenticate",
    "protonpass_vaults",
    "protonpass_items",
    "protonpass_fields",
    "protonpass_secret",
    "protonpass_inject",
    "protonpass_terminate"
]

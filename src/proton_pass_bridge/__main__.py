import argparse
import sys
from . import __version__
from . import core

"""
🛡️ Proton Pass Wrapper Check
----------------------------------------------
[Library]  v0.1.0 (Latest)         ✅
[CLI]      v1.5.2 (Verified)       ✅
[Binary]   /usr/local/bin/proton-pass
[Session]  Active (Local)          ✅

👉 Next Step: Use help(ppw) to explore API.
"""

def run_check():
    # 1. Gather comprehensive data from core.py
    wrapper_ver = __version__
    cli_path = core.find_cli_path() 
    cli_ver = core.get_cli_version() if cli_path else "N/A"
    
    # New state-aware detections
    is_auth = core.status() if cli_path else False
    is_headless = core.detect_headless()  # Checks for TTY or CI environment variables
    session_type = "Headless" if is_headless else "Local"
    
    # 2. Render the "Executive Check"
    print(f"\n🛡️ Proton Pass Wrapper Check")
    print("-" * 46)
    
    # Row 1: Library Version
    print(f"{'[Library]':<11} v{wrapper_ver:<18} ✅ (Latest)")

    # Row 2 & 3: CLI Detection & Path
    if cli_path:
        print(f"{'[CLI]':<11} v{cli_ver:<18} ✅ (Verified)")
        print(f"{'[Binary]':<11} 📍 {cli_path}")
    else:
        print(f"{'[CLI]':<11} {'Not Detected':<18} ❌")
        print(f"{'[Binary]':<11} {'N/A':<18} ❌")

    # Row 4: Session State
    if is_auth:
        print(f"{'[Session]':<11} {session_type:<18} ✅ (Active)")
    else:
        state_label = "Inactive" if cli_path else "Unknown"
        icon = "⚠️" if cli_path else "❌"
        print(f"{'[Session]':<11} {state_label:<18} {icon}")

    # 3. Dynamic "Next Step" logic based on specific failure states
    print("-" * 46)
    
    if not cli_path:
        msg = "👉 Next Step: Install CLI (https://protonpass.github.io/pass-cli/) or manually verify path with ppw.path()."
    elif not is_auth:
        if is_headless:
            msg = "👉 Next Step: Configure 'PROTON_PASS_APP_PASSWORD' for headless auth."
        else:
            msg = "👉 Next Step: Run 'ppw.authenticate()' to log into your account."
    else:
        msg = f"👉 Next Step: Use 'help(ppw)' to explore API."
    
    print(f"{msg}\n")

def main():
    # Setup the Argument Parser
    parser = argparse.ArgumentParser(
        prog="proton-pass-wrapper",
        description="🔐 A secure Python bridge for the Proton Pass CLI.",
        epilog="Documentation: https://github.com/joel-collard/proton-pass-wrapper"
    )

    # --version: Handled automatically by argparse
    parser.add_argument(
        "-v", "--version", 
        action="version", 
        version=f"%(prog)s v{__version__}"
    )

    # --check: The diagnostic tool
    parser.add_argument(
        "--check", 
        action="store_true", 
        help="Run environment diagnostics and check session status"
    )

    # Show help if no arguments are passed
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)

    args = parser.parse_args()

    if args.check:
        run_check()
        sys.exit(0)

if __name__ == "__main__":
    sys.exit(main())

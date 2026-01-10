## TO DO
## Check Wrapper Version
## Check CLI Version
## Check Authentication


import argparse
import sys
from . import __version__
from . import core

def run_check():
    """
    Executes the diagnostic health check.
    This coordinates the logic from core.py to present a clean report.
    """
    print(f"\n🔍 {core.BOLD}Proton Pass Wrapper: Environment Check{core.END}")
    print("-" * 45)
    
    # 1. Check Wrapper Version
    print(f"Proton Pass Wrapper Version:    v{__version__}")
    
    # 2. Check CLI Path (Calling the logic we will build in core.py)
    cli_path = core.find_cli_path()
    if cli_path:
        print(f"Proton Pass CLI Path:    {cli_path} ✅")
        
        # 3. Check CLI Version
        cli_ver = core.get_cli_version()
        print(f"Proton Pass CLI Version: {cli_ver} ✅")
        
        # 4. Check Auth Status
        if core.status():
            print(f"Session Status:     Authenticated 🔐")
        else:
            print(f"Session Status:     Authentication Required ⚠️")
            print(f"\n💡 Run 'ppw.authenticate()' in Python to log in.")
    else:
        print(f"Proton CLI Path:    Not Found ❌")
        print(f"\n❗ Ensure Proton Pass CLI is installed and in your PATH.")
        print(f"Visit: https://protonpass.github.io/pass-cli/")

    print("-" * 45 + "\n")

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

import argparse
import json
from va import Vuln
from cvss_calc import assess_cvss
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

ORANGE = '\033[38;5;214m'  # Orange color
RESET = '\033[0m'  # Reset color
DARK_MAGENTA = '\033[38;5;125m'


def print_logo():
    logo = f"""
{ORANGE}
                                          
      __     ___    ______     ______ ______  __
      \\ \\   / / \\  / ___\\ \\   / / ___/ ___\\ \\/ /  
       \\ \\ / / _ \\| |    \\ \\ / /\\___ \\___ \\\\  /   
        \\ V / ___ | |___  \\ V /  ___) ___) /  \\   
         \\_/ /   \\_\\____|  \\_/  |____|____/_/\\_\\                                       
{RESET}
    """
    info = f"""
\033[1;34m
\033[0;32mProject Name:\033[0m {ORANGE}Vacvssx{RESET}
\033[0;32mAuthor:\033[0m \033[33mSudhan\033[0m
\033[0;32mDescription:\033[0m \033[38;5;30mVulnerability Assessment and CVSS Scoring Tool
\033[0m
    """
    print(logo)
    print(info)


# Load vulnerabilities from the file
def load_vuln():
    with open('default_vuln.json', 'r') as f:
        return json.load(f)


def main():
    # Print logo and information
    print_logo()

    # Load default vulnerabilities
    default_vulns = load_vuln()

    # Parse arguments
    parser = argparse.ArgumentParser(description=f"{DARK_MAGENTA}Vulnerability Assessment Tool{RESET}")

    parser.add_argument('--use-default', action='store_true', help=f"Use a default vulnerability from the list")
    parser.add_argument('--id', help=f"Vulnerability ID (ignored if using default)")
    parser.add_argument('--description', help=f"Description of the vulnerability (ignored if using default)")
    parser.add_argument('--impact', type=float, help=f"Impact score (0-10, ignored if using default)")
    parser.add_argument('--exploitability', type=float, help=f"Exploitability score (0-10, ignored if using default)")

    args = parser.parse_args()

    if args.use_default:
        print(f"\n{Fore.GREEN}Select a default vulnerability from the list:{Style.RESET_ALL}")
        for i, vuln in enumerate(default_vulns):
            print(f"{Fore.LIGHTBLUE_EX}[{i}] {vuln['id']}: {vuln['description']}{Style.RESET_ALL}")

        # Users to select a vulnerability
        try:
            index = int(input(f"{Fore.YELLOW}Enter the index of the vulnerability: {Style.RESET_ALL}"))
            if index < 0 or index >= len(default_vulns):
                print(f"{Fore.RED}Invalid index. Please select a valid vulnerability.{Style.RESET_ALL}")
                return
            selected_vuln = default_vulns[index]
        except ValueError:
            print(f"{Fore.RED}Please enter a valid integer index.{Style.RESET_ALL}")
            return

        vulnerability = Vuln(
            selected_vuln['id'],
            selected_vuln['description'],
            selected_vuln['impact'],
            selected_vuln['exploitability']
        )
    else:
        if not (args.id and args.description and args.impact and args.exploitability):
            print(f"{Fore.RED}Please provide --id, --description, --impact, and --exploitability or use --use-default.{Style.RESET_ALL}")
            return

        vulnerability = Vuln(
            args.id, args.description, args.impact, args.exploitability
        )

    print(f"{Fore.GREEN}\nCreating vulnerability assessment...{Style.RESET_ALL}")
    vulnerability.display()

    # Calculate CVSS score
    cvss_score = assess_cvss(vulnerability)
    print(f"\n{Fore.LIGHTBLUE_EX}Calculated CVSS Score: {Fore.RED}{cvss_score:.2f}{Style.RESET_ALL}")


if __name__ == "__main__":
    main()

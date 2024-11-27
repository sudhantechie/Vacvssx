from colorama import Fore, Style

class Vuln:
    def __init__(self, id, description, impact, exploitability):
        self.id = id
        self.description = description
        self.impact = impact
        self.exploitability = exploitability

    def display(self):
        print(f"{Fore.MAGENTA}Vulnerability Details:{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}ID: {self.id}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Description: {self.description}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Impact: {self.impact}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Exploitability: {self.exploitability}{Style.RESET_ALL}")

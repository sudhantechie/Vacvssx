# Vulnerability Assessment and CVSS Scoring Tool

This tool allows users to calculate the CVSS score using a command-line interface (CLI).

Requirements
~~~~~~~~~~~~

- `argparse`
- `json`
- `colorama`




Download/Installation
~~~~~~~~~~~~~~~~~~~~~

* git clone 
* cd vacvssx https://github.com/sudhantechie/Vacvssx.git
* pip install -r requirements.txt

Usage
~~~~~
```

      __     ___    ______     ______ ______  __
      \ \   / / \  / ___\ \   / / ___/ ___\ \/ /
       \ \ / / _ \| |    \ \ / /\___ \___ \\  /
        \ V / ___ | |___  \ V /  ___) ___) /  \
         \_/_/   \_\____|  \_/  |____|____/_/\_\



Project: Vacvssx
Author: Sudhan
Description: Vulnerability Assessment and CVSS Scoring Tool


usage: vacvssx.py [-h] [--use-default] [--id ID] [--description DESCRIPTION] [--impact IMPACT]
                  [--exploitability EXPLOITABILITY]

Vulnerability Assessment Tool

options:
  -h, --help            show this help message and exit
  --use-default         Use a default vulnerability from the list
  --id ID               Vulnerability ID (ignored if using default)
  --description DESCRIPTION
                        Description of the vulnerability (ignored if using default)
  --impact IMPACT       Impact score (0-10, ignored if using default)
  --exploitability EXPLOITABILITY
                        Exploitability score (0-10, ignored if using default)
```

Examples
~~~~~~~~


1. **Using a Default Vulnerability:**

  This command uses a default vulnerability from the list:

   
   python vacvssx.py --use-default
   

  Output:
   
   Select a default vulnerability from the list:
   [0] CVE-2021-12345: Example Vulnerability Description
   Enter the index of the vulnerability: 0
   Creating vulnerability assessment...
   

2. **Creating a Custom Vulnerability:**

  This command creates a custom vulnerability with the specified attributes:

   
   python vacvssx.py --id "CVE-2021-22986" --description "Vulnerability in F5 BIG-IP APM leading to authentication bypass." --impact 8.5 --exploitability 6.0
   

  Output:
   
   Creating vulnerability assessment...
   

3. **Displaying Help Message:**

  To see all available options and usage instructions, use the help flag:

   
   python vacvssx.py --help
   

  Output:
   
   usage: vacvssx.py [-h] [--use-default] [--id ID] [--description DESCRIPTION] [--impact IMPACT]
                     [--exploitability EXPLOITABILITY]
   



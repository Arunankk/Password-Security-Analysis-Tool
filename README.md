\# Password Security Analysis Tool



\## Overview

A Python-based cybersecurity project that evaluates password security using password length, character diversity, common-password checks, and predictable-pattern detection.



The tool assigns a score out of 100, classifies password strength as Weak, Medium, or Strong, and provides recommendations to improve password security.



\## Features

\- Password length evaluation

\- Lowercase, uppercase, digit, and special-character checks

\- Detection of common passwords and predictable word combinations

\- Detection of repeated characters and sequential patterns

\- Password strength score from 0 to 100

\- Strength classification: Weak, Medium, or Strong

\- Actionable security recommendations

\- Automated unit tests using Python's `unittest`



\## Requirements

\- Python 3.10 or later recommended

\- No third-party packages required



\## How to Run



1\. Open Command Prompt.

2\. Navigate to the project folder.

3\. Run:



```bash

python password\_analyzer.py

```



4\. Enter a fictional sample password to view the analysis report.



\## Run the Tests



```bash

python -m unittest discover -s tests -v

```



\## Project Structure



```text

Password-Security-Analysis-Tool/

├── password\_analyzer.py

├── README.md

└── tests/

&#x20;   └── test\_password\_analyzer.py

```



\## Security and Limitations

\- This is an educational heuristic tool, not a guarantee of password security.

\- Its score is not a measure of the time required to crack a password.

\- The common-password list is limited and does not cover every known weak password.

\- Do not enter real passwords or production credentials during testing.

\- Passwords are analyzed locally by this script and are not intentionally transmitted or saved by the program.



\## Learning Outcomes

\- Python programming and conditional logic

\- Basic password-security principles

\- Pattern detection and risk identification

\- Automated testing with `unittest`

\- Documenting a cybersecurity project for GitHub


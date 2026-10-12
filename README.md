 Password Security Analysis Tool

 Overview:

A Python-based cybersecurity project that evaluates password security using password length, character diversity, common-password checks, and predictable-pattern detection.

The tool assigns a score out of 100, classifies password strength as Weak, Medium, or Strong, and provides recommendations to improve password security.

 Features:

- Password length evaluation
- Lowercase, uppercase, digit, and special-character checks
- Detection of common passwords and predictable word combinations
- Detection of repeated characters and sequential patterns
- Password strength score from 0 to 100
- Password classification as Weak, Medium, or Strong
- Actionable security recommendations
- Automated unit tests using Python's unittest framework

 Requirements:

- Python 3.10 or later recommended
- No third-party packages required

 How to Run:

1. Open Command Prompt.
2. Navigate to the project folder:

   ```bash
   cd Desktop/Password-Security-Analysis-Tool
   ```

3. Run the program:

   ```bash
   python password_analyzer.py
   ```

4. Enter a fictional sample password to view the analysis report.

 Run the Tests:

Run the following command from the project folder:

```bash
python -m unittest discover -s tests -v
```

The project includes eight automated tests covering common passwords, repeated characters, sequential patterns, password classification, and score boundaries.

 Project Structure:

```text
Password-Security-Analysis-Tool/
├── password_analyzer.py
├── README.md
├── .gitignore
└── tests/
    └── test_password_analyzer.py
```

 Security and Limitations:

- This is an educational, heuristic-based tool and does not guarantee password security.
- The score does not represent the time required to crack a password.
- The common-password list is limited and does not cover every known weak password.
- The tool uses basic pattern checks and may not detect every predictable password.
- Do not enter real passwords or production credentials during testing.
- The script analyzes passwords locally and does not intentionally transmit or save the entered password.

 Learning Outcomes:

- Python programming and conditional logic
- Basic password-security principles
- Password pattern detection and risk identification
- Automated testing with Python's unittest framework
- Git and GitHub version control
- Cybersecurity project documentation

 Author:

Arunankk

 GitHub Repository:

https://github.com/Arunankk/Password-Security-Analysis-Tool

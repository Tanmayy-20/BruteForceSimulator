Brute Force Attack Simulator
===========================

This is an educational project that demonstrates how brute force attacks work 
against password-based authentication systems, and why strong passwords and 
security defenses are necessary to protect accounts.

The project simulates:
- Normal login attempts
- Brute force password attempts using a wordlist (wordlist.txt)
- Full brute force attempts using all character combinations
- Login system with account lockout defense

⚠ Disclaimer:
This tool is created for LEARNING and CYBERSECURITY EDUCATION ONLY.
Do NOT use this tool against real systems, networks, websites, or accounts.
Unauthorized access is illegal and punishable by law.

-------------------------------------------------------------
Project Folder Structure
-------------------------------------------------------------

BruteForceSimulator
│
├── simulator.py     - Main Python program
└── wordlist.txt     - List of passwords used for brute-force simulation

-------------------------------------------------------------
Features
-------------------------------------------------------------

1️⃣ Normal Login Mode
   - User enters password manually to authenticate.

2️⃣ Wordlist Based Brute Force Attack
   - Tries passwords from "wordlist.txt" one by one.
   - Shows attempts, time taken, and final result.

3️⃣ Full Brute Force Search
   - Generates every possible character combination.
   - Allows selecting character set: digits, lowercase, both, or custom.
   - Shows how password length increases difficulty exponentially.

4️⃣ Account Lockout Defense
   - Locks login after too many wrong attempts.
   - Demonstrates real-world security control.

-------------------------------------------------------------
Requirements
-------------------------------------------------------------

- Windows OS (or any OS with Python installed)
- Python 3.8+

-------------------------------------------------------------
How to Run
-------------------------------------------------------------

1. Install Python from: https://www.python.org/
2. Open the project folder in VS Code
3. Open terminal and run:

    python simulator.py

4. Choose options from menu to simulate different attacks.

-------------------------------------------------------------
Educational Objectives
-------------------------------------------------------------

✔ Understand brute-force attacks
✔ Learn how weak passwords get cracked
✔ Understand the impact of password complexity
✔ See how defenses like lockout help prevent attacks

-------------------------------------------------------------
Future Enhancements 
-------------------------------------------------------------

- Add GUI using Tkinter
- Add progress bar and time estimation
- Export results to text or PDF report
- Compare weak vs strong password cracking time graphs
- Add hashed password cracking simulation (MD5, SHA1, etc.)

GitHub Profile: <Your GitHub URL>

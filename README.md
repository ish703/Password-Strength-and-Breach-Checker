🔐 Password Strength & Breach Checker (Python)

A simple and effective Python-based tool that checks the strength of a password, detects whether it appears in known breached password lists, and also provides a secure SHA-256 hash for safe storage.

This project is perfect for learning basic cybersecurity concepts such as password hygiene, regex validation, hashing, and breach awareness.

🚀 Features
✅ 1. Password Strength Checker

Checks password strength based on:

Minimum length

Uppercase letters

Lowercase letters

Numbers

Special characters

✅ 2. Weak / Common Password Detection

The tool warns you if the password matches common weak passwords such as:
password, 123456, abc123, etc.

✅ 3. Breached Password Check

Your password is compared with a list inside:

breached_passwords.txt


If found → shows a warning
If not found → shows a safe message

✅ 4. SHA-256 Secure Hashing

The password is converted into a secure SHA-256 hash so it can be stored safely without exposing plain text.
🛠️ Technologies Used

Python 3

Regex (re)

Hashlib

VS Code (optional)

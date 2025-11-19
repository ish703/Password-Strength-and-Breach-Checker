🔐 Password Strength & Breach Checker (Python)

Passwords are the first and most important layer of security for protecting our digital information. Every year, millions of accounts get hacked because people continue to use weak, easy-to-guess, or breached passwords. Attackers use automated tools to crack simple passwords within seconds. Because of this, it has become essential to use strong, complex, and unique passwords for every account.

This project Password Strength & Breach Checker — is designed to help users understand the security level of their password before they use it. The tool analyzes the password in real-time and provides immediate feedback. It checks for password length, uppercase letters, lowercase letters, numbers, and special characters. It also warns the user if the password is too common or predictable.

A unique part of this project is the inclusion of a breached password check. Many passwords have already been leaked in past cyberattacks. These leaked passwords are stored in large breach databases. If a user’s password appears in such a breached list, it becomes unsafe to use—even if it is strong. That is why this tool checks the password against a sample file named breached_passwords.txt, which contains commonly leaked passwords. If the password is found, the tool alerts the user immediately.

To enhance security further, the project also generates a SHA-256 hash of the password. Password hashing ensures that the password is never stored or displayed in plain text. Even if someone gets access to the hashed password, it cannot be reversed easily. This demonstrates how real-world systems store passwords securely.

Overall, this project helps users:

Understand the importance of strong passwords

Avoid using passwords that are commonly hacked

Learn about hashing and how it protects sensitive data

Experience how password checking works in real cybersecurity systems

The project is built using Python, making it simple, lightweight, and easy to run on any system. It is an ideal project for students, beginners, and anyone learning cybersecurity fundamentals.

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

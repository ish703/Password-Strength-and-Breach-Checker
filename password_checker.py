# -------------------- PASSWORD STRENGTH, BREACH CHECKER & HASHING WITH GUI --------------------

import re
import hashlib
import tkinter as tk
from tkinter import messagebox

# -------------------- Data --------------------
common_passwords = ["123456", "password", "123456789", "qwerty", "abc123"]

# Make sure you have a file "breached_passwords.txt" with sample breached passwords:
# 123456
# password
# qwerty
# abc123
# letmein
# monkey
# dragon

# -------------------- Functions --------------------

# Password Strength Checker
def check_password_strength(password):
    strength = 0
    result = ""
    
    # Length
    if len(password) >= 8:
        strength += 1
    else:
        result += "Password too short, min 8 chars.\n"

    # Uppercase
    if re.search(r"[A-Z]", password):
        strength += 1
    # Lowercase
    if re.search(r"[a-z]", password):
        strength += 1
    # Numbers
    if re.search(r"[0-9]", password):
        strength += 1
    # Special Characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1

    # Common password check
    if password.lower() in common_passwords:
        result += "This is a common password. Avoid using it.\n"
        strength = 1

    # Strength result
    if strength <= 2:
        result += "Weak password"
    elif strength in [3, 4]:
        result += "Moderate password"
    else:
        result += "Strong password"

    return result

# Breach Checker
def check_password_breach(password):
    try:
        with open("breached_passwords.txt", "r") as file:
            breached_passwords = [line.strip() for line in file.readlines()]
        if password.lower() in breached_passwords:
            return "Warning: This password has appeared in a data breach!"
        else:
            return "Good news: This password has not been found in breaches."
    except FileNotFoundError:
        return "Breach dataset file not found!"

# Hash Password
def hash_password(password):
    encoded = password.encode()
    hashed = hashlib.sha256(encoded).hexdigest()
    return hashed

# -------------------- GUI Function --------------------
def analyze_password():
    password = password_entry.get()
    if not password:
        messagebox.showwarning("Input Error", "Please enter a password!")
        return

    strength_result = check_password_strength(password)
    breach_result = check_password_breach(password)
    hash_result = hash_password(password)

    messagebox.showinfo("Analysis Results",
                        f"{strength_result}\n\n{breach_result}\n\nSHA-256 Hash:\n{hash_result}")

# -------------------- GUI Setup --------------------
root = tk.Tk()
root.title("Password Strength & Breach Checker")
root.geometry("450x300")

label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

analyze_btn = tk.Button(root, text="Check Password", command=analyze_password, font=("Arial", 12))
analyze_btn.pack(pady=20)

root.mainloop()

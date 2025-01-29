import re
import tkinter as tk
from tkinter import messagebox

def check_password_complexity(password):
    # Criteria checks
    length_check = len(password) >= 8
    lowercase_check = any(char.islower() for char in password)
    uppercase_check = any(char.isupper() for char in password)
    digit_check = any(char.isdigit() for char in password)
    special_char_check = any(char in "!@#$%^&*()-_=+[{]}|;:'\",<.>/?`~" for char in password)

    # Feedback messages
    feedback = []

    if not length_check:
        feedback.append("Password must be at least 8 characters long.")
    if not lowercase_check:
        feedback.append("Password must include at least one lowercase letter.")
    if not uppercase_check:
        feedback.append("Password must include at least one uppercase letter.")
    if not digit_check:
        feedback.append("Password must include at least one digit.")
    if not special_char_check:
        feedback.append("Password must include at least one special character (e.g., !@#$%^&*).")

    if all([length_check, lowercase_check, uppercase_check, digit_check, special_char_check]):
        return "Password is strong!"
    else:
        return "Password is not strong enough.\n" + "\n".join(feedback)

def evaluate_password():
    password = password_entry.get()
    result = check_password_complexity(password)
    messagebox.showinfo("Password Complexity Check", result)

# Create the main application window
root = tk.Tk()
root.title("Password Complexity Checker")

# Create and place widgets
instruction_label = tk.Label(root, text="Enter your password to check its complexity:")
instruction_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", width=30)
password_entry.pack(pady=5)

check_button = tk.Button(root, text="Check Password", command=evaluate_password)
check_button.pack(pady=10)

# Run the application
root.mainloop()

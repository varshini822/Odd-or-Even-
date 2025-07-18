import tkinter as tk
from tkinter import messagebox

# Function to check odd or even
def check_odd_even():
    num = entry.get()
    
    if num.isdigit() or (num.startswith('-') and num[1:].isdigit()):
        num = int(num)
        if num % 2 == 0:
            result_label.config(text=f"{num} is an Even number ✅")
        else:
            result_label.config(text=f"{num} is an Odd number 🔢")
    else:
        result_label.config(text="❌ Invalid input! Please enter an integer.")

# GUI Setup
root = tk.Tk()
root.title("Odd or Even Checker")
root.geometry("400x200")
root.resizable(False, False)

# Title
title_label = tk.Label(root, text="🎯 Odd or Even Checker", font=("Arial", 16))
title_label.pack(pady=10)

# Input field
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=5)

# Button to check
check_button = tk.Button(root, text="Check", font=("Arial", 12), command=check_odd_even)
check_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

# Run the GUI loop
root.mainloop()

import random
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Initialize the main window with colorful theme
ctk.set_appearance_mode("dark")  # Dark theme
ctk.set_default_color_theme("green")  # Green theme

# Generate a random 4-digit secret number
secret_code = str(random.randint(1000, 9999))
attempts = 10

# Function to check the guess
def check_guess():
    global attempts
    guess = entry_guess.get()

    if len(guess) != 4 or not guess.isdigit():
        messagebox.showerror("❌ Error", "Enter a valid 4-digit number!")
        return

    if guess == secret_code:
        messagebox.showinfo("🎉 Winner!", "Congratulations! You cracked the code! 🔓")
        reset_game()
        return

    # Generate hints with colorful indicators
    hint = []
    for i in range(4):
        if guess[i] == secret_code[i]:
            hint.append("🟢")  # Correct place (Green)
        elif guess[i] in secret_code:
            hint.append("🟡")  # Correct number, wrong place (Yellow)
        else:
            hint.append("🔴")  # Wrong number (Red)

    # Update attempts and UI
    attempts -= 1  # Reduce attempts before updating UI
    attempts_label.configure(text=f"🎯 Attempts Left: {attempts}", fg_color="#FF5733")
    
    # Insert guess results with emoji-friendly font
    attempts_listbox.insert("1.0", f"🔢 Guess: {guess} → {' '.join(hint)}\n")
    attempts_listbox.yview_moveto(0)  # Scroll to top

    if attempts == 0:
        messagebox.showinfo("😢 Game Over", f"You lost! The secret code was {secret_code} 🎭")
        reset_game()

# Function to reset the game
def reset_game():
    global secret_code, attempts
    secret_code = str(random.randint(1000, 9999))
    attempts = 10
    attempts_label.configure(text="🎯 Attempts Left: 10", fg_color="#FFC300")
    attempts_listbox.delete("1.0", tk.END)

# Create main window
app = ctk.CTk()
app.title("🎮 Code Breaker Game")
app.geometry("450x550")
app.configure(fg_color="#1F1F1F")  # Dark Background

# UI Elements with Colors
title_label = ctk.CTkLabel(app, text="🔐 Code Breaker 🔐", font=("Segoe UI Emoji", 24), text_color="#00FF99")
title_label.pack(pady=15)

entry_guess = ctk.CTkEntry(app, placeholder_text="💡 Enter 4-digit guess", font=("Segoe UI Emoji", 18), fg_color="#282828", text_color="#FFD700")
entry_guess.pack(pady=10)

check_button = ctk.CTkButton(app, text="✅ Check Guess", command=check_guess, fg_color="#008080", hover_color="#006666", font=("Arial", 16))
check_button.pack(pady=10)

attempts_label = ctk.CTkLabel(app, text="🎯 Attempts Left: 10", font=("Arial", 16), text_color="#FFC300")
attempts_label.pack(pady=5)

# **Use tkinter.Text instead of CTkTextbox**
attempts_listbox = tk.Text(app, height=10, width=50, font=("Segoe UI Emoji", 14), bg="#2B2B2B", fg="white", borderwidth=2)
attempts_listbox.pack(pady=10)

reset_button = ctk.CTkButton(app, text="🔄 Restart Game", command=reset_game, fg_color="#FF4500", hover_color="#B22222", font=("Arial", 16))
reset_button.pack(pady=10)

# Run the app
app.mainloop()

import random
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Initialize the main window
ctk.set_appearance_mode("dark")  # Dark theme
ctk.set_default_color_theme("green")  # Green theme

app = ctk.CTk()
app.title("🎮 Code Breaker Game")
app.geometry("500x650")
app.configure(fg_color="#1C1C1C")  # Darker background for better contrast

# Global Variables
secret_code = ""
attempts = 0
mode_selected = False
selected_mode = tk.StringVar()

# Function to update mode details
def update_mode_details(choice):
    global attempts
    mode_details_label.configure(text="")  # Clear previous text
    
    if choice == "Easy":
        attempts = 5
        mode_details_label.configure(text="🔥 Easy Mode\n(3 Digits - 5 Attempts)", text_color="#00FF99")
    elif choice == "Medium":
        attempts = 7
        mode_details_label.configure(text="⚡ Medium Mode\n(4 Digits - 7 Attempts)", text_color="#FFD700")
    elif choice == "Hard":
        attempts = 9
        mode_details_label.configure(text="💀 Hard Mode\n(5 Digits - 9 Attempts)", text_color="#FF4500")

# Function to start the game
def start_game():
    global secret_code, mode_selected, attempts

    choice = selected_mode.get()
    if choice == "Easy":
        secret_code = str(random.randint(100, 999))  # 3-digit number
    elif choice == "Medium":
        secret_code = str(random.randint(1000, 9999))  # 4-digit number
    elif choice == "Hard":
        secret_code = str(random.randint(10000, 99999))  # 5-digit number
    else:
        messagebox.showerror("⚠️ Error", "Please select a valid mode!")
        return

    mode_selected = True
    mode_frame.pack_forget()  # Hide mode selection screen
    game_frame.pack(pady=20)  # Show game UI
    title_label.configure(text="🔐 Crack the Code!", text_color="#FFD700")
    attempts_label.configure(text=f"🎯 Attempts Left: {attempts}")
    attempts_listbox.delete("1.0", tk.END)  # Clear previous attempts

# Function to check the guess
def check_guess():
    global attempts

    if not mode_selected:
        return

    guess = entry_guess.get().strip()

    if len(guess) != len(secret_code) or not guess.isdigit():
        messagebox.showerror("❌ Error", f"Enter a valid {len(secret_code)}-digit number!")
        return

    if guess == secret_code:
        messagebox.showinfo("🎉 Winner!", f"Congratulations! You cracked the code! 🔓\nThe secret number was: {secret_code}")
        reset_game()
        return

    # Generate hints
    attempts_listbox.insert(tk.END, f"🔢 Guess: {guess} ➝ ", "bold")

    for i in range(len(secret_code)):
        if guess[i] == secret_code[i]:
            attempts_listbox.insert(tk.END, f"{guess[i]}(🟢) ", "green")  # Correct position
        elif guess[i] in secret_code:
            attempts_listbox.insert(tk.END, f"{guess[i]}(🟡) ", "yellow")  # Wrong position
        else:
            attempts_listbox.insert(tk.END, f"{guess[i]}(🔴) ", "red")  # Incorrect digit

    attempts_listbox.insert(tk.END, "\n")  # New line for next guess
    attempts_listbox.yview_moveto(1)  # Scroll to bottom

    attempts -= 1
    attempts_label.configure(text=f"🎯 Attempts Left: {attempts}")

    if attempts == 0:
        messagebox.showinfo("😢 Game Over", f"You lost! The secret code was {secret_code} 🎭")
        reset_game()

# Function to reset the game
def reset_game():
    global mode_selected
    mode_selected = False
    game_frame.pack_forget()  # Hide game UI
    mode_frame.pack(pady=20)  # Show mode selection screen
    title_label.configure(text="🔐 Code Breaker - Select Mode", text_color="#00FF99")
    selected_mode.set("")  # Reset dropdown
    mode_details_label.configure(text="")  # Clear mode details

# **Mode Selection Screen**
mode_frame = ctk.CTkFrame(app, fg_color="#2A2A2A", corner_radius=15)
mode_frame.pack(pady=30, padx=20, fill="both", expand=True)

title_label = ctk.CTkLabel(mode_frame, text="🔐 Code Breaker - Select Mode", font=("Segoe UI Emoji", 22), text_color="#00FF99")
title_label.pack(pady=20)

# **Dropdown Menu for Mode Selection**
mode_dropdown = ctk.CTkComboBox(mode_frame, values=["Easy", "Medium", "Hard"], variable=selected_mode,
                                command=update_mode_details, font=("Arial", 16), width=250)
mode_dropdown.pack(pady=10)

# **Mode Details Label**
mode_details_label = ctk.CTkLabel(mode_frame, text="", font=("Arial", 16))
mode_details_label.pack(pady=10)

# **Start Game Button**
start_button = ctk.CTkButton(mode_frame, text="🚀 Start Game", command=start_game, fg_color="#008080",
                             hover_color="#006666", font=("Arial", 18), height=45, corner_radius=10, width=200)
start_button.pack(pady=20)

# **Game UI (Initially Hidden)**
game_frame = ctk.CTkFrame(app, fg_color="#2A2A2A", corner_radius=15)

entry_guess = ctk.CTkEntry(game_frame, placeholder_text="💡 Enter Guess", font=("Segoe UI Emoji", 20),
                           fg_color="white", text_color="black", width=300, height=50)
entry_guess.pack(pady=15)

check_button = ctk.CTkButton(game_frame, text="✅ Check Guess", command=check_guess, fg_color="#008080",
                             hover_color="#006666", font=("Arial", 18), height=50, corner_radius=10, width=200)
check_button.pack(pady=10)

attempts_label = ctk.CTkLabel(game_frame, text="🎯 Attempts Left: 10", font=("Arial", 18), text_color="#FFC300")
attempts_label.pack(pady=5)

# **Enhanced Listbox for Guess History**
attempts_listbox = tk.Text(game_frame, height=10, width=55, font=("Segoe UI Emoji", 14), bg="#2B2B2B",
                           fg="white", borderwidth=2, relief="solid", wrap="word", padx=5, pady=5)
attempts_listbox.pack(pady=10)

# **Define color tags**
attempts_listbox.tag_configure("green", foreground="#00FF00", font=("Arial", 14, "bold"))
attempts_listbox.tag_configure("yellow", foreground="#FFD700", font=("Arial", 14, "bold"))
attempts_listbox.tag_configure("red", foreground="#FF4500", font=("Arial", 14, "bold"))
attempts_listbox.tag_configure("bold", font=("Arial", 14, "bold"))

reset_button = ctk.CTkButton(game_frame, text="🔄 Restart Game", command=reset_game, fg_color="#FF4500",
                             hover_color="#B22222", font=("Arial", 18), height=50, corner_radius=10, width=200)
reset_button.pack(pady=10)

# Run the app
app.mainloop()

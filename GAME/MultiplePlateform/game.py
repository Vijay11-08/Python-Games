import tkinter as tk
from tkinter import messagebox
import random

def show_game_selection():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Label(root, text="Choose a Game", font=("Comic Sans MS", 16), bg="lightyellow").pack()
    games = [
        ("Math Quiz", start_math_quiz_ui),
        ("Guess the Number", start_guess_ui),
        ("Rock Paper Scissors", start_rps_ui),
        ("Shape Matching Game", start_shape_ui),
        ("Tic-Tac-Toe", start_tic_tac_toe_ui),
        ("Memory Card Game", start_memory_game_ui),
        ("Maze Solver", start_maze_solver_ui),
        ("Word Scramble", start_word_scramble_ui),
        ("Typing Speed Test", start_typing_speed_ui),
        ("Balloon Pop Math", start_balloon_pop_math_ui)
    ]
    for name, func in games:
        tk.Button(root, text=name, command=func).pack(pady=5)

def start_math_quiz_ui():
    clear_window()
    quiz_frame = tk.Frame(root)
    tk.Label(quiz_frame, text="Math Quiz", font=("Arial", 16)).pack()
    
    def generate_question():
        num1 = random.randint(1, 10)
        num2 = random.randint(1, 10)
        operation = random.choice(["+", "-", "*"])
        question_label.config(text=f"{num1} {operation} {num2}")
        return eval(f"{num1} {operation} {num2}")
    
    def check_answer():
        try:
            user_ans = int(answer_entry.get())
            if user_ans == correct_answer:
                messagebox.showinfo("Result", "Correct!")
            else:
                messagebox.showinfo("Result", "Incorrect! Try Again")
            generate_new()
        except ValueError:
            messagebox.showwarning("Error", "Please enter a valid number!")
    
    def generate_new():
        global correct_answer
        correct_answer = generate_question()
    
    question_label = tk.Label(quiz_frame, text="", font=("Arial", 14))
    question_label.pack()
    
    answer_entry = tk.Entry(quiz_frame)
    answer_entry.pack()
    
    tk.Button(quiz_frame, text="Submit", command=check_answer).pack()
    generate_new()
    
    quiz_frame.pack()

def start_guess_ui():
    clear_window()
    guess_frame = tk.Frame(root)
    tk.Label(guess_frame, text="Guess the Number", font=("Arial", 16)).pack()
    number = random.randint(1, 50)
    
    def check_guess():
        try:
            user_guess = int(guess_entry.get())
            if user_guess == number:
                messagebox.showinfo("Result", "Correct! You guessed it!")
            elif user_guess < number:
                messagebox.showinfo("Result", "Too Low!")
            else:
                messagebox.showinfo("Result", "Too High!")
        except ValueError:
            messagebox.showwarning("Error", "Enter a number between 1-50")
    
    guess_entry = tk.Entry(guess_frame)
    guess_entry.pack()
    tk.Button(guess_frame, text="Check", command=check_guess).pack()
    guess_frame.pack()

def clear_window():
    for widget in root.winfo_children():
        widget.destroy()
    tk.Button(root, text="Back to Menu", command=show_game_selection).pack(pady=5)

# Placeholder functions for new games
def start_rps_ui(): pass
def start_shape_ui(): pass
def start_tic_tac_toe_ui(): pass
def start_memory_game_ui(): pass
def start_maze_solver_ui(): pass
def start_word_scramble_ui(): pass
def start_typing_speed_ui(): pass
def start_balloon_pop_math_ui(): pass

# Main Window
root = tk.Tk()
root.title("Kids Game Platform")
root.geometry("550x600")
root.configure(bg="lightyellow")
show_game_selection()
root.mainloop()

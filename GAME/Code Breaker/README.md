# Code Breaker (Puzzle Game) 🔐

## Game Concept
**"Code Breaker"** is a logic-based puzzle game where players must decode a secret number or word using clues and patterns. The game challenges problem-solving skills while keeping it fun and engaging.

## How It Works 🎮
- The game generates a secret **4-digit number** (or a word for advanced levels).
- Players must guess the correct code **within a limited number of attempts**.
- After each guess, the game provides hints:
  - 🔵 **Correct number in the correct place**
  - 🟡 **Correct number but in the wrong place**
  - ❌ **Wrong number**
- Players use these hints to refine their guesses and crack the code!

## Game Levels 🌟
- **Easy Mode** – 3-digit numbers, unlimited attempts.
- **Medium Mode** – 4-digit numbers, 10 attempts.
- **Hard Mode** – 5-digit numbers with fewer hints and 7 attempts.
- **Master Mode** – Guess a secret word instead of numbers!

## Features 🛠️
✅ **Graphical Interface** – Using `tkinter` or `pygame` for an interactive UI.
✅ **Timer Mode** – Solve within a time limit for an added challenge.
✅ **Leaderboard** – Track high scores and best times.
✅ **Multiplayer Mode** – Two players can take turns setting and guessing codes.
✅ **Randomized Codes** – Ensures fresh and challenging gameplay every time.

## Example of Game Flow 🎲
```
Secret Code: ????  
Player's Guess: 4523  
Hint: 🔵🟡❌❌ (1 number is correct in the right place, 1 correct but in the wrong place)  
```
The player keeps guessing based on these hints until they crack the code!

## Installation & Setup ⚙️
```bash
# Clone this repository
git clone https://github.com/your-username/code-breaker.git

# Navigate to the project directory
cd code-breaker

# Install required dependencies (if using Python)
pip install -r requirements.txt

# Run the game
python game.py
```

## Technologies Used 🖥️
- **Python** (Core logic and backend)
- **tkinter / pygame** (For graphical interface)
- **SQLite** (For storing leaderboard data)

## Future Enhancements 🚀
- **Online Multiplayer Mode** – Play with friends remotely.
- **More Difficulty Levels** – Increase complexity and challenge.
- **Theme Customization** – Players can choose game themes and colors.

## Contributing 🤝
Contributions are welcome! Feel free to open an issue or submit a pull request.


---
🚀 **Start breaking codes now! Happy guessing!** 🔐

![alt text](image.png)


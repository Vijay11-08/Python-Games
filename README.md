# AI Chess Game Using Pygame & Stockfish

This is an AI-powered Chess game built using **Pygame** and **Stockfish**. The player plays as **White**, and the AI (Stockfish) plays as **Black**.

---
## 🛠️ Installation

### **1️⃣ Install Dependencies**
Make sure you have **Python 3.8+** installed. Then, install the required libraries:
```sh
pip install pygame chess
```

### **2️⃣ Download Stockfish Engine**
- Download **Stockfish Chess Engine** from [official site](https://stockfishchess.org/download/).
- Extract the folder and copy the path of the Stockfish executable (`.exe` on Windows, or `.bin` on Linux/Mac).

### **3️⃣ Clone the Repository**
```sh
git clone https://github.com/yourusername/ai-chess-game.git
cd ai-chess-game
```

### **4️⃣ Set Stockfish Path**
Update the `STOCKFISH_PATH` variable in the script to the path where you downloaded Stockfish.

Example:
```python
STOCKFISH_PATH = r"C:\Users\YourName\Downloads\stockfish\stockfish-windows-x86-64-avx2.exe"
```

### **5️⃣ Run the Game**
```sh
python ai_chess.py
```

---
## 🎮 How to Play

- **Select a Piece:** Click on a white piece to see its valid moves.
- **Move the Piece:** Click on a valid square to move it.
- **AI Moves Automatically:** After your move, the AI (Stockfish) will respond.
- **Game Over:** Checkmate, stalemate, or insufficient material will end the game.

---
## 📷 Screenshots
*(Include screenshots of your game here!)*

---
## 🔧 Features
✅ Fully functional Chess game in Pygame  
✅ AI opponent powered by Stockfish  
✅ Legal move highlighting  
✅ Checkmate, stalemate, and draw detection  

---
## ⚠️ Troubleshooting
**Issue:** Pieces don't appear.  
✔ Make sure you have the correct images in the `pieces/` folder.

**Issue:** Stockfish is not working.  
✔ Verify the `STOCKFISH_PATH` is correct.

---
## 👥 Credits
- **Stockfish Team** - For the amazing chess engine
- **Pygame Community** - For the game framework

---
## 📜 License
This project is **open-source** under the MIT License.

Happy Gaming! 🎉♟️


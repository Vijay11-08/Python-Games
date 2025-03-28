let secretCode = "";
let attempts = 0;

function startGame() {
    let difficulty = document.getElementById("difficulty").value;
    
    if (difficulty === "easy") {
        secretCode = Math.floor(100 + Math.random() * 900).toString();
        attempts = 5;
    } else if (difficulty === "medium") {
        secretCode = Math.floor(1000 + Math.random() * 9000).toString();
        attempts = 7;
    } else {
        secretCode = Math.floor(10000 + Math.random() * 90000).toString();
        attempts = 9;
    }

    document.getElementById("game").style.display = "block";
    document.getElementById("attempts").innerText = `🎯 Attempts Left: ${attempts}`;
    document.getElementById("result").innerHTML = "";
    document.getElementById("codeBox").style.display = "none";
    document.getElementById("restartBtn").style.display = "none";
}

function checkGuess() {
    let guess = document.getElementById("guess").value;
    let resultText = "🔢 Guess: " + guess + " ➝ ";

    if (guess.length !== secretCode.length || isNaN(guess)) {
        alert(`❌ Enter a valid ${secretCode.length}-digit number!`);
        return;
    }

    if (guess === secretCode) {
        document.getElementById("codeBox").style.display = "block";
        document.getElementById("codeBox").innerText = `🎉 You Cracked the Code: ${secretCode}! 🎊`;
        document.getElementById("restartBtn").style.display = "block";
        return;
    }

    for (let i = 0; i < secretCode.length; i++) {
        if (guess[i] === secretCode[i]) {
            resultText += `${guess[i]}(🟢) `;
        } else if (secretCode.includes(guess[i])) {
            resultText += `${guess[i]}(🟡) `;
        } else {
            resultText += `${guess[i]}(🔴) `;
        }
    }

    document.getElementById("result").innerHTML += `<p>${resultText}</p>`;
    attempts--;
    document.getElementById("attempts").innerText = `🎯 Attempts Left: ${attempts}`;

    if (attempts === 0) {
        document.getElementById("codeBox").style.display = "block";
        document.getElementById("codeBox").innerText = `💀 Game Over! The Code was: ${secretCode} 😢`;
        document.getElementById("restartBtn").style.display = "block";
    }
}

function restartGame() {
    location.reload();
}
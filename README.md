# 🎯 Number Guessing Game (Python)

Welcome to the **Number Guessing Game**, a simple yet engaging command-line game built using Python. This project is a great way to understand how to handle user input, generate random numbers, use loops and conditionals, and improve the user experience with friendly messages and error handling.

---

## 📌 Table of Contents

- [About the Game](#about-the-game)
- [Features](#features)
- [How It Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Setup Instructions](#setup-instructions)
- [Sample Gameplay](#sample-gameplay)
- [Possible Improvements](#possible-improvements)
- [License](#license)

---

## 🧠 About the Game

In this game, the computer randomly selects a number between **1 and 100**, and the player has **5 attempts** to guess it correctly.

Each incorrect guess will prompt the player with whether the guess was **too low** or **too high**, helping them get closer to the right answer. If the player guesses the number correctly within 5 attempts, they win the game!

---

## 🌟 Features

✅ Random number generation  
✅ Input validation and error handling  
✅ Attempt-based gameplay  
✅ Helpful hints after each guess  
✅ Friendly messages and emojis for better experience  
✅ Clean and beginner-friendly Python code

---

## ⚙️ How It Works

1. The program imports the `random` module to generate a random number between 1 and 100.
2. The player is prompted to enter a guess.
3. After each guess:
   - If it's too high or too low, the program gives feedback.
   - If it’s correct, the player wins.
4. The player gets a total of **5 chances**.
5. If all chances are used without guessing correctly, the correct number is revealed.

---

## 🧰 Technologies Used

- **Python 3.x**
- No external libraries are required.

---
## screenshot
![project-screenshot]()

## 🚀 Setup Instructions

1. Make sure Python is installed. To check, open a terminal and run:
   ```bash
   python --version

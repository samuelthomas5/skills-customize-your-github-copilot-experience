
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build the classic word-guessing game using Python strings, loops, and user input. Players will guess letters to reveal a hidden word before running out of attempts. This assignment practices string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Set Up Game Structure

#### Description
Create the foundational structure for your Hangman game, including initializing variables, setting up a word list, and implementing the game loop.

#### Requirements
Completed program should:

- Have a predefined list of words to randomly select from
- Initialize game variables (word, guessed letters, attempts remaining)
- Implement a main game loop that continues until win/lose condition
- Display the current game state after each turn


### 🛠️ Implement Game Logic

#### Description
Add the core logic for handling player input, checking guesses, and updating the game state based on whether guesses are correct or incorrect.

#### Requirements
Completed program should:

- Accept letter input from the player
- Check if the guessed letter is in the hidden word
- Track guessed letters and prevent duplicate guesses
- Update the word progress display in the format (_ _ _ _)
- Decrease attempts remaining for incorrect guesses


### 🛠️ Add Win/Lose Conditions

#### Description
Implement the end-game logic that determines when the player wins or loses, and display appropriate messages.

#### Requirements
Completed program should:

- Detect when the word is completely guessed (win condition)
- Detect when attempts reach zero (lose condition)
- Display a win message with the revealed word
- Display a lose message with the correct word
- Offer to play again or exit gracefully

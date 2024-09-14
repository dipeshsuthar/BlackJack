# Blackjack Game in Python

## Overview

This repository contains a Python implementation of a simplified Blackjack game. The game allows a player to play against a dealer, following the standard rules of Blackjack. The program features a text-based interface and handles multiple game rounds.

## Features

- **Card and Deck Management**: Create and manage a standard deck of 52 cards.
- **Hand Evaluation**: Track and evaluate the player's and dealer's hands, including handling Ace values.
- **Game Logic**: Support for multiple rounds of Blackjack with standard game rules.
- **Replay Option**: Allow players to play multiple games in a single session.
- **Text Output**: Display game progress and results in the console and log to a file.

## How to Run the Program

1. **Prerequisites**: Ensure you have Python 3.x installed on your system.

2. **Clone the Repository**: Download or clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Run the Program**: Execute the Python script to start the game.

   ```bash
   python blackjack_game.py
   ```

4. **Follow the Prompts**: Enter your name, choose the number of games, and follow the prompts to play the game.

## Program Functionality

### 1. **Card Class**

   - **Purpose**: Represents an individual card with a suit and rank.
   - **Methods**:
     - `__init__(self, suit, rank)`: Initializes a card with the given suit and rank.
     - `__str__(self)`: Returns a string representation of the card (e.g., "10 of hearts").

### 2. **Deck Class**

   - **Purpose**: Manages a deck of 52 cards, including shuffling and dealing.
   - **Methods**:
     - `__init__(self)`: Creates a deck with all possible combinations of suits and ranks.
     - `shuffle(self)`: Shuffles the deck.
     - `deal(self, number)`: Deals a specified number of cards from the deck.

### 3. **Hand Class**

   - **Purpose**: Represents a hand of cards for a player or dealer.
   - **Methods**:
     - `__init__(self, dealer=False)`: Initializes a hand, optionally marking it as a dealer's hand.
     - `add_card(self, card_list)`: Adds cards to the hand.
     - `calculate_value(self)`: Calculates the total value of the hand, adjusting for Aces as needed.
     - `get_value(self)`: Returns the calculated value of the hand.
     - `is_blackjack(self)`: Checks if the hand is a Blackjack (value of 21 with two cards).
     - `display(self, show_all_dealer_cards=False)`: Displays the cards in the hand, optionally showing hidden dealer cards.

### 4. **Game Class**

   - **Purpose**: Manages the flow of the game, including dealing, player actions, and determining winners.
   - **Methods**:
     - `play(self)`: Starts and manages the game loop, handling multiple rounds and player actions.
     - `check_winner(self, player_hand, dealer_hand, game_over=False)`: Determines the winner of the game based on the hands' values.
     - `print(self)`: Returns the text output for the game (used internally).

### 5. **Game Flow**

   - **Initial Setup**: The player enters their name and chooses the number of games to play.
   - **Game Rounds**:
     1. **Deal**: Two cards are dealt to both the player and the dealer.
     2. **Player Turn**: The player decides whether to "Hit" or "Stand".
     3. **Dealer Turn**: The dealer draws cards until reaching at least 17.
     4. **Determine Winner**: Compare hands and announce the winner.
   - **Replay**: After each game, the player can choose to play again or exit.

## Example Output

```
Welcome User!
******************************
Rules for Name: 
 Only Alphabets 
 #No Digits
 #No Special Characters
 #No Symbols
******************************
Please enter your name to start the Blackjack Game: John
Hello John! Please choose an option below 😊
How many games do you want to play? 3
You Played: 3
******************************
Game 1 of 3
Your hand:
10 of hearts
5 of spades
Value: 15

Dealer's hand:
Hidden
7 of diamonds

Choose 'Hit' or 'Stand': h
...
Your choice was: hit
...

Final Results:
Your hand: 20
Dealer's hand: 19
You win! 😀

Would you like to play again? : no
Thank you for Playing! John
If you want to play again, run this program again 😊
```

## Result Logging

- Game results and key actions are logged to `results.txt` in the repository directory.

## Contact

For any questions or feedback, please open an issue in the repository or contact the repository owner.

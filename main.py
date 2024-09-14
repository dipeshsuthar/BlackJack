import fileinput
import random

#Creating card class for suits and rank
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.rank['rank']} of  {self.suit}"

#Creating deck class for suits and ranks of Blakcjack Game.
class Deck:
    def __init__(self):
        self.cards = []
        #List of suits
        suits = ["speades", "clubs", "hearts", "diamonds"]
        #List of Ranks with it's values
        ranks = [
            {"rank": "A", "value": 11},
            {"rank": "2", "value": 2},
            {"rank": "3", "value": 3},
            {"rank": "4", "value": 4},
            {"rank": "5", "value": 5},
            {"rank": "6", "value": 6},
            {"rank": "7", "value": 7},
            {"rank": "8", "value": 8},
            {"rank": "9", "value": 9},
            {"rank": "10", "value": 10},
            {"rank": "J", "value": 10},
            {"rank": "Q", "value": 10},
            {"rank": "K", "value": 10}
        ]
        for suit in suits:
            for rank in ranks:
                self.cards.append(Card(suit, rank))
    #Function to shuffle the cards
    def shuffle(self):
        if len(self.cards) > 1:
            random.shuffle(self.cards)
    #Function for deal of cards
    def deal(self, number):
        cards_dealt = []
        for x in range(number):
            if len(self.cards) > 0:
                card = self.cards.pop()
                cards_dealt.append(card)
        return cards_dealt

#Function for hand of players and dealers
class Hand:
    def __init__(self, dealer=False):
        self.cards = []
        self.value = 0
        self.dealer = dealer
    #To add cards
    def add_card(self, card_list):
        self.cards.extend(card_list)
    #to calculate card values
    def calculate_value(self):
        self.value = 0
        has_ace = False

        for card in self.cards:
            card_value = int(card.rank["value"])
            self.value += card_value
            if card.rank["rank"] == "A":
                has_ace = True

            if has_ace and self.value > 21:
                self.value -= 10
    #to get the card values
    def get_value(self):
        self.calculate_value()
        return self.value
    #to check if it's blackjack or not
    def is_blackjack(self):
        return self.get_value() == 21
    #displaying the cards
    def display(self, show_all_dealer_cards=False):
        print(f'''{"Dealer's " if self.dealer else "Your"} hand:''')
        printstuff(f'''{"Dealer's " if self.dealer else "Your"} hand:''')

        for index, card in enumerate(self.cards):
            if index == 0 and self.dealer \
                    and not show_all_dealer_cards and not self.is_blackjack():
                print("Hidden")
                printstuff("Hidden")
            else:
                print(card)
                printstuff(card)


        if not self.dealer:
            print("Value: ", self.get_value())
        print()

def printstuff(stuff):
    with open("results.txt", "a") as file:
        print(stuff, file=file)

#Function to play the Blackjack game
class Game:
    def play (self):
        game_number = 0
        games_to_play = 0

        while games_to_play <= 0:
            try:
                games_to_play = int(input("How many games do you want to play? "))
                printstuff("You Played :")
                printstuff(games_to_play)
            except:
                print("You must enter a value.")

        while game_number < games_to_play:
            game_number += 1

            deck = Deck()
            deck.shuffle()

            player_hand = Hand()
            dealer_hand = Hand(dealer=True)

            for i in range(2):
                player_hand.add_card(deck.deal(1))
                dealer_hand.add_card(deck.deal(1))

            print()
            print("*" * 30)
            print(f"Game {game_number} of {games_to_play}")
            printstuff(f"Game {game_number} of {games_to_play}")
            print("*" * 30)
            player_hand.display()
            dealer_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            choice = ""
            while player_hand.get_value() < 21 and choice not in ["s", "stand"]:
                choice = input("Choose 'Hit' or 'Stand':").lower()
                print()
                printstuff("\nYour choice was : "+ choice + "\n")
                while choice not in ["h", "s", "hit", "stand"]:
                    choice = input("Choose 'Hit' or 'Stand' (or H/S):").lower()
                    print()
                    printstuff("\nYour choice was  :"+ choice + "\n")

                if choice in ["hit", "h"]:
                    player_hand.add_card(deck.deal(1))
                    player_hand.display()

            if self.check_winner(player_hand, dealer_hand):
                continue

            player_hand_value = player_hand.get_value()
            dealer_hand_value = dealer_hand.get_value()

            while dealer_hand_value < 17:
                dealer_hand.add_card(deck.deal(1))
                dealer_hand_value = dealer_hand.get_value()

            dealer_hand.display(show_all_dealer_cards=True)

            if self.check_winner(player_hand, dealer_hand):
                continue

            print("Final Resulsts:")
            printstuff("\nFinal Results:")

            print("Your hand:", player_hand_value)
            printstuff(player_hand_value)

            print("Dealer's hand:", dealer_hand_value)
            printstuff(dealer_hand_value)




            self.check_winner(player_hand, dealer_hand, True)

        print("\n Thanks for Playing!" + name)
        printstuff("Thanks for Playing!" + name + "\n")

    #Function to check the winner of the game
    def check_winner(self, player_hand, dealer_hand, game_over=False):
        if not game_over:
            if player_hand.get_value() > 21:
                print("You busted. Dealer wins! 😭")
                printstuff("\nYou busted. Dealer wins!\n")

                return True
            elif dealer_hand.get_value() > 21:
                print("Dealer busted. You win! 😀")
                printstuff("\nDealer busted. You win!\n")


                return True
            elif dealer_hand.is_blackjack() and player_hand.is_blackjack():
                print("Both players have blackjack! Tie! 😑")
                printstuff("\nBoth players have blackjack! Tie!\n")

                return True
            elif player_hand.is_blackjack():
                print("You have blackjack. You win! 😀")
                printstuff("\nYou have blackjack. You win!\n")

                return True
            elif dealer_hand.is_blackjack():
                print("Dealer has blackjack. Dealer wins! 😭")
                printstuff("\nDealer has blackjack. Dealer wins!\n")

                return True
        else:
            if player_hand.get_value() > dealer_hand.get_value():
                print("You win! 😀")
                printstuff("\nYou win!\n")

            elif player_hand.get_value() == dealer_hand.get_value():
                print("Tie! 😑")
                printstuff("\nTie!\n")

            else:
                print("Dealer wins. 😭")
                printstuff("\nDealer Wins!\n")

            return True
        return False

    def print(self):
        return self.text



#TO start the Game
print("\u001b[33m Welcome User!")
print("*" * 30)
print("\u001b[33m Rules for Name: \n Only Alphabets \n #No Digits\n #No Special Characters\n #No Symbols")
print("*" * 30)
name = str(input("\u001b[0m Please enter your name to start the Blackjack Game : -", ))
printstuff("Your name :" + name)
print("Hello " + name + " Please chose option below 😊")
g = Game()
g.play()
answer = "yes", "no"
answer = input("Would like to play again? :")
while answer in ["yes"]:
    g.play()
    answer = input("Would like to play again? :")
    if answer not in ["yes"]:
        print("Thank you for Playing! " + name + "\n  If you want to play again Run this program again 😊")

fileinput.close()
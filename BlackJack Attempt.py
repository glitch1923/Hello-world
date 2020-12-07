# Imports and Constants

import random

suits = ["Heart", "Spades", "Clubs", "Diamonds"]
ranks = ["Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King", "Ace"]
value = {"Two": 2, "Three": 3, "Four": 4, "Five": 5, "Six": 6, "Seven": 7, "Eight": 8, "Nine": 9, "Ten": 10, "Jack": 10,
         "Queen": 10, "King": 10, "Ace": 11}


# Create Card

class card():
    def __init__(self, suit_, rank_):
        self.suit_ = suit_
        self.rank_ = rank_
        self.value = value[rank_]

    def __str__(self):
        return (f"{self.rank_} of {self.suit_}")


# Create Deck of Cards as an object itself

class Deck():
    def __init__(self):
        self.allcards = []
        for suit in suits:
            for rank in ranks:
                self.allcards.append(card(suit, rank))

    # Using random library, we shuffle the items in the list

    def shuffle_cards(self):
        random.shuffle(self.allcards)

    # Deal once - will just pop one card from the deck.

    def deal_once(self):
        return self.allcards.pop(0)


# We need to now create the Player Class
# Creating a Player, His Attributes and things he carries for the game.

class Player():
    # Player having attributes of Name, Money in Wallet and Cards
    def __init__(self):
        self.name = input("Enter your Name: ")
        self.wallet = 3000
        self.all_cards = []
        self.bet_amount = 0

    # To add to Holding cards of Player
    def add_cards(self, dealt_card):
        self.all_cards.append(dealt_card)

    # To Place a bet - cash mechanics
    def bet(self):
        self.bet_amount = int(input(f"You have ${self.wallet}. Place your bet :"))
        self.wallet = self.wallet - self.bet_amount
        return self.bet_amount

    # To add Cash to Player wallet when he wins
    def add_cash(self, win_amount):
        self.wallet = self.wallet + win_amount

    # To know what cards a player is holding
    def holding(self):
        for i in range(0, len(self.all_cards)):
            print(self.all_cards[i])

    def score(self):
        total_score = 0
        for i in range(0, len(self.all_cards)):
            if self.all_cards[i] != "Ace of Diamonds" and self.all_cards[i] != "Ace of Spades" and self.all_cards[
                i] != "Ace of Clubs" and self.all_cards[i] != "Ace of Hearts":
                total_score = total_score + self.all_cards[i].value
            elif self.all_cards[i] == "Ace of Diamonds" or self.all_cards[i] == "Ace of Spades" or self.all_cards[
                i] == "Ace of Clubs" or self.all_cards[i] == "Ace of Hearts":
                if total_score <= 10:
                    total_score = total_score + 11
                else:
                    total_score = total_score + 1

        return total_score


class Dealer():
    # Player having attributes of Name, Money in Wallet and Cards
    def __init__(self):
        self.name = "Dealer"
        self.all_cards = []

    # To add to Holding cards of Player
    def add_cards(self, dealt_card):
        self.all_cards.append(dealt_card)

    # To add Cash to Player wallet when he wins
    def add_cash(self, win_amount):
        self.wallet = self.wallet + win_amount

    # To know what cards a player is holding
    def holding(self):
        for i in range(0, len(self.all_cards)):
            print(self.all_cards[i])

    # To know the value of sum of card ranks of one player

    # To know the value of sum of card ranks except the first one (which is blind)
    def score(self):
        total_score = 0
        for i in range(0, len(self.all_cards)):
            if self.all_cards[i] != "Ace of Diamonds" and self.all_cards[i] != "Ace of Spades" and self.all_cards[
                i] != "Ace of Clubs" and self.all_cards[i] != "Ace of Hearts":
                total_score = total_score + self.all_cards[i].value
            elif self.all_cards[i] == "Ace of Diamonds" or self.all_cards[i] == "Ace of Spades" or self.all_cards[
                i] == "Ace of Clubs" or self.all_cards[i] == "Ace of Hearts":
                if total_score <= 10:
                    total_score = total_score + 11
                else:
                    total_score = total_score + 1
            else:
                pass
        return total_score

    def partial_sum(self):
        total_score = 0
        for i in range(1, len(self.all_cards)):
            if self.all_cards[i] != "Ace of Diamonds" and self.all_cards[i] != "Ace of Spades" and self.all_cards[
                i] != "Ace of Clubs" and self.all_cards[i] != "Ace of Hearts":
                total_score = total_score + self.all_cards[i].value
            elif self.all_cards[i] == "Ace of Diamonds" or self.all_cards[i] == "Ace of Spades" or self.all_cards[
                i] == "Ace of Clubs" or self.all_cards[i] == "Ace of Hearts":
                if total_score <= 10:
                    total_score = total_score + 11
                else:
                    total_score = total_score + 1
            else:
                pass
        return total_score
    # Functions defined for checking wins in 3 different fashions.


# Check for replay game ?

def repeat():
    repeat = input("Would you like to Play again? Y/N: ").lower()
    if repeat == 'y':
        return True
    else:
        return False


# Check for blackjack score 21
def bj_check(score):
    return score == 21


# Check for a bust when score goes beyond 21
def bust_check(score):
    return score > 21


# Check comparitively between Player and Dealer Scores in case it is less than 21
def Player_Win(Player_score, Dealer_score):
    return (Player_score() > Dealer_score())


# START OF GAME LOGIC

game_start = input("\nWould you Like to Play a Game of BlackJack ?\nEnter Y(es) or N(o) :").lower()
if game_start == 'y':
    # Create Player, Dealer, Deck of Cards
    Player1 = Player()
    Dealer1 = Dealer()
    game_on = True
    # Game Start
    while game_on:
        # Bet Value
        Player1.all_cards = []
        Dealer1.all_cards = []
        bet_value = Player1.bet()
        # Create New Deck & Shuffle it
        New_Deck = Deck()
        New_Deck.shuffle_cards()
        # Draw two cards each for Dealer and Player
        for i in range(0, 2):
            Player1.all_cards.append(New_Deck.deal_once())
            Dealer1.all_cards.append(New_Deck.deal_once())
        turn = 'Player'
        print(f"{Player1.name} goes first")
        # Player1 Turn
        while turn == 'Player':
            print(f"\nYou currently hold the below cards :\t\t\t Wallet:${Player1.wallet}\n ")
            Player1.holding()
            if bust_check(Player1.score()):
                print(f"\n{Player1.name} Busts ! Dealer Wins !\t\t\t\t Wallet: {Player1.wallet}\n")
                print(f"\nDealer's Cards :\n")
                Dealer1.holding()
                print(f"\n{Player1.name}'s Cards :\n")
                Player1.holding()
                game_on = False
                if repeat():
                    game_on = True


            elif bj_check(Player1.score()):
                Player1.wallet = Player1.wallet + (bet_value * 2)
                print(f"\n{Player1.name} wins BlackJack ! \t\t\t\t Wallet: {Player1.wallet}\n")
                print(f"\nDealer's Cards :\n")
                Dealer1.holding()
                print(f"\n{Player1.name}'s Cards :\n")
                Player1.holding()
                game_on = False
                if repeat():
                    game_on = True
                break

            hit_on = input(f"\nYour current total is - {Player1.score()}. Would you like to Hit? : Y/N  \n").lower()
            if hit_on == 'y':
                Player1.all_cards.append(New_Deck.deal_once())
                if bust_check(Player1.score()):
                    print(f"\n{Player1.name} Busts ! Dealer Wins !\t\t\t\t Wallet: {Player1.wallet}\n")
                    print(f"\nDealer's Cards :\n")
                    Dealer1.holding()
                    print(f"\n{Player1.name}'s Cards :\n")
                    Player1.holding()
                    game_on = False
                    if repeat():
                        game_on = True
                    hit_on = 'n'
                    break

                elif bj_check(Player1.score()):
                    Player1.wallet = Player1.wallet + (bet_value * 2)
                    print(f"\n{Player1.name} wins BlackJack ! \t\t\t\t Wallet: {Player1.wallet}\n")
                    print(f"Dealer's Cards :\n")
                    Dealer1.holding()
                    print(f"{Player1.name}'s Cards :\n")
                    Player1.holding()
                    game_on = False
                    if repeat():
                        game_on = True
                    hit_on = 'n'
                    break
            else:
                turn = 'Dealer'
                break

        while turn == 'Dealer':
            print("\nDealer's Turn !")
            print(f"\nDealer's Cards :")
            Dealer1.holding()
            if bust_check(Dealer1.score()):
                Player1.wallet = Player1.wallet + (bet_value * 2)
                print(f"\n{Dealer1.name} Busts ! {Player1.name} Wins !\t\t\t\t Wallet: {Player1.wallet}\n")
                print(f"\nDealer's Cards :")
                Dealer1.holding()
                print(f"\n{Player1.name}'s Cards :")
                Player1.holding()
                game_on = False
                if repeat():
                    game_on = True
                turn = 'None'
                break

            elif bj_check(Dealer1.score()):
                print(f"{Dealer1.name} wins BlackJack !\t\t\t\t Wallet: {Player1.wallet}\n")
                print(f"Dealer's Cards :\n")
                Dealer1.holding()
                print(f"\n{Player1.name}'s Cards :\n")
                Player1.holding()
                game_on = False
                if repeat():
                    game_on = True
                turn = 'None'
                break
            else:
                while Dealer1.partial_sum() <= 17:
                    Dealer1.all_cards.append(New_Deck.deal_once())

while bj_check(Dealer1.score()) and bust_check(Dealer1.score()) and bj_check(Player1.score) and bust_check(
        Player1.score):
    if Player_Win(Player1.score, Dealer1.score):
        Player1.wallet = Player1.wallet + (bet_value * 2)
        print(f"\n{Player1.name} Wins with score {Player1.score()} !\t\t\t\t Wallet: {Player1.wallet}\n")
        print(f"\n{Player1.name}'s Cards :")
        Player1.holding()
        print(f"\nDealer's Cards :")
        Dealer1.holding()
        game_on = False
        if repeat():
            game_on = True
    else:
        print(f"\nDealer Wins ! with score {Dealer1.score()}\n")
        print(f"\nDealer's Final Cards :")
        Dealer1.holding()
        print(f"\n{Player1.name}'s Cards :")
        Player1.holding()
        game_on = False
        if repeat():
            game_on = True
        break



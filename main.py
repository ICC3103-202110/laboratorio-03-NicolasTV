import random
from player import Player
from ambassador import Ambassador
from assassin import Assassin
from captain import Captain 
from contessa import Contessa
from duke import Duke

players = []
coins = []
deck = []
TURN = n_players - 1
DECK_MAX = 3


def start_game():

    print("\n·················· Welcome to Coup ··················")
    print("This board game is played with a minimum of 3 players and a maximum of 4.\n")

    n_players = int(input("Enter the number of players:  "))
    while n_players < 3 or n_players > 4:
        print("Invalid number of players, try again\n")
        n_players = int(input("Enter the number of players:  "))

def generate_players(array):
    for i in range(n_players):
        user_id = i + 1
        name = input(f"\nWrite the name of player {user_id}: ")
        players.append(Player(name, user_id))

    return players

def next_turn():
    TURN += 1
    if TURN == n_players:
        return 1

    return 2

def coin(Player(user_id)):
    
    



def generate_deck():
    while i < DECK_MAX:
        deck.append(Ambassador())
        deck.append(Assassin())
        deck.append(Captain())
        deck.append(Contessa())
        deck.append(Duke())
        i += 1
    
    random.shuffle(deck)
    
    return deck    


if __name__ == "__main__":
    start_game()

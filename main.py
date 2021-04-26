import random
from player import Player
from actions import Actions
from coup import Coup
from income import Income
from foreign_aid import Foreign_aid
from ambassador import Ambassador
from assassin import Assassin
from captain import Captain
from contessa import Contessa
from duke import Duke
from deck import Deck

CONTINUE_PLAYING = True


def intro():
    print("\n·················· Welcome to Coup ··················")
    print("This table game is played with at least 3 players "
          "and maximum 4.\n")

def game_deck(game_cards):
    game_cards = create_deck()
    game_deck = random.shuffle(game_cards)
     
    return game_deck

def create_players(Player):
    players_list = []

    N_PLAYERS = int(input("\nEnter the number of players: "))
    while N_PLAYERS < 3 or N_PLAYERS > 4:
        print("Invalid number of players, try again\n")
        N_PLAYERS = int(input("Enter the number of players: "))
    print(" ")

    for i in range(N_PLAYERS):
        name = input(f"Write the name of player {i + 1}: ")
        coins = 0
        user_id = i
        alive = True
        hand_cards = [0, 0]
        players_list.append(Player(name, coins, user_id, alive, hand_cards))

    return players_list



def show_coins(array):
    print("\nThe balance is: ")

    for (i, _) in enumerate(array):
        print(f"{array[i].name}: {array[i].coins}")
    print(" ")

    return array


def next_turn(array):
    turn = 0
    for i in range(len(array)):
        print(f"Its {array[i].name} turn: ")
        turn += 1


if __name__ == "__main__":
    game_cards = []
    intro()
    players = create_players(Player)
    show_coins(players)
    cards = game_deck(Deck)
    game_cards.append(cards)
    
    while CONTINUE_PLAYING = True:


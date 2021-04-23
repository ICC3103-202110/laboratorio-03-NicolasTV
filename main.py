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
from game import Game

CONTINUE_PLAYING = True


def intro():
    print("\n·················· Welcome to Coup ··················")
    print("This table game is played with at least 3 players "
          "and maximum 4.\n")


def create_players():
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
        playing = True
        players_list.append(Player(name, coins, user_id, playing))

    return players_list


def show_coins(array):
    print("\nThe balance is: ")

    for (i, _) in enumerate(array):
        print(f"{array[i].name}: {array[i].coins}")
    print(" ")

    return array


def next_turn(n, Player.user_id):
    for i in range(n)
        if Player.user_id == n:
            print(f"Is {Player[n].name} turn")

            return n-1

        return
     

    


if __name__ == "__main__":
    intro()
    players = create_players()
    show_coins(players)

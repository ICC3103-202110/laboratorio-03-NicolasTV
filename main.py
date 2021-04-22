import random
from player import Player

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
        players_list.append(Player(name, coins, user_id))

    return players_list


def show_coins(array):
    print("\nThe balance is: ")

    for (i, _) in enumerate(array):
        print(f"{array[i].name}: {array[i].coins}")
    print(" ")

    return array


def next_turn(players):

    print()


if __name__ == "__main__":
    intro()
    players = create_players()
    show_coins(players)

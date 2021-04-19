from player import Player

players = []


def start_game():

    print("\n·················· Welcome to Coup ··················")
    print("This board game is played with a minimum of 3 players and a maximum of 4.\n")
    n_players = int(input("Enter the number of players:  "))
    while n_players < 3 or n_players > 4:
        print("Invalid number of players, try again\n")
        n_players = int(input("Enter the number of players:  "))

    for i in range(n_players):
        user_id = i + 1
        name = str(input(f"\nWrite the name of player {user_id}: "))
        players.append(Player(name, user_id))


def console():

    while true:
        start_game()


if __name__ == "__main__":
    print(start_game())

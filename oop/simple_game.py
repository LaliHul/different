# Simple Game
# Demonstrates importing modules

import games, random

print("Welcome to the world's simplest game!")

again = None
while again != "n":
    players = []
    num = games.ask_number(question = "How many players? (2 - 5):", low = 2, high = 5)

    for i in range(num):
        name = input("")
        score = random.randrange(100) - 1
        player = games.Player(name, score)
        players.append(player)

    print("Here are the game results:")
    for player in players:
        print(player)

    again = games.ask_yes_no("Do you want to play again? (y/n)")

input("\n\nPress the enter key to exit.")

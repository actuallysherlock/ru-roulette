import random
import time
import os
from termcolor import colored

def russian_roulette_game():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("\n Let's play some Russian Roulette.")
    # Player selection menu
    players = ["Player 456", "Salesman"]
    print("\n   (1) Player 456")
    print("   (2) Salesman\n")

    selected_player = input(" [*] Choose your player (1 or 2): ").strip()
    if selected_player == "1":
        selected_player = players[0]
    elif selected_player == "2":
        selected_player = players[1]
    else:
        print(colored(" [!] Invalid choice. Defaulting to Player 456.", "light_red"))
        selected_player = players[0]
    print("")

    # Game setup
    options = ['Click'] * 5 + ['BANG']
    random.shuffle(options)
    player_turn = players[0]  # Initial turn
    print(" " + ("-" * 35))
    print("")

    while options:
        if len(options) == 2:
            print(" 50/50 chance! Spinning the chamber...")
            time.sleep(0.5)

        result = options.pop() 
        time.sleep(0.5)

        if (6 - len(options) == 1 and result == "BANG"):
            print(f" Round 1 - {player_turn}'s turn: {colored(result.upper(), 'light_green' if result == "Click" else 'light_red')}")
            print("")
            print(" " + ("-" * 35))
            print(f"\n WOMP WOMP. {player_turn}, you lost ON THE FIRST TRY.")
            break
        else:
            print(f" Round {6 - len(options)} - {player_turn}'s turn: {colored(result.upper(), 'light_green' if result == "Click" else 'light_red')}")

            if result == "BANG":
                if player_turn == selected_player:
                    print("")
                    print(" " + ("-" * 35))
                    print(f"\n BANG! {player_turn}, you died.")
                else:
                    print("")
                    print(" " + ("-" * 35))
                    print(f"\n Lucky, you survived! {player_turn} is out.")
                break

            # Switch player turn
            player_turn = players[1] if player_turn == players[0] else players[0]

if __name__ == "__main__":
    shall_continue = True
    while True:
        if not shall_continue:
            break
        russian_roulette_game()
        while True:
            user_choice = input("\n [*] Play again? (Y/N): ")
            if user_choice.lower() == "y":
                break
            elif user_choice.lower() == "n":
                shall_continue = False
                print("")
                break
            else:
                print(colored(" [!] Invalid choice entered.", "light_red"))
                continue




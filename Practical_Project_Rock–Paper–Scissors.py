from colorama import Fore, Back
import random
rock = "Rock"
paper = "Paper"
scissors = "Scissors"
player_count = 0
computer_count = 0
while True:
    player_move = input("Choose [r]ock, [p]aper, [s]cissors: ")
    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    computer_move = random.randint(1, 3)
    if computer_move == 1:
        computer_move = rock
    elif computer_move == 2:
        computer_move = paper
    elif computer_move == 3:
        computer_move = scissors
    print(Fore.GREEN + f"The computer chose {computer_move}.")
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        print(Fore.BLUE + "You win!")
        player_count += 1
    elif (computer_move == rock and player_move == scissors) or \
            (computer_move == paper and player_move == rock) or \
            (computer_move == scissors and player_move == paper):
        print(Fore.RED + "You lose!")
        computer_count += 1
    else:
        print(Fore.YELLOW + "Draw!")
    print(Fore.RESET + f"Current score is player: {player_count}, computer: {computer_count}")
    decision = input("Type [y] to Play Again or [n] to quit: ")
    if decision == "y":
        continue
    elif decision == "n":
        print(Back.WHITE + Fore.BLACK + "Thank you for playing!")
        break
print(f"Final score is player: {player_count}, computer: {computer_count}")





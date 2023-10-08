import random

class bcolors :
    RED = "\033[91m",
    GREEN = "\033[92m",
    YELLOW = "\033[93m",
    BLUE = "\033[94m",
    RESET = "\033[0m",
    #reset: resets to default color


user_input = input("Rock, Paper, Scissors? ")

if user_input.strip() == "1" or user_input.strip().lower() == "r" or user_input.strip().lower() == "rock":
    user_input = "Rock"
elif user_input.strip() == "2" or user_input.strip().lower() == "p" or user_input.strip().lower() == "paper":
    user_input = "Paper"
elif user_input.strip() == "3" or user_input.strip().lower() == "s" or user_input.strip().lower() == "scissors":
    user_input = "Scissors"

#print(f"You've chosen {bcolors.BLUE}{user_input}{bcolors.RESET}")
#for some reason colors don't work for me 

randomlist = ['Rock','Paper','Scissors']

try:
    with open("additional/rpsscore.txt", "r") as score_file:
        scores = score_file.read().split()
        if len(scores) == 3:
            totplcount, totcomcount, totdrawcount = map(int, scores)
            print(f"Previous session restored: Wins: {totplcount}, Losses: {totcomcount}, Draws: {totdrawcount}")
except FileNotFoundError:
    totcomcount = 0
    totplcount = 0
    totdrawcount = 0
    print(f"No previous session could be found: Wins: {totplcount}, Losses: {totcomcount}, Draws: {totdrawcount}")

comcount = 0
plcount = 0
drawcount = 0
while True:
    if user_input != "Invalid Input":
        compick = random.choice(randomlist)

        if user_input.strip() == "1" or user_input.strip().lower() == "r" or user_input.strip().lower() == "rock":
            user_input = "Rock"
        elif user_input.strip() == "2" or user_input.strip().lower() == "p" or user_input.strip().lower() == "paper":
            user_input = "Paper"
        elif user_input.strip() == "3" or user_input.strip().lower() == "s" or user_input.strip().lower() == "scissors":
            user_input = "Scissors"
        else:
            print("Invalid input")

        print(f"You've chosen {user_input}")
        print(f"The computer has picked: {compick}")

        if user_input == compick:
            print("Draw!")
            drawcount += 1
        elif user_input.lower() == "rock" and compick.lower() == "scissors":
            print("User wins!")
            plcount += 1
        elif user_input.lower() == "paper" and compick.lower() == "rock":
            print("User wins!")
            plcount += 1
        elif user_input.lower() == "scissors" and compick.lower() == "paper":
            print("User wins!")
            plcount += 1
        elif user_input.lower() == "rock" and compick.lower() == "paper":
            print("Computer wins!")
            comcount += 1
        elif user_input.lower() == "paper" and compick.lower() == "scissors":
            print("Computer wins!")
            comcount += 1
        elif user_input.lower() == "scissors" and compick.lower() == "rock":
            print("Computer wins!")
            comcount += 1

    print(f'Player: {plcount} - Computer: {comcount} - Draws: {drawcount}')

    play_again = input("Play again? (yes/no): ")
    if play_again.strip().lower() == "yes":
        user_input = input("Rock, Paper, Scissors? ")
    elif play_again.strip().lower() == "no" or play_again.strip().lower() == "exit" or play_again.strip().lower() == "quit" or play_again.strip().lower() == "cancel":
        break

totplcount += plcount
totcomcount += comcount
totdrawcount += drawcount

with open("additional/rpsscore.txt", "w") as score_file:
    score_file.write(f"{totplcount} {totcomcount} {totdrawcount}")

print(f'Your total Wins: {totplcount}, Losses: {totcomcount}, Draws made with computer: {totdrawcount}')
# simple scissors paper rock game
# computers choice is random
# scissors (0) beats paper (1) beats rock (2) beats scissors (0)

import random

print("Welcome to Scissors Paper Rock!!!!")

humanChoice = ""
humanChoiceNum = -2
while (humanChoiceNum < 0):
    humanChoice = input("Please choose your input, type \"end\" to end the game: ")

    if (humanChoice.lower() == "rock" or humanChoice.lower() == "r"):
        humanChoiceNum = 2
        humanChoice = "Rock"
    elif(humanChoice.lower() == "scissors" or humanChoice.lower() == "s"):
        humanChoiceNum = 0
        humanChoice = "Scissors"
    elif(humanChoice.lower() == "paper" or humanChoice.lower() == "p"):
        humanChoiceNum = 1
        humanChoice = "Paper"
    elif(humanChoice.lower() == "end"):
        exit()
    else:
        print("Please give a valid input")
        

print("Your choice was: " + humanChoice)

computerChoiceNum = random.randint(0,2)
# computerChoiceNum = 2
if (computerChoiceNum == 0):
    computerChoice = "Scissors"
elif (computerChoiceNum == 1):
    computerChoice = "Paper"
elif (computerChoiceNum == 2):
    computerChoice = "Rock"
print("I choose " + computerChoice)

# if subtract human from computer
# rock (2)
minus = computerChoiceNum - humanChoiceNum

if (minus == 0):
    print("It's a draw!")
elif (minus == 1 or minus == -2):
    print("You won")
elif (minus == -1 or minus == 2):
    print ("I won")
    
# print(minus)

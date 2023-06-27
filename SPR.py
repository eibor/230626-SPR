# simple scissors paper rock game
# computers choice is random
# scissors (0) beats paper (1) beats rock (2) beats scissors (0)

import random

def setChoice(numChoice, strChoice):
    retChoice = [numChoice]
    if (numChoice < 0 or numChoice > 2):
        # take strChoice 
        if (strChoice.lower() == "rock" or strChoice.lower() == "r"):
            retChoice[0] = 2
            retChoice.append("Rock")
        elif(strChoice.lower() == "scissors" or strChoice.lower() == "s"):
            retChoice[0] = 0
            retChoice.append("Scissors")
        elif(strChoice.lower() == "paper" or strChoice.lower() == "p"):
            retChoice[0] = 1
            retChoice.append("Paper")
        elif(strChoice.lower() == "end"):
            print("Thanks for playing!")
            exit()
        else:
            print("Please give a valid input")
    # take numChoice
    elif (numChoice == 0):
        retChoice[0] = 0
        retChoice.append("Scissors")
    elif (numChoice == 1):
        retChoice[0] = 1
        retChoice.append("Paper")
    else:
        retChoice[0] = 2
        retChoice.append("Rock")

    return retChoice

# begin main line

print("Welcome to Scissors Paper Rock!!!!")
while (True):
    humanChoice = ""
    humanChoiceNum = -2
    while (humanChoiceNum < 0):
        humanChoice = input("Please choose your input, type \"end\" to end the game: ")

        [humanChoiceNum, humanChoice] = setChoice(-1, humanChoice)
            

    print("Your choice was: " + humanChoice)

    # computerChoiceNum = random.randint(0,2)
    # computerChoiceNum = 2
    # if (computerChoiceNum == 0):
    #     computerChoice = "Scissors"
    # elif (computerChoiceNum == 1):
    #     computerChoice = "Paper"
    # elif (computerChoiceNum == 2):
    #     computerChoice = "Rock"
    [computerChoiceNum, computerChoice] = setChoice(random.randint(0,2),"")
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

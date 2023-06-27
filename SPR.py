# simple scissors paper rock game
# computers choice is random
# logic is: scissors (0) beats paper (1) beats rock (2) beats scissors (0)

import random

# I thought writing this as a function would make it simpler 
# it did not
def setChoice(numChoice, strChoice):
    retChoice = [numChoice,""]
    if (numChoice < 0 or numChoice > 2):
        # take strChoice 
        if (strChoice.lower() == "rock" or strChoice.lower() == "r"):
            retChoice = [2, "Rock"]
        elif(strChoice.lower() == "scissors" or strChoice.lower() == "s"):
            retChoice = [0, "Scissors"]
        elif(strChoice.lower() == "paper" or strChoice.lower() == "p"):
            retChoice = [1, "Paper"]
        elif(strChoice.lower() == "end"):
            print("Thanks for playing!")
            exit()
        else:
            print("Please give a valid input")
    # take numChoice
    elif (numChoice == 0):
        retChoice = [0, "Scissors"]
    elif (numChoice == 1):
        retChoice = [1, "Paper"]
    else:
        retChoice = [2, "Rock"]

    return retChoice

# begin main line
# only way to end it is by typing end

count = [0,0]
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

    minus = computerChoiceNum - humanChoiceNum

    if (minus == 0):
        print("It's a draw!")
    elif (minus == 1 or minus == -2):
        print("You won")
        count[0] += 1
    elif (minus == -1 or minus == 2):
        print ("I won")
        count[1] += 1
    
    print("Score is computer: " + str(count[1]) + " human: " + str(count[0]))
    print()
        
    # print(minus)

import random
active = True
dice = {"d100":100,
        "d20":20,
        "d12":12,
        "d10":10,
        "d8":8,
        "d6":6,
        "d4":4}

# While loop for rolling dice as indicated in the dice set above
# Asks the user if they would like to roll some dice and upon answering "y", the user is then asked to indicate which dice they want to roll
while active:
    roll_dice = input("Would you like to roll some dice? (y/n) ")
    if roll_dice.lower() == "y":
        while active:
            roll = input("What dice do you want to roll? \nd100 \nd20 \nd12 \nd10 \nd8 \nd6 \nd4 \n")
            max = dice[roll]
            if max:
                print(random.randint(1,max))
            else:
                print("Not a valid die!")
            
            roll_again = input("Would you like to roll again? (y/n) ") #Clean this section for misinputs to loop back to this question if the expect result(s) are not retrieved 
            if roll_again.lower() != "y":
                print("Thanks for rolling!")
                active = False

# If the user answered "n" then the program will end.
    elif roll_dice.lower() == "n":
        print("Please comeback when you are ready to roll!")
        active = False
        
# However if the user does not answer "y" or "n", the will be informed the the input in not understood
# The user will then be asked again if they want to roll dice
    elif roll_dice.lower() != "y" or "n":
        print("I dont understand")
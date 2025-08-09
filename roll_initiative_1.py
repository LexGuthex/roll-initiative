import random
active = True

while active:
    roll_dice = input("Would you like to roll some dice? (y/n) ")
    if roll_dice.lower() == "y":
        while active:
            dice = input("What dice do you want to roll? \nd100 \nd20 \nd12 \nd10 \nd8 \nd6 \nd4 \n")
            if dice.lower() == "d100":
                print(random.randint(1, 100))
            elif dice.lower() == "d20":
                print(random.randint(1, 20))
            elif dice.lower() == "d12":
                print(random.randint(1, 12))
            elif dice.lower() == "d10":
                print(random.randint(1, 10))
            elif dice.lower() == "d8":
                print(random.randint(1, 8))
            elif dice.lower() == "d6":
                print(random.randint(1, 6))
            elif dice.lower() == "d4":
                print(random.randint(1, 4))
            else:
                print("Not a valid die!")
            
            # Clean this section for misinputs to loop back to this question if the expect result(s) are not retrieved    
            roll_again = input("Would you like to roll again? (y/n) ")
            if roll_again.lower() != "y":
                print("Thanks for rolling!")
                active = False

    elif roll_dice.lower() == "n":
        print("Please comeback when you are ready to roll!")
        active = False
    elif roll_dice.lower() != "y" or "n":
        print("I dont understand")
# Initializing
yes_no = ["yes", "no"]
directions = ["left", "right", "forward", "backward"]

# Intro
playername = input("What is your name, adventurer?\n")
print("Greetings, " + playername + ". Lets start the adventure!")
print("You are on the edge of a dense forest.")
print("Can you find your way through?\n")

# GAME Begins
entry = ""
while entry not in yes_no:
    entry = input("Would you like to step into the forest?\nyes/no\n")           #asked whether interested to play the game or not
    if entry == "yes":
        print("You head into the forest. You hear crows cawing in the distance.\n")
    elif entry == "no":
        print("You are not ready for this quest. Goodbye, " + playername + ".")
        quit()
    else:
        print("I didn't understand that.\n")

# Game proceeds
entry = ""
while entry not in directions:
    print("To your left, you see a bear.")                  #situation is explained
    print("To your right, there is more forest.")
    print("There is a rock wall directly in front of you.")
    print("Behind you is the forest exit.\n")
    entry = input("What direction do you move?\nleft/right/forward/backward\n")
    if entry == "left":                                             #corresponding action is taken
        print("The bear eats you. Farewell, " + playername + ".")
        quit()
    elif entry == "right":
        print("You head deeper into the forest.\n")
    elif entry == "forward":
        print("You cannot scale the wall.\n")
        entry = ""
    elif entry == "backward":
        print("You leave the forest. Goodbye, " + playername + ".")
        quit()
    else:
        print("I didn't understand that.\n")                           #game ends

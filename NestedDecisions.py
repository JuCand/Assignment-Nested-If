# Task 1 Code Correction 

#place = input("Choose a place: forest or cave? ")

#if place = "forest":
#    action = input("climb a tree or cross a river?")
#    if action = "climb a tree":
#        print("You found a bird's nest!")
#    else action = "cross a river":
#        print("You found a boat!")
#elif place = "cave":
#    print("You find a hidden treasure!")

# Task 2 Setting the scene 
# Based on your corrected code from Task 1, expand the game. If the user chooses "cave", ask them if they want to "light a torch" or "proceed in the dark",
# and provide outcomes for each decision.

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass    
elif place == "cave":
    action2 = input("light a torch or proceed in the dark?")
    if action2 == "light a torch":
        print("You find a hidden treasure!")
    elif action2 == "proceed in the dark":
        print("You have fallen into a hole!")
    else:
        pass
else:
    pass





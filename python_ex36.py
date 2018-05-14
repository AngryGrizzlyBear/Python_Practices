# The goal of this game is to keep you from progressing. 
# Don't be afraid! Otherwise, you're going home.

from sys import exit

def right_road():
    print "You've decided to go down the right road."
    print "As you walk, you've discovered a hole in the middle of the road. What do you do?"
    print "Please select your answer. \nA. Jump over the hole.\nB. Jump in the hole.\nC. Turn around."

    next = raw_input("> ")

    if next == "A".lower() or next == "Jump over the hole.".lower():
        print "The hole expands as you jump over. You barely manage to grab the edge."
        print "You successfully pull yourself up and dust yourself off. What do you do?"
        print "Please select your answer. \nA. Continue.\nB. Go back home."
        
        next = raw_input("> ")
        
        if next == "A".lower() or next == "Continue".lower():
            print "You continue on down the road."
            end_of_gane()
        elif next == "B".lower() or next == "Go back home".lower():
            print "Realizing the danger, you decide to go back home and call it a day."
        else: 
            game_over()
    elif next == "B".lower() or next == "Jump in the hole.".lower():
        print "The hole expands, swallowing you whole."
        print "After spending countless hours in the hole, the ground decides to spit you back out."
        game_over("Covered in oil, dirt, and junk, you're contemplating on whether or not you want to continue. In fact, you've decided.")
    elif next == "C".lower() or next == "Go back home.".lower():
        print "You've decided that you should'nt even be here. You've made the decision to go home, safely."
    else:
        game_over("You're terrible.")

def middle_road():
    print "You've decided to go down the middle road."
    print "Immediately, you see a cat stuck in a tree."
    print "Please select your answer. \nA. Help the cat.\nB. Walk past the cat."
    cat_helped = False

    while True:
        next = raw_input("> ")

        if next == "A".lower():
            print "You help the cat. The cat looks worried. What do you do?"
            cat_helped = True
            print "Choose your answer."       
        
        

def start():
    print "You're traveling down a road."
    print "You come across three paths."
    print "You have three choices. Which Path do you take?"
    print "Please select your answer.\nA. Right Road.\nB. Middle Road.\nC. Left Road."

    next = raw_input("> ")

    if next == "A".lower() or next == "Right Road".lower():
        print "You have chosen to go down the right road."
        right_road()
    elif next == "B".lower() or next == "Middle Road".lower():
        print "You have chosen to go down the middle road."
        middle_road()
    elif next == "C".lower() or next == "Left Road".lower():
        print "You have chosen to down the left road."
    else: 
        game_over()

def game_over(why):
    print why, "You're too scared to progress. You turn around and go home."
    exit(0)

def end_of_gane():
    print "You've come to the end of your journey."
    print "You find a diamond lying still in the floor."
    print "You take it home, sell it, and make a lot of money. Good job!"
    exit(0)


start()
# The goal of this game is to keep you from progressing. 
# Don't be afraid! Otherwise, you're going home.

from sys import exit

def start():
    print "You're traveling down a road."
    print "You come across three paths."
    print "You have three choices. Which Path do you take?"
    print "Please select your answer.\nA. Right Road.\nB. Middle Road.\nC. Left Road."

    next = raw_input("> ")

    if next == "A".lower() or next == "Right Road".lower():
        print "You have chosen to go down the right road."
    elif next == "B".lower() or next == "Middle Road".lower():
        print "You have chosen to go down the middle road."
    elif next == "C".lower() or next == "Left Road".lower():
        print "You have chosen to down the left road."
    else: 
        game_over()

def game_over():
    print "You're too scared to progress. You turn around and go home."

start()
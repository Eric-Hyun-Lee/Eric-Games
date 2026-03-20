#both pigs on the same side - 1 point - called Siders
#one pig on its back - 5 points - Razorback
#one pig on its feet - 5 points - Trotter
#one pig on its nose - 10 points - Snouter
#one pig on its ear - 15 points - Leaning Jowler
#combination of any two of the last four possibilities - add the points - Mixed Combo
#both pigs on backs - 20 points - Double Razorback
#both pigs on feet - 20 points - Double Trotter
#oth pigs on noses - 40 points - Double Snouter
#both pigs on ears - 60 points - Double Leaning Jowler
#pigs on opposite sides - 0 points - Pig Out

#From wikipedia:
#left side - 35%
#right side - 30%
#back - 22%
#feet - 9%
#nose - 3%
#ear - 1%
import random

def roll_pig():
    '''roll_pig() -> str
    rolls a pig, returns its side'''
    rollnum = random.random()  # rand number between 0 and 1
    if rollnum < 0.35:  # 35%
        return 'left'
    elif rollnum < 0.65: # next 30%
        return 'right'
    elif rollnum < 0.87: # next 22%
        return 'back'
    elif rollnum < 0.96: # next 9%
        return 'feet'
    elif rollnum < 0.99: # next 3%
        return 'nose'
    else: # last 1%
        return 'ear'

def roll_two_pigs():
    '''roll_two_pigs() -> (str, str, int)
    rolls two pigs
    returns the two rolls and the score'''
    # roll two pigs
    pig1 = roll_pig()
    pig2 = roll_pig()

    # compute score
    scores = {'left': 0, 'right': 0, 'back': 5, 'feet': 5, 'nose': 10, 'ear': 15}
    score = scores[pig1] + scores[pig2]

    # deal with special cases
    if pig1 == pig2:
        score *= 2  # double score for pigs landing the same way

        # check for siders
        if score == 0:
            score = 1

    return (pig1, pig2, score)

def set_up_game():
    '''set_up_game() -> list
    returns a list of players' names'''
    # Get number of players
    numPlayers = ''
    while not numPlayers.isdigit(): # loop until we get a number
        numPlayers = input("How many players: ")
    numPlayers = int(numPlayers) # convert input string to int

    playerList = []  # initialize list of players

    # get player data
    for n in range(numPlayers):
        name = input("Player " + str(n + 1) + ", enter your name: ")
        playerList.append(name)

    return playerList
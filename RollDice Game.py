# 
# Name: Saman Rastgar
# Script name: Roll Dic part 2
# Description: Making a game that consist of two players playing roll dices 
# DATE: June 16 2020
#

import random

def roll(numSides):
    if numSides>0 and numSides<64:
        result=random.randint(1,numSides)
        return result
    else:
        print("at least one of the numbers is not in range of 0 to 64")
        return -1
    

playerOne=roll(32) # player 1 enters
playerTwo=roll(32) # player 2 enters

def Comparison(playerOne,playerTwo):
    if playerOne>playerTwo and 0<(playerOne and playerTwo)<64:
        print("player one Won with "+str(playerOne))
        print("player two lost with "+str(playerTwo))
    elif playerOne<playerTwo and 0<(playerOne and playerTwo)<64:
        print("player two Won with "+str(playerTwo))
        print("player one Lost with "+str(playerOne))
    elif playerOne==playerTwo and 0<(playerOne and playerTwo)<64:
        print("It's a tie")
    else:
        print("Check the numbers entered")

Comparison(playerOne,playerTwo)

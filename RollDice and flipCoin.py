# 
# Name: Saman Rastgar
# Script name:  Roll the Dice game plus the coin flip 
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
    

playerOne=roll(6)
playerTwo=roll(6)



def Comparison(playerOne,playerTwo):
    if playerOne>playerTwo and 0<(playerOne and playerTwo)<64:
        print("player one Won with "+str(playerOne))
        print("player two lost with "+str(playerTwo))
    elif playerOne<playerTwo and 0<(playerOne and playerTwo)<64:
        print("player two Won with "+str(playerTwo))
        print("player one Lost with "+str(playerOne))
    elif playerOne==playerTwo and 0<(playerOne and playerTwo)<64:
        print("It's tie so we flip the coin instead")
        tossCoin()
    else:
        print(playerOne,playerTwo)
        print("We Check the numbers entered")

def tossCoin():
     toss=random.randint(1,2)
     if(toss==1):
         print("It's head so player 1 wins ")
     if(toss==2):
         print("It's tail so player 2 wins")
     
Comparison(playerOne,playerTwo)


    

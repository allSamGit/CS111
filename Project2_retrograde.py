# Author:  Saman Rastgar
# Date:  6/20/2020
# Description:  Retro Arcade program to make lists of games contain Dice,Slots and Madlib


import random
from datetime import datetime

# Parameters
#   name - Name of the current player
#
# Returns
#   True - Player Wins
#   False - Player Loses
def playGameOfDice(name): 


        print(name+" welcome to Dice game.\n")
        playerScore=0
        computerScore=0

        while( playerScore<5 and computerScore<5):

          print("playerScore: "+str(playerScore))
          print("computerScore: "+str(computerScore))

          enter=input("\nPress enter to roll...")
                
          random.seed(datetime.now())
          playerRoll=random.randint(1,6)
          computerRoll=random.randint(1,6)

          if(playerRoll>computerRoll):
             playerScore+=1
             print(name+" Wins!")
             
          elif(playerRoll<computerRoll):
             computerScore+=1
             print("Computer Wins!")
             
          else:
             print("It's tie")

        print("playerScore: "+str(playerScore))
        print("computerScore: "+str(computerScore))
             

        if(playerScore>computerScore):
          return True
        else:
          return False


# Parameters
#   name - Name of the current player
#
# Returns
#   True - Player Wins
#   False - Player Loses
def playGameOfSlots(name):

    symbolList = ["Cherry", "Lemon", "Seven", "Diamond", "Heart"]
    
    print(name+" Welcome to the Slots game")

    attempts=0
    playerHasWon=False
    
    while(attempts<5 and playerHasWon==False):

        print("Number of attempts : "+str(attempts)+"\n")
        enterPressed=input("Press enter to pull the handle")

        firstChoice=random.choice(symbolList)
        secondChoice=random.choice(symbolList)
        thirdChoice=random.choice(symbolList)
        
        print(firstChoice+"    "+secondChoice+"    "+thirdChoice+"\n") 

        if(firstChoice==secondChoice==thirdChoice):
            playerHasWon=True

        attempts+=1

    return playerHasWon 



#no parameter
#
#
# Returns
# madlib paragraph 
def generateMadlib():

    #    Add additional lists as necessary.
    tasteList = ['Sweet','Salty','Yummy','Fluffy','Dry','Hot']
    activityList = ['boating','camping','dancing','painting','fishing','swimming' ]
    adverbList = ['Randomly','Expertly','Weirdly','Beautifully','Willfully','Quickly']
    exclamationList = ['Hmm','Oops','Yeah','Ahh',' ugh','Oh dear!']
    moodList = ['Sad','upset','annoyed','angry','frustrated','confused']
    placeList = ['castle','cave','your room','bathroom','relaxing chair','beach']

    #six randomly chosen variables from the list
    taste=random.choice(tasteList)
    activity=random.choice(activityList)
    tone=random.choice(adverbList)
    reaction=random.choice(exclamationList)
    mood=random.choice(moodList)
    place=random.choice(placeList)
    

    # Setup the output string that will contain the Madlib
    output = playerName+"...This is your Story\n"

    output += "You are reaching to kitchen Closet to make some "+taste+" Breakfast.\n"
    output += "Then you recieve a call from your friend asking you if you are interested to go "+activity+" with her.\n"
    output += "While you guys are in "+activity+" You told her you feel sick and you ask her if she can give you ride back home.\n"
    output += "You apologize to her and you ask her "+tone+" if you can arrange it for some other time.\n"
    output += reaction+" You forgot that your phone was on speaker so she heard you laughing with your other friend about how you ditched her."
    output += "You realize this and now you are "+mood+" but your friend doesn't want to talk to you anymore."
    output += "All of your story is taking place in "+place+" While you are working on one of your book chapters."

    # Return generated Madlib
    return output

#parameter-player name
#
#Returns nothing
#Prints the generated madlib
#
def createMadlib(name):

    print(name+" Welcome to the Madlib game.\n")
    input("press Enter to generate Madlib...\n")
    generateMadlib()
    print(generateMadlib())


#
# Display the winner for the current game
#
# Parameter
#  name - The name of the winner
#
def displayWinner(name):
    # Display the winner!
    winnerString = "*  " + name + " Wins!  *"
    starBorder = "*" * len(winnerString)
    print(starBorder)
    print(winnerString)
    print(starBorder)



###
# Custom function
# Checks if the game function returns true Then it returns the player's name
# uses the display winner function
###
def displayResult(playerName,Winner):
        
  if(Winner==True):
     displayWinner(playerName)
  else:
     #winnerString = "*  Computer Wins!  *"
     playerName="Computer"
     displayWinner(playerName)  



balance=100

playerName=input("Enter your name please:")
print("\n") 
print(playerName+" Welcome to Retro Arcade!")  

while ( balance > 0 ):
        
    print("(D)ice Game")
    print("(S)lots Game")
    print("(M)adlib Game")
    print("(Q)uit")
        
    print("Your balance is: "+str(balance)+"\n")     

    selection=input("Select one from the above menu:")

    if(selection=='D'):
        diceWinner=playGameOfDice(playerName)
        displayResult(playerName,diceWinner)
        balance-=10
    elif(selection=='S'):
        slotWinner=playGameOfSlots(playerName)
        displayResult(playerName,slotWinner)
        balance-=10           
    elif(selection=='M'):
        createMadlib(playerName)
        balance+=20
    elif(selection=='Q'):
        break


print("Game Over...Thanks for playing")
        


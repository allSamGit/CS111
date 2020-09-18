# Author:  Saman Rastgar    
# Date:  6/20/20
# Description:  Retro Arcade - Component One - Dice Game


# Step 1. Import required libraries
import random
from datetime import datetime

#
# This game is player vs computer where each take turns rolling a single six-sided
#    die.  The player with the highest roll each round wins a point.  The computer
#    receives the point for a tie.  The first player to 5 points wins.
#
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
             print(name+" Wins!")
             playerScore+=1
          elif(playerRoll<computerRoll):
             print("Computer Wins!")
             computerScore+=1
          else:
             print("It's tie")
             

        if(playerScore>computerScore):
          return True
        else:
          return False

######################################################################
# The code below this comment is what runs the program.  Please      #
#   take the time to look at how your function is being called and   #
#   what is being done with the return value, but you do not need    #
#   to modify this code to complete the component.                   #
######################################################################
        
# Setup a default player
playerName = "Bob"

# Call the function and store the result
playerWins = playGameOfDice(playerName)

# Display the winner!
if playerWins == True:
    winnerString = "*  " + playerName + " Wins!  *"
else:
    winnerString = "*  computer Wins!  *"
    
starBorder = "*" * len(winnerString)
print(starBorder)
print(winnerString)
print(starBorder)
    
    

    
 








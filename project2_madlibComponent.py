# Author:  
# Date:  
# Description:  Retro Arcade - Component Three - Madlib Game

# Step 1: Import required libraries
import random

# Step 2: Copy your generateMadlib() function from Madlib MiniTask and past it here

def generateMadlib():
    # Step 1. Define List variables for each category in your Madlib.
    #    Add additional lists as necessary.
    adjList = ['Sweet','Salty','Yummy','Fluffy','Dry','Hot']
    nounList = ['boating','camping','dancing','painting','fishing','swimming' ]
    adverbList = ['Randomly','Expertly','Weirdly','Beautifully','Willfully','Quickly']
    exclamationList = ['Hmm','Oops','Yeah','Ahh',' ugh','Oh dear!']

    taste=random.choice(adjList)
    activity=random.choice(nounList)
    tone=random.choice(adverbList)
    reaction=random.choice(exclamationList)


    # Setup the output string that will contain the Madlib
    output = playerName+"...This is your Story\n"

    # Step 2. Write your Madlib below using String concatination and the random.choice() function
    output += "You are reaching to kitchen Closet to make some "+taste+" Breakfast.\n"
    output += "Then you recieve a call from your friend asking you if you are interested to go "+activity+" with her.\n"
    output += "While you guys are in "+activity+" You told her you feel sick and you ask her if she can give you ride back home.\n"
    output += "You apologize to her and you ask her "+tone+" if you can arrange it for some other time.\n"
    output += reaction+" You forgot that your phone was on speaker so she heard you laughing with your other friend about how you ditched her."

    # Return generated Madlib
    return output

#
# The createMadlib() function allows us to demonstrate code-reuse by utilizing
#   the generateMadlib() function we wrote in class.  This function displays
#   a welcome message to the player, prompts them, generates the madlib and 
#   prints it.
#
# Parameters
#   name - Name of the current player
#
# Returns
#   nothing
def createMadlib(name):

    # Step 3: The game should begin by displaying a welcome message including the
    #    name of the game (Madlib) and the players name.
    print(name+" Welcome to the Madlib game.\n")

    # Step 4: Prompt the player to Press Enter to generate the Madlib
    input("press Enter to generate Madlib...\n")

    # Step 5: Call the generateMadlib() function and store the result to a variable
    generateMadlib()

    # Step 6: Print the generated Madlib
    print(generateMadlib())


######################################################################
# The code below this comment is what runs the program.  Please      #
#   take the time to look at how your function is being called and   #
#   what is being done with the return value, but you do not need    #
#   to modify this code to complete the component.                   #
######################################################################             
        
# Setup a default player
playerName = "Bob"

# Call the function to create a Madlib
createMadlib(playerName)

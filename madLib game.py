#
# Author: Saman Rastgar
# Date: 6/18/20
# Description: We are playing a game where the words are random
#  and you have to make an story based on the words.There is an added while loop
#  to ask the player if they want to play the game again.
#
# This Madlib will require the following categories
#  adj  - http://examples.yourdictionary.com/examples-of-adjectives.html
#  noun  - http://examples.yourdictionary.com/noun-examples.html
#  adverb  - http://examples.yourdictionary.com/examples-of-adverbs.html
#  exclamation  - http://examples.yourdictionary.com/examples-of-interjections.html

import random

#
# This function is an implementation of the <REPLACE WITH MADLIB NAME> Madlib.
#   It will dynamically generate a new Madlib each time it is called by
#   randomly selecting values from the above lists
# Return
# This function will return a String containing the new Madlib

playerName="Saman"     #Type your name to start the game

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
# Generate the Madlib
#
madlib = generateMadlib()


#
# Print the Madlib
#
print(madlib)

validResponse = False
playAgain=False

while validResponse == False or playAgain==True:
# Prompt the user for a response
 answer = input("\n Do you want to play again? (Yes/No):")
# Check if user entered a valid response
 if answer.lower() == "yes":
     playAgain = True
     validResponse = True
     print(generateMadlib())
 elif answer.lower() == "no":
     playAgain = False
     validResponse = True
     print("Ok Thank you,Good Bye")
 else:
     print("\nPlease enter either Yes or No")

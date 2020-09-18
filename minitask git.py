#
# Author: 
# Date: 
# Description:
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

playerName="Saman"

def generateMadlib():
    # Step 1. Define List variables for each category in your Madlib.  
    #    Add additional lists as necessary.
    ADJ_LIST = ['Sweet','Salty','Yummy','Fluffy','Dry','Hot']
    NOUN_LIST = ['boating','camping','dancing','painting','fishing','swimming' ]
    ADVERB_LIST = ['Randomly','Expertly','Weirdly','Beautifully','Willfully','Quickly']
    EXCLAMATION_LIST = ['Hmm','Oops','Yeah','Ahh',' ugh','Oh dear!']

    taste=random.choice(ADJ_LIST)
    activity=random.choice(NOUN_LIST)
    tone=random.choice(ADVERB_LIST)
    reaction=random.choice(EXCLAMATION_LIST)
   

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

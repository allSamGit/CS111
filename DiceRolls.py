# 
# Name: Saman Rastgar
# Script name: Dice Rolls
# Description: writing a function that gives us a random number between 1 and 6
# DATE: June 15 2020
#
import random
from datetime import datetime


def roll(numSides):
    
    lower = 1
    upper = 6

    # Randomly select an Integer value within range (inclusive)
    random.seed(datetime.now())
    result = random.randint(lower,numSides)
    return str(result)




print("Your randomly chosen number is: "+ roll(6))

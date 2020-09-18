# 
# Author:Saman Rastgar
# Date: 6/25/20
# Description: Print a song in the list using for loop and in operator
# First we need to read the songs from a CSV file.
#

#
#  Read lines of text from a specified file and create a list of those lines
#    with each line added as a separate String item in the list
#	
# Parameter
#   inputfile - A String with the name of a text file to convert to a Lit
#
# Return
#   A List containing each line from the text file

#This variable is used to intialized on of the songs 
singleSongCSV = "Jimmy Buffett,Songs You Know by Heart,He Went to Paris,209"

#param name of the text file
#
# returns the lines read from the file
#
def getListFromFile (inputFile):
	outputList = []
	try:
		source = open(inputFile,"r")
		outputList =  source.readlines()
		source.close()
	except FileNotFoundError:
		print("Unable to open input file: " + inputFile)

	return outputList

#
# Use the getListFromFile() function to open the song data file
# and store the return value to songList
#
inputFile = "jimmy_buffett-collection.CSV"
songList = getListFromFile(inputFile)

wordSearched ="yes" # word that needs to be searched

#
# Use a for loop, the in operator and the printSong() function 
#   to print each song in the songList that contains the word "cheese"
#param one of the song's name
#
# returns name of the song
def printSong(song):
  print(song)
  
def songFound(song):
   for song in songList:
      if wordSearched in song.lower():
          return song      

if(songFound(singleSongCSV)):      
  printSong(singleSongCSV)
else:
 print("Song with the word \""+wordSearched+"\" not Found")


          

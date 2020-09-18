#
# Author: Saman Rastgar
# Date:  7/1/2020
# Description: Creating a jukebox that has a menu to load,show and find the songs
# in the playlist.


fileResult="" #saving the search result strings in this string then append them to file


#
#  Read lines of text from a specified file and create a list of those lines
#    with each line added as a separate String item in the list
#   
# Parameter
#   inputfile - A String with the name of a text file to convert to a List
#
# Return
#   A List containing each line from the text file
def getListFromFile (inputFile):
    outputList = []
    try:
        source = open(inputFile,"r")
        outputList =  source.readlines()
        source.close()
    except FileNotFoundError:
        print("Unable to open input file: " + inputFile)

    return outputList



# description : prints the shortest and longest song
# param
# minPos: shortest song index
# maxPos : longest song index
def songShortLong(songList,minPos,maxPos):
    if(songList==None or minPos==None or maxPos==None):
        printMenu()
    else:
        if(minPos):
         song=songList[minPos]
         print("\nshortest Song info:")
         printSong(song)
        if(maxPos):
         song=songList[maxPos]
         print("\nlongest Song info:")
         printSong(song)

# description: prints the catalog info
# param
# songList : list of songs 
def printCatalogStats(songList):
    
   totalPlayTime=0  #catalog time
   numSongs=0       
   artistCounter=0
   albumCounter=0
   artistList=[]
   albumList=[]
   durationList=[]
 
   
   for song in songList:
     singleSong=song.split(',')
     numSongs+=1
     playTime=int(singleSong[3])
     totalPlayTime += playTime
     artist=singleSong[0]
     album=singleSong[1]
     duration=singleSong[3]
     duration = duration.rstrip("\n")
     songDuration= int(duration)
     
             
     
     artistList.append(artist)
     albumList.append(album)
     durationList.append(songDuration)
      
   formattedTime=formatTotalTime(totalPlayTime)
   if(durationList==[] or songList==[]):
       print("No file is imported to analyze")
   else:
       shortestSong=min(durationList)
       minPosition = durationList.index(shortestSong)
       longestSong=max(durationList)
       maxPosition = durationList.index(longestSong)
       print("Catalog Statistics: ")
       print("Number of Artists: "+str(numArtist(artistList)))
       print("Number of Albums: "+str(numAlbums(albumList)))
       print("Number of Songs: "+str(numSongs))
       print("Catalog playTime: "+formattedTime)
       songShortLong(songList,minPosition,maxPosition)

    

#description: calculates the number of albums by removing the duplicates of the list
#param
#artistList : list of artist with repetitive albums names
#return size of the list which is equal to number of albums 
def numAlbums(albumList):
    nonRepeatedAlbumList = []
    for i in albumList: 
      if i not in nonRepeatedAlbumList: 
        nonRepeatedAlbumList.append(i)
    [nonRepeatedAlbumList.append(x)
    for x in albumList
      if x not in nonRepeatedAlbumList]
    return len(nonRepeatedAlbumList)

#description: calculates the number of artist by removing the duplicates of the list
#param
#artistList : list of artist with repetitive artist names
#return size of the list which is equal to number of artists 
def numArtist(artistList):
   nonRepeatedArtistList = []
   for i in artistList: 
      if i not in nonRepeatedArtistList: 
        nonRepeatedArtistList.append(i)

      [nonRepeatedArtistList.append(x)
      for x in artistList
       if x not in nonRepeatedArtistList]
      return len(nonRepeatedArtistList)

# description:Finds the song with the query searches and prints the result
#
#param
#  queryString: The keyword you want to search in the songlist
#  songList : List of the songs
#     
def findSongs(queryString, songList):
  for song in songList:
       if queryString in song.lower():
         printSong(song)

# description:Counts the number of matched songs with that query
#
#param
#  queryString: The keyword you want to search in the songlist
#  songList : List of the songs
# 
def countSongs(queryString, songList):
  count=0
  for song in songList:
       if queryString in song.lower():
         count+=1
  return count 
    

# description:takes the seconds and convert it to the formatted mm:ss
# for each song in the songList
#
# returns formatted time to display
def formatTime(seconds):
      
      minutes=int(seconds/60)
      seconds=seconds%60
      formattedTime="{:02d}:{:02d}".format(minutes,seconds)
      return formattedTime

# description:takes the seconds and convert it to the formatted hh:mm:ss
# for the total play time of catalog
#
# returns formatted time to display    
def formatTotalTime(seconds):

    seconds = seconds % (24 * 3600) 
    hours = seconds // 3600  #floor division(rounds the number down)
    seconds %= 3600
    minutes = seconds // 60 
    seconds %= 60
    formattedTime="{:02d}:{:02d}:{:02d}".format(hours,minutes,seconds)
    return formattedTime

# description: prints the song in the nicely formatted
# param
# song : song object in the list format
#
def printSong(song):
      global fileResult
      formattedSong=""
      divider="-"*int((len(song)/2))+"\n"
      print(divider)
      fileResult+=divider
     
      singleSong=song.split(',')
      seconds=int(singleSong[3])
      formattedTime=formatTime(seconds)
   
      #save printSong result to file
      formattedSong += "Artist: "+ singleSong[0]+"\n"
      formattedSong += "Album: "+singleSong[1]+"\n"
      formattedSong += "Title: "+singleSong[2]+"\n"
      formattedSong += "Duration: "+formattedTime+"\n"

      fileResult+=formattedSong #adding the song info to file data
      print(formattedSong)


# description: prints the menu for the jukebox
#  
def printMenu():
    #print menu print out
     print("(L)oad catalog")
     print("(S)earch catalog")
     print("(A)nalyse catalog")
     print("(P)rint catalog")
     print("(Q)uit")
     
# description: writes the search result to the assigned output file
# param
# file name: file name for outputing the search result
# data :search result saved in list format
#
def writeToFile(inputFile,data):
    try:
        source = open(inputFile,"w")
        source.writelines(data)
        print("Result saved in "+inputFile+" file")
        source.close()
    except FileNotFoundError:
        print("Unable to open input file: " + inputFile)

    
# description: takes the strings one by one and appends it to the search result
# param
# string : file result that would be appended
#
def resultAppend(string):
    resultedOutput=[]
    resultedOutput.append(string)
    return resultedOutput

# description: prompts the user if they want to save the result
# and saves it to the specified file if the answer is yes
#
def saveInFile():
         
     response=input("Would you like to save the result(yes/no)?")
     if(response.lower()=="yes"):
       resultFileName=input("Name of the file to log the result: ")
       resultList= resultAppend(fileResult)
       writeToFile(resultFileName,resultList)
     elif(response.lower()=="no"):
       printMenu()


#description: checks if song is not loaded in the program
#param
#songList:list of songs 
def songListChecker(songList):
    if(songList==None):
        print("\nplease load the file first(press L) to load")
        printMenu()

# while loop checking for the user input
# if statements checking to see what the user inputted (L, A, S, Q)   
flag=False
songList=None
while(flag==False):

    entry=input("Please enter a command (press m for Menu):")    
    if(entry.lower()=="m"):        
         printMenu()         
    if(entry.lower()=="l"):
         fileName=input("Enter the file name:")
         songList=getListFromFile(fileName)            
    if(entry.lower()=="s"):

      if songList==None:
         songListChecker(songList)
      else:
         searchQuery=input("Please enter the search query:")
         numOfMatches="Found "+str(countSongs(searchQuery, songList))+" matches."
         fileResult+=numOfMatches
         print(numOfMatches)
         findSongs(searchQuery, songList)
         saveInFile()
         
    if(entry.lower()=="a"):
        if songList==None:
         songListChecker(songList)
        else:
         printCatalogStats(songList)
         
             
    if(entry.lower()=="p"):
         
         if songList==None:
            songListChecker(songList)
         else:
          print("\n********List of all the songs*********\n")
          for song in songList:
           printSong(song)         
    if(entry.lower()=="q"):
         flag=True

print("Leaving Jukebox Hero...  Goodbye!") #This message shows up if the menu entry is q

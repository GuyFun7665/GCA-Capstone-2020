import re
def replace(infile):
    for line in infile:
        try:
            outFile = open("replaced.c","a")
            variables=["local_","uVar","iVar","puVar","ppHVar","pcVar","lVar","pFVar"]
            strip = line.strip()
            print(strip)
        except IOError:
            print("Error opening file")
  
def fileinput():
    try:
        inputFile = open("Testaroo1.c", "r")
        return inputFile
    except IOError:
        print("Error opening file")
    
infile = fileinput()
replace(infile)
import re
def replace(infile):
    for line in infile:
        try:
            outFile = open("replaced.c","a")
            variables=["local_","local_res","uVar","iVar","puVar","ppHVar","pcVar","lVar","pFVar"]
            strip = line.strip()
            
            for index in variables:
                #print index
                pattern = index+'[ab-z]?\d+'
                regexs = re.compile(pattern)
                if regexs.search(strip):
                    strip = regexs.sub("repVar",strip)
            outFile.write(strip+"\n")
        except IOError:
            print("Error opening file")
        outFile.close()
  

  
def fileinput():
    try:
        inputFile = open("Testaroo1.c", "r")
        return inputFile
    except IOError:
        print("Error opening file")
    
infile = fileinput()
replace(infile)
infile.close()


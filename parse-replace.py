import re
def replace(infile):
    for line in infile:
        try:
            outFile = open("replaced.c","r+")
            variables=["local_","local_res","uVar","iVar","puVar","ppHVar","pcVar","lVar","pFVar"]
            strip = line.strip()
            
            for index in variables:
                #print index
                pattern = index+'[ab-z]?\d+'
                regexs = re.compile(pattern)
                if regexs.search(strip):
                    print"Matched"
                    outFile.write(regexs.sub("repVar",strip)+"\n")
                else:
                        outFile.write(strip+"\n")
                        
                        
                        
            #print(strip)
            outFile.close()
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
infile.close()


#read file line by line
#Check line against variable lists
#if line contains a variable name
#strip
#else
#write unlatered line
#go to next line in file
#repeat
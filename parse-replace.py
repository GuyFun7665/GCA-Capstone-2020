import re
def replace(infile):
    outFile = open("replaced.c","w")
    funcPatt = "FUN_"+'[ab-z]?\d+[ab-z]?\d+'
    for line in infile:
        try:
            variables=["local_","local_res","uVar","iVar","puVar","ppHVar","pcVar","lVar","pFVar","pHVar"]
            strip = line.strip()
            for index in variables:
                #print index
                pattern = index+'[ab-z]?\d+'
                if re.search(pattern,strip):
                    strip = re.sub(pattern,"repVar",strip)
                if re.search(funcPatt,strip):
                    strip = re.sub(funcPatt,"repFunc",strip)
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


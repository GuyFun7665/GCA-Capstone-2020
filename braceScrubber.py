import re

def braceRM(infile):
    outFile = open("braced.c","w")
    patt = "\{?\}?"
    regexs = re.compile(patt)
    for line in infile:
        strip = line.strip()
        if regexs.search(strip):
            strip = regexs.sub("",strip)
        outFile.write(strip+"\n")

def fileinput():
    try:
        inputFile = open("Testaroo1.c", "r")
        return inputFile
    except IOError:
        print("Error opening file")
        
        
infile = fileinput()
braceRM(infile)
infile.close()
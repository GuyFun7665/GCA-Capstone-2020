import os
import re

#https://gist.github.com/ChunMinChang/88bfa5842396c1fbbc5b
def comment_remover(text):
    def replacer(match):
        s = match.group(0)
        if s.startswith('/'):
            return "" # note: a space and not an empty string
        else:
            return s
    pattern = re.compile(
        r'//.*?$|/\*.*?\*/|\'(?:\\.|[^\\\'])*\'|"(?:\\.|[^\\"])*"',
        re.DOTALL | re.MULTILINE
    )
    return re.sub(pattern, replacer, text)
    
#Step through all files in directory
def library_scrubber():
    for filename in os.listdir("C Libraries"):
        if filename.endswith(".h"):
            print(os.path.join("C Libraries", filename))
            f=open(os.path.join("C Libraries", filename), "r")
            outfile=open(os.path.join("Scrubbed Libraries", filename), "w")
            #f=open("test.txt","r")
            fileData=(f.read())
            cleanData=(comment_remover(fileData))
            outfile.write(cleanData)
            #print(cleanData)
            #if (file compare) matches:
                #print("potential match with ", filename)
                

def replace():
    try:
        inputFile = open("Testaroo1.c", "r")
    except IOError:
        print("Error opening file")
        
    for line in inputFile:
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
    inputFile.close()
  
  
#Snas a statically set directory for files and sub-directories. 
def compare():
    CLibs = os.listdir("Scrubbed Libraries")
    for scanning in CLibs:
        print("Scanning file ", scanning)
        LineCount=0
        with open('replaced.c', 'r') as FuncFile:
            FileScan = os.path.join("Scrubbed Libraries", scanning)
            with open(FileScan, 'r') as LibFile:
                same = set(FuncFile).intersection(LibFile)
      
            same.discard('\n')

            with open('compareResults.txt', 'a+') as file_out:
                file_out.write("\nMatched lines in "+scanning + "\n\n")
                for line in same:
                    file_out.write(line)
                    LineCount = LineCount+1
                FuncLines = sum(1 for line in open('replaced.c')) 
                MatchedLines = sum(1 for line in open('compareResults.txt')) 
                #wont work with multiple libs. Fix by having a count above then compare.
                CLibLines = sum(1 for line in open(FileScan)) 
                print("Function lines " ,FuncLines)
                print("Library lines " ,CLibLines)
                print("Matched lines " ,LineCount)
                compper = (LineCount/FuncLines)*100 
                #print(LineCount)
                print("Matched Percentage =",compper,"% \n")
             
            

               # file_out=open("compareResults.txt","a+")
                file_out.write("\n \n ANALYSIS: "+str(scanning)+"\n")
                file_out.write("Total lines in the outputted funtion: "+str(FuncLines)+"\n")
                file_out.write("Total matched lines from the function and library: "+str(LineCount)+"\n")
                file_out.write("Matched Percentage = "+str(compper)+"% \n")
    #close the files
    #Do a switch case on examination of percentage e.g. 80% is likely the used folder
    
library_scrubber()
replace()
compare()

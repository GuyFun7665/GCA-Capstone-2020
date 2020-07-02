#TODO write a description for this script
#@author Scott Matheson, Shayne Gradwell, Tyson Jamison
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 

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
    for filename in os.listdir("Capstone\C Libraries"):
        if filename.endswith(".h"):
            print(os.path.join("Capstone\C Libraries", filename))
            f=open(os.path.join("Capstone\C Libraries", filename), "r")
            outfile=open(os.path.join("Capstone\Scrubbed Libraries", filename), "w")
            #f=open("test.txt","r")
            fileData=(f.read())
            cleanData=(comment_remover(fileData))
            outfile.write(cleanData)
            outfile.close()
            f.close()
            #print(cleanData)


def replace():
    outFile=open(os.path.join("Capstone","replaced.c"), "w")
    infile=open("Capstone\Testaroo1.c", "r")
    funcPatt = "FUN_"+'[ab-z]?\d+[ab-z]?\d+'
    for line in infile:
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
    outFile.close()
    infile.close()
  
  
#Snas a statically set directory for files and sub-directories. 
def compare():
    cLibs = os.listdir("Capstone\Scrubbed Libraries")
    for scanning in cLibs:
        print "Scanning file " + scanning
        lineCount=0
        funcLines=0
        cLibLines=0
        funcFile=open(os.path.join("Capstone","replaced.c"), "r")
        for line in funcFile:
            funcLines +=1
        #with open("Capstone\replaced.c", "r") as FuncFile:
        fileScan = os.path.join("Capstone\Scrubbed Libraries", scanning)
        with open(fileScan, 'r') as libFile:
            for line in libFile:
                cLibLines +=1
            same = set(funcFile).intersection(libFile)
  
        same.discard('\n')

        with open('Capstone\compareResults.txt', 'a+') as file_out:
            file_out.write("\nMatched lines in "+scanning + "\n\n")
            for line in same:
                file_out.write(line)
                lineCount = lineCount+1
            #wont work with multiple libs. Fix by having a count above then compare.
            #funcLines = sum(1 for line in open(os.path.join("Capstone","replaced.c"))) 
            #matchedLines = sum(1 for line in open(os.path.join("Capstone","compareResults.txt")) 
            #cLibLines = sum(1 for line in open(fileScan))
            print "Function lines " + str(funcLines)
            print "Library lines " + str(cLibLines)
            print "Matched lines " + str(lineCount)
            compper = (lineCount/funcLines)*100 
            #print(LineCount)
            print "Matched Percentage: " + str(compper) + "% \n"


           # file_out=open("compareResults.txt","a+")
            file_out.write("\n \n ANALYSIS: "+str(scanning)+"\n")
            file_out.write("Total lines in the outputted funtion: "+str(funcLines)+"\n")
            file_out.write("Total matched lines from the function and library: "+str(lineCount)+"\n")
            file_out.write("Matched Percentage = "+str(compper)+"% \n")
        libFile.close()
        funcFile.close()
        file_out.close()
    #close the files
    #Do a switch case on examination of percentage e.g. 80% is likely the used folder

print(os.getcwd())
library_scrubber()
replace()
compare()

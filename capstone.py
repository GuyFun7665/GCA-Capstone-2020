# Ghidra Code Analyzer was developed for analysts to compare decompiled code against known malware and C libraries.
#@author Scott Matheson, Shayne Gradwell, Tyson Jamison
#@category _NEW_
#@keybinding 
#@menupath 
#@toolbar 


import os
import re
import sys
from sets import Set

#ghidra_default_dir = os.getcwd()
#jython_dir = os.path.join(ghidra_default_dir, "Ghidra", "Features", "Python", "lib", "Lib", "site-packages")
#sys.path.insert(0,jython_dir)
#sys.path.append(os.getcwd()+'\Capstone')
#import SplitExports

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
    print "Scrubbing variables in Exported Functions"
    repFiles=os.listdir("Capstone\Exported Functions")
    for file in repFiles:
        outFile=open(os.path.join("Capstone\Scrubbed Functions", file), "w")
        infile=open(os.path.join("Capstone\Exported Functions", file), "r")
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
    print "Done!"
  

def compare():
   # cLibs = os.listdir("Capstone\Scrubbed Libraries") #Gets the files and subdirectories from the specified directory.
    #compFuncs = os.listdir("Capstone\Scrubbed Functions")
    #for scanning in cLibs: #Will loop for every opened library file.
     #   if scanning.startswith("rep"):
      #      scanLibs = os.path.join("Capstone\Scrubbed Libraries", scanning)
       #     for func in compFuncs:
        #        scanFunc = os.path.join("Capstone\Scrubbed Functions", func)
                #with open(scanFunc, 'r') as funcFile, open(scanLibs,'r') as libFile, open('funcPlaceholder.txt','a+') as placeHolder: #Opens Library, Function, and an output text file.
                 #   matchCount = 0
                   # funcLineCount = len(funcFile.readlines(  )) #Counts the total lines within the function. Currently not in use.
                    #funcWordCount = 0
                   # print "Comparing files %s & %s" % (scanLibs, scanFunc)
                    #funcFile.seek(0) #Resets the function to the top of the file.
                    #for funcLine in funcFile:
                     #   funcWords = list(funcLine.split())
                      #  funcWordCount = funcWordCount + len(funcWords) #Counts the total word scanned from the function.
                       # libFile.seek(0) #Resets libFile back to the top of file.
                        
                        #for libLine in libFile:         
                            #libWords = libLine.split()
                            #bracClear = ["{", "}", ]
                            #varMatch = []
                            
                            #BELOW CODE IS TO COMPARES BY INDIVIDUAL WORDS.
                            #funcListLen = list(range(len(funcWords)))  #Takes the range of the length an converts to a list so we can loop through the elements.
                            #libListLen = list(range(len(libWords)))
                            #for i in funcListLen:
                                
                                #bracRem= ["{", "}",] 
                              
                               # for p in libListLen:
                               #     if (funcWords[i:i+1] == bracRem[0:1] or funcWords[i:i+1] == bracRem[1:2]) or funcWords[i:i+1] == bracRem[2:3]:
                                        #This filters out brackets, can be removed once filtered functions are taken in.
                                        #Can use if we still have an issue with blank lines.
                                        
                              #          pass                      
                                    
                             #       elif libWords[p:p+1] in varMatch:
                                        
                            #            pass
                                        
                           #         elif (funcWords == libWords): # Add [i:i+1] to funcWords and [p:p+1] to libWords in order to analyze by individual words.
                          #              matchCount += 1
                         #               placeHolder.write(str(scanning) + "  ")
                        #                placeHolder.write(str(funcWords[p:p+1]) + "  MATCHED IN BOTH FILES "  + str(matchCount) + "\n")
                       #                 varMatch.append(libWords[p:p+1])
                                        
                      #              else:
                     #                   pass
                                    
                    #placeHolder.write("\n\n Results from " + str(scanLibs) + " " + str(scanFunc) + "\n")
                    #placeHolder.write("Matched lines: " + str(matchCount) + " and Total Lines: " + str(funcWordCount) + "\n")
                    #matchPerc = 0.0
                   # matchPerc = (float(matchCount)/float(funcWordCount))*100
                    #print(matchPerc)
                  #  placeHolder.write("Matched Percentage: " + str(matchPerc) + "\n\n")

    cLibs = os.listdir("Capstone\Scrubbed Libraries") #Gets the files and subdirectories from the specified directory.
    compFuncs = os.listdir("Capstone\Scrubbed Functions")
    for scanning in cLibs: #Will loop for every opened library file.
        if scanning.startswith("rep"):
            scanLibs = os.path.join("Capstone\Scrubbed Libraries", scanning)
            for func in compFuncs:
                scanFunc = os.path.join("Capstone\Scrubbed Functions", func)
        
                funcFile = open(scanFunc, 'r')
                libFiles = open(scanLibs, 'r')
                outputTxt = open('CodeAnalyzerResults.txt', 'a+')
                print "Comparing files %s & %s" % (scanLibs, scanFunc)
              
                funcWordCount = 0
                libWordCount = 0
                funcMatch = 0
                matchPercentage = 0.0
                
                funcWords = funcFile.read().split() #Splitting the files into individual words.
                libWords = libFiles.read().split()
                matchedWords = set(funcWords) & set(libWords) #Reading for what words are matched.
                funcWordCount = len(funcWords) #Counting the amount of words.
                libWordCount = len(libWords)
                
                for word in matchedWords:
                    outputTxt.write('MATCHED: {}.  Occurs {} times within the function and {} times within {}.\n' .format(word, funcWords.count(word), libWords.count(word), scanning))
                    
                    
                    if funcWords.count(word) > libWords.count(word): #A loop to exclude multiple matches.
                        funcMatch += libWords.count(word)
                        
                    else:
                        funcMatch += funcWords.count(word)
                    
                outputTxt.write("\nAbove results are from: {} compared against {}\n" .format(func, scanning))
                outputTxt.write("Total words scanned in for comparison = {}\n" .format(libWordCount))
                outputTxt.write("Total matched words in the function = {}\n" .format(funcMatch))
                
                matchPercentage = (float(funcMatch)/float(funcWordCount))*100
               
                outputTxt.write("Matched: {} / {}. Percentage of match is = {}\n\n\n" .format(funcMatch, funcWordCount, round(matchPercentage,2))) 
                
    funcFile.close()
    libFiles.close()
    outputTxt.close()         
#Snas a statically set directory for files and sub-directories. 
#def compare():
#   cLibs = os.listdir("Capstone\Scrubbed Libraries")
#   for scanning in cLibs:
#      print "Scanning file " + scanning
#       lineCount=0
#        funcLines=0
#        cLibLines=0
#        funcDir = os.listdir("Capstone\Exported Functions")
#        #funcFile=open(os.path.join("Capstone","replaced.c"), "r")
#        for func in funcDir:
            # if func.startswith("rep"):
                # funcFile = open(os.path.join("Capstone\Exported Functions", func), "r")
                # for line in funcFile:
                    # funcLines +=1
                # #with open("Capstone\replaced.c", "r") as FuncFile:
                # fileScan = os.path.join("Capstone\Scrubbed Libraries", scanning)
                # with open(fileScan, 'r') as libFile:
                    # for line in libFile:
                        # cLibLines +=1
                    # same=set(funcFile).intersection(libFile)
                # same.discard("\n")
                
                # with open('Capstone\compareResults.txt', 'a+') as file_out:
                    # file_out.write("\nMatched lines in "+scanning + "\n\n")
                    # for line in same:
                        # file_out.write(line)
                        # lineCount = lineCount+1
                    # #wont work with multiple libs. Fix by having a count above then compare.
                    # #funcLines = sum(1 for line in open(os.path.join("Capstone","replaced.c"))) 
                    # #matchedLines = sum(1 for line in open(os.path.join("Capstone","compareResults.txt")) 
                    # #cLibLines = sum(1 for line in open(fileScan))
                    # print "Function lines " + str(funcLines)
                    # print "Library lines " + str(cLibLines)
                    # print "Matched lines " + str(lineCount)
                    # compper = (lineCount/funcLines)*100 
                    # #print(LineCount)
                    # print "Matched Percentage: " + str(compper) + "% \n"


                   # # file_out=open("compareResults.txt","a+")
                    # file_out.write("\n \n ANALYSIS: "+str(scanning)+"\n")
                    # file_out.write("Total lines in the outputted funtion: "+str(funcLines)+"\n")
                    # file_out.write("Total matched lines from the function and library: "+str(lineCount)+"\n")
                    # file_out.write("Matched Percentage = "+str(compper)+"% \n")
                    # funcFile.close()
        # libFile.close()
        # file_out.close()
    #close the files
    #Do a switch case on examination of percentage e.g. 80% is likely the used folder
    
def main():
    userIn = 'a'
    while userIn.lower() != 'q':
        userIn = askString("Action Selection", "Would you like to (S)crub libraries, (R)eplace variables, (C)ompare functions or (Q)uit: ")
        if userIn.lower() == 's':
            library_scrubber()
        elif userIn.lower() == 'r':
            replace()
        elif userIn.lower() == 'c':
            compare()
        elif userIn.lower() == 'q':
            print "Exiting..."
        else:
            popup("Error: Unrecognized input.")

print(os.getcwd())
main()
#SplitExports.run()
#library_scrubber()
# replace()
# compare()

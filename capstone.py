# Ghidra Code Analyzer was developed for analysts to compare decompiled code against known malware and C libraries.
#@author Scott Matheson, Shayne Gradwell, Tyson Jamison
#@category CodeAnalyzer
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
resLik = "X"
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

#Compares the matched percentage against the size of the files.
#A function that is much smaller than the file its being compared against is more likely to have a match and vice versa. 
def enhanced_comparison(sizeComp, matchPercentage): 
    if sizeComp >= 200.00:
        if matchPercentage >= 75.00:
            resLik = "high"
            
        elif matchPercentage >= 50.00:
            resLik = "high "
            
        elif matchPercentage >= 25.00:
            resLik = "medium"
            
        elif matchPercentage >= 10.00:
            resLik = "low"
            
        else:
            resLik = "improbable"
            
    elif sizeComp >= 100.00:
        if matchPercentage >= 75.00:
            resLik = "high"
            
        elif matchPercentage >= 50.00:
            resLik = "medium"
            
        elif matchPercentage >= 25.00:
            resLik = "medium"
            
        elif matchPercentage >= 10.00:
            resLik = "low"
            
        else:
            resLik = "improbable"
            
    elif sizeComp >= 80.00:
        if matchPercentage >= 75.00:
            resLik = "high"
            
        elif matchPercentage >= 50.00:
            resLik = "medium"
            
        elif matchPercentage >= 25.00:
            resLik = "low"
            
        elif matchPercentage >= 10.00:
            resLik = "low"
            
        else:
            resLik = "improbable"
            
    elif sizeComp >= 50.00:
        if matchPercentage >= 75.00:
            resLik = "medium"
            
        elif matchPercentage >= 50.00:
            resLik = "medium"
            
        elif matchPercentage >= 25.00:
            resLik = "low"
            
        elif matchPercentage >= 10.00:
            resLik = "improbable"
            
        else:
            resLik = "improbable"
            
    elif sizeComp >= 25.00:
        if matchPercentage >= 75.00:
            resLik = "medium"
            
        elif matchPercentage >= 50.00:
            resLik = "low"
            
        elif matchPercentage >= 25.00:
            resLik = "low"
            
        elif matchPercentage >= 10.00:
            resLik = "improbable"
            
        else:
            resLik = "improbable"
            
    else:
        if matchPercentage >= 75.00:
            resLik = "low"
            
        elif matchPercentage >= 50.00:
            resLik = "low"
            
        elif matchPercentage >= 25.00:
            resLik = "low"
            
        elif matchPercentage >= 10.00:
            resLik = "improbable"
            
        else:
            resLik = "improbable"
            
    return resLik
    
def compare():

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
              
                remBrac = 0
                funcWordCount = 0
                libWordCount = 0
                funcMatch = 0
                matchPercentage = 0.0
                sizeComp = 0.0
                
                
                funcWords = funcFile.read().split() #Splitting the files into individual words.
                libWords = libFiles.read().split()
                matchedWords = set(funcWords) & set(libWords) #Reading for what words are matched.
                funcWordCount = len(funcWords) #Counting the amount of words.
                libWordCount = len(libWords)
                sizeComp = (float(funcWordCount)/float(libWordCount))*100
                
                for word in matchedWords:
                    if word == '{' or word == '}':
                        if funcWords.count(word) > libWords.count(word): #A loop to exclude brackets.
                            remBrac += libWords.count(word)
                            
                        else:
                            remBrac += funcWords.count(word)
                        
                    else:
                        outputTxt.write('MATCHED: {}  Occurs {} times within the function and {} times within {}.\n' .format(word, funcWords.count(word), libWords.count(word), scanning))
                        
                        
                        if funcWords.count(word) > libWords.count(word): #A loop to exclude multiple matches.
                            funcMatch += libWords.count(word)
                            
                        else:
                            funcMatch += funcWords.count(word)
                
                outputTxt.write("\nAbove results are from: {} compared against {}\n" .format(func, scanning))
                outputTxt.write("Total words scanned in for comparison = {}\n" .format(libWordCount))
                outputTxt.write("Total matched words in the function = {}\n" .format(funcMatch))
                outputTxt.write("Brackets filtered out = {}\n" .format(remBrac))
                
                funcWordCount = funcWordCount - remBrac
                matchPercentage = (float(funcMatch)/float(funcWordCount))*100
                outputTxt.write("Exported function word count: {} and compared file word count: {}\n" .format(funcWordCount, libWordCount))
                outputTxt.write("Matched: {} / {}. Percentage of match is = {}%\n" .format(funcMatch, funcWordCount, round(matchPercentage,2))) 
                outputTxt.write("Likelihood of a match is: {}\n\n\n" .format(enhanced_comparison(sizeComp, matchPercentage)))
    funcFile.close()
    libFiles.close()
    outputTxt.close()         

    
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

#current issue. Sometimes matches a word multiple times. Need to rejig the loop logic.

import os

cLibs = os.listdir('CLibs2Scan\\') #Gets the files and subdirectories from the specified directory.

for scanning in cLibs: #Will loop for every opened library file.
    scanLibs = "CLibs2Scan\\" + scanning
    with open('Test4.c', 'r') as funcFile, open(scanLibs,'r') as libFile, open('funcPlaceholder.txt','a+') as placeHolder: #Opens Library, Function, and an output text file.
        matchCount = 0
        funcLineCount = len(funcFile.readlines(  )) #Counts the total lines within the function. Currently not in use.
        funcWordCount = 0
        print("\nScanning file ", scanLibs, "\n\n")
        funcFile.seek(0) #Resets the function to the top of the file.
        for funcLine in funcFile:
            funcWords = funcLine.split()
            funcWordCount += len(funcWords) #Counts the total word scanned from the function.
            libFile.seek(0) #Resets libFile back to the top of file.
            
            for libLine in libFile:         
                libWords = libLine.split()
                bracClear = ["{", "}", ]

                #BELOW CODE IS TO COMPARES BY INDIVIDUAL WORDS.
                funcListLen = [*range(len(funcWords))]  #Takes the range of the length an converts to a list so we can loop through the elements.
             
                for i in funcListLen:
                  libListLen = [*range(len(libWords))]
                  bracRem= ["{", "}",] 
                  
                  for p in libListLen:
                    if (funcWords[i:i+1] == bracRem[0:1] or funcWords[i:i+1] == bracRem[1:2]) or funcWords[i:i+1] == bracRem[2:3]:
                        #This filters out brackets, can be removed once filtered functions are taken in.
                        #Can use if we still have an issue with blank lines.
                        pass                      
                        
                    elif (funcWords == libWords): # Add [i:i+1] to funcWords and [p:p+1] to libWords in order to analyze by individual words.
                       matchCount += 1
                       placeHolder.write(str(scanning) + "  ")
                       placeHolder.write(str(funcWords[p:p+1]) + "  MATCHED  " + str(libWords[p:p+1]) + "  " + str(matchCount) + "\n")
                        
                    else:
                       pass
                        
        placeHolder.write("\n\n Results from " + str(scanLibs) + "\n")
        placeHolder.write("Matched lines: " + str(matchCount) + " and Total Lines: " + str(funcWordCount) + "\n") 
        placeHolder.write("Matched Percentage: " + str(matchCount/funcWordCount*100) + "\n\n")
           
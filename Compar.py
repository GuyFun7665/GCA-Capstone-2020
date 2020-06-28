import os
#Snas a statically set directory for files and sub-directories. 
CLibs = os.listdir('CLibs2Scan\\')

for scanning in CLibs:
    print("Scanning file ", scanning)
    LineCount=0
    with open('Test4.c', 'r') as FuncFile:
        FileScan = "CLibs2Scan\\" + scanning
        with open(FileScan, 'r') as LibFile:
            same = set(FuncFile).intersection(LibFile)
  
        same.discard('\n')

        with open('compareResults.txt', 'a+') as file_out:
            file_out.write("\nMatched lines in "+scanning + "\n\n")
            for line in same:
                file_out.write(line)
                LineCount = LineCount+1
            FuncLines = sum(1 for line in open('Test4.c')) 
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
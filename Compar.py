#Files are statically set. 


with open('Test4.c', 'r') as FuncFile:

    with open('winnt.h', 'r') as LibFile:
        same = set(FuncFile).intersection(LibFile)
       #Will need to search multiple lib files.
    
same.discard('\n')

with open('compareResults.txt', 'w') as file_out:
    for line in same:
        file_out.write(line)
 
FuncLines = sum(1 for line in open('Test4.c')) 
MatchedLines = sum(1 for line in open('compareResults.txt'))
print("Function lines " ,FuncLines)
print("Matched lines " ,MatchedLines)
compper = MatchedLines/FuncLines
print("Matched Percentage =",compper,"%")


file_out=open("compareResults.txt","a+")
file_out.write("\n \n ANALYSIS: \n")
file_out.write("Total lines in the outputted funtion: "+str(FuncLines)+"\n")
file_out.write("Total matched lines from the function and library: "+str(MatchedLines)+"\n")
file_out.write("Matched Percentage = "+str(compper)+"% \n")

#Do a switch case on examination of percentage e.g. 80% is likely the used folder
#Psuedo code template for the Ghidra Code Analyser (GCA)
# Authors - Scott Matheson, Shayne Gradwell, Tyson Jamieson

#The GCA is a script that will export the functions that are decompiled in Ghidra, export it to a file, and comapre it to existing C libraries. 
#This allows the analyst to identify bodies of code taht might have been pulled from these C libraries, making analysis more streamlined.


def exportFunctions():
    #This function will serve as the expoerter of the decompiled fucntions in Ghidra. 
    #This will be attempted with the decompiler.java script that calls the cppExporter.java, which has functionality to split each function into it's own file on export
    #With this, we hope to export each function to a specific folder
    #Return File names to compare
    
def importCLibraries():
    #This Function serves to import our c libraries for comparison to the decompiled code.
    #So far, we will be reading in all the C libraries for comparison

def sortCompareFunctions():
    #This function provides the functionality to compare the two bodies of code to search for code that is matching.
    #This will probably be done by a text parse, but if we have extra time we can do it by object comparison.
    
    
#Main calls to each function
funcFile = exportFunctions()
importCLibraries()
sortCompareFunctions(funcFile)
#Printing the results to screen, and maybe reading the results out to file.



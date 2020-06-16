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
for filename in os.listdir("C Libraries"):
    if filename.endswith(".h"):
        print(os.path.join("C Libraries", filename))
        f=open(os.path.join("C Libraries", filename), "r")
        #f=open("test.txt","r")
        fileData=(f.read())
        cleanData=(comment_remover(fileData))
        print(cleanData)
        #if (file compare) matches:
            #print("potential match with ", filename)
            


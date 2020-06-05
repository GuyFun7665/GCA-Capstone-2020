import os

#Step through all files in directory
for filename in os.listdir("C Libraries"):
    if filename.endswith(".h"):
        print(os.path.join("C Libraries", filename))
        f=open(os.path.join("C Libraries", filename), "r")
        print(f.read())
        #if (file compare) matches:
            #print("potential match with ", filename)
#madlibs.py

import os, re

#reads a text file and asks for user input anywhere the words 
#ADJECTIVE, NOUN, ADVERB, or VERB are found and replaces each 
#instance with user input. Then prints the replaced text to screen
#and saves the replaced text as a new file.

#Read in a text file
madlib=open(os.path.abspath(".\\Text Files\\Madlib.txt"), "r")
readlib=madlib.read()

#Check the text file for keywords and assign them to a list, to pass for input
madlibRE=re.compile(r'ADJECTIVE|NOUN|ADVERB|VERB')
liblist=madlibRE.findall(readlib)

#Prepare all info to be recombined by making lists
inputcontainer, outputlist, es=[],[], "" #Gotta create those empty variables
for hit in liblist:
    inputcontainer.append(input("Please enter a(n) "+hit+".")) #For each keyword, ask the user for one of those wordtypes
therest=re.split(madlibRE, readlib)

if therest[0]=='':
    for pos in range(len(therest)): outputlist=outputlist+inputcontainer[pos]+therest[pos+1]
else:
    for pos in range(len(therest)-1):outputlist=outputlist+[therest[pos]]+[inputcontainer[pos]]
    outputlist=outputlist+[therest[-1]]
writestr=es.join(outputlist) 

#Create and write to a new file our madlib, as well as printing it and saving it
savedlib=open(os.path.abspath(".\\Text Files\\Finishedlib.txt"), "w")
savedlib.write(writestr)
madlib.close()
savedlib.close()
print(writestr)
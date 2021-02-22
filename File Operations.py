'''How to read from files, create, write and rename files
Openning a file - you need a file stream so that information can flow.
There are 3 modes in python. Reading (R), Writiing (W) and Appending (A)
'''
file = open('file.txt', 'r')

content = file.read()
print(content)

file.close() #Closes a stream

with open('myfile.txt', 'r') as f: 
    '''
    Everything to be done in the stream happens within the indentation hence no need for the close function.
    Best used when you only need to use it once
    '''
    content = f.read()

print(content)

#Writing files
file = open('file.txt', 'w')

file.write('I am learning Python.') #This overwrites any previous text to the new text

file.flush() 

with open('myfile.txt', 'w') as f: 
   
    f.write('My name is Rhee!')


#Append to files
file = open('file.txt', 'a')

content = file.write('Python is fun to learn.') #Adds this text to the file

file.flush() 


#OS Module
from os import * #This imports all functions in the module

mkdir('Test') #This makes a directory
chdir('Test') #This changes the directory
mkdir('NewDir') #Creates new directory in the old directory

rename('file', 'new') #This renames a file
remove('new') #This removes a file
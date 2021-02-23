'''
Strings can be treated as sequences of characters.
A string is a list so you can use certain list functions on them.
'''

text = 'Hello world!'

print(len(text))

print(text[2]) #This prints the character in the 2nd index. NB: Counting starts from 0 in lists just as in arrays

print(text[6:]) #This slices the text t be printed. It prints all characters from index 6 onwards.

#Iterating over strings
for letter in text:
    print(letter)

#Dealing with escape characters
text = 'Hello world! \nThis day is awesome!' #\n inserts a new line.

print(text)

text = 'Hello world! \tThis day is awesome!' #\t inserts a tab.

print(text)

text = 'Hello world!  \bThis day is awesome!' #\b for backspace.

print(text)

text = 'Hello world!\sThis day is awesome!' #\s inserts a space.

print(text)

#String formatting
name = input()
age = int(input())

#print('My name is '+ name + ' and I am '+ age + ' years old.')#Old and long way of doing it

print('My name is %s  and I am %d years old.' % (name, age))#d is for numbers, s is for strings

print('My name is {} and I am {} years old.'.format(name, age))#More generalized way of doing it

#String Functions
#Case manipulation function
text = 'i am in uppercase!'

text = text.upper()#The upper method converts the text into uppercase

print(text)

text = 'I AM IN LOWERCASE!'

text = text.lower()#The lower method converts the text into lowercase

print(text)

text = 'I AM A TITLE!'

text = text.title()#The title method converts the first letter of every word into uppercase

print(text)

text = 'I am a title!'

text = text.swapcase()#The swapcase method swaps uppercase to lowercase and vice versa

print(text)

#Count function - it counts how many times a substring is contained in a string
text = 'I am a title and I am in green!'

print(text.count('I')) #It counts how many times a certain parameter appears in the main string.

#Find function - It returns the index of the string
text = 'I am a title and I am in green!'

print(text.find('title'))

#Joint function - it is used to join a sequence to one string separated by a specific separator
separator = ';'

mylist = ['Kitchen', 'Dog', 'Rhee']

print(separator.join(mylist))

#Split function - it is used to split a sequence to one string separated by a specific separator
text = 'I am happy because I am almost done with basics of Python!'

words = text.split(' ')

print(words)

#Replace function
text = 'I am happy because I am almost done with basics of Python!'

print(text.replace('happy', 'excited'))
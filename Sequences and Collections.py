#Sequence is a collection of elements. One object that contains multiples values but can be treated as one thing.
#List -Defined using square brackets []
mylist = [10, 20, 30, 'string', True, 8.97]
print(mylist)

#Most sequences are indexed. Index is a number that gives us information about the position of an element in our collection
print(mylist[3]) #This is to specify a certain index
print(mylist[:3]) #This means from the beginning upto index 2, excluding the third index
print(mylist[-2]) #use of the - is to indicate that you're counting the second element from right to left.

mylist[3] = 'Rheena' #This changes the value of the third index to a new value
print(mylist)

#Iterate over lists using for loops
for x in mylist:
    print(x)

#Operations in lists
x = [1, 2, 3]
y = [4, 5, 6]
print(x + y) #This merges the lists
print(x * 4) #This repeats the list 4 times in a row

#Functions in lists - they give some information on lists
x = [1, 2, 3]

print(len(x)) #Tells the length of the list
print(max(x)) #Tells the biggest value of the list but only works when the values are of the same data type
print(min(x)) #Tells the smallest value of the list but only works when the values are of the same data type

#Methods in lists
#Append method - it append (adds) one more value at the end of the list
x = [1, 2, 3]

x.append('Rhee')
print(x)

#Insert method - it inserts (adds) one more value at a given part of the list
x = [1, 2, 3]

x.insert(2, 'Rhee')
print(x)

#Remove method - it removes a value from the list
x = [1, 2, 3, 'Rhee', 'KM']

x.remove('KM')
print(x)

#Pop function - allows you to removes a value from a specific index without knowing what the element is
x = [1, 2, 3, 'Rhee', 'KM']

x.pop(2)
print(x)

#Index method - You pass a value to it and if the value is in the list, the method returns the index of the value
x = [1, 2, 3, 'Rhee', 'KM']

print(x.index('Rhee'))
x.pop(x.index('Rhee')) #Pops (removes) the stated index
print(x)

#Sort method - basically sorts the list
x = [24, 55, 31, 52, 27]

x.sort() #The values of x change to the new sorted values
print(x)
print(sorted(x)) #sorted is a key word to print a sorted list but the values of x remains the same


'''Tuples - They are immutable. 
Their value and/or structure cannot be changed. They are defined with parethesis
'''
y = (1, 2, 3)
y = list(y) #Doing this allows you to change the values (type casting) but it appears as a list
y[2] = 10
y = tuple(y) #This changes it back to a tuple with the new changed value in it
print(y)

'''Dictionary - They are composed of key value pairs and they are not indexed. 
A key value pair consists of a unique key which is the replacement for the index and a value that belongs to that key.
The access of value of a dictionary is referred to by the key:
Dictionaries are defined by curly brackets
'''
person = {'Name': 'Rheena', 'Age': 24, 'Gender': 'Female'}
print(person)
print(person['Age']) #This is to acces a particular key

person['NewAge'] = 25 #This adds a new key to the dictionary
print(person)

#Dictionary methods
#item - This returns a list of all items
print(person.items())

#keys - This returns a list of all they keys
print(person.keys())

#values - This returns a list of all values
print(person.values())


#Membership operators - They check if an element is contained in the sequence
x = [1, 2, 3]

print(2 in x)
print(7 in x)
print(3 not in x)
print(8 not in x)


#Identity operator - check if the value is a type
x = 10

if type(x) is int:
    print('x is int!')
else:
    print('x is not int!')

y = 'Hello'

if type(y) is not int:
    print('y is string!')
else:
    print('y is not string!')


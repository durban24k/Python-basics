#A function is a block of reusable code. It is defined by the def keyword followed by the function
def helloworld() :
    print('Hello world!')

helloworld()

def add(x, y) :
    return x + y #It gets the result and doesn't output it

result = add(19, 12)
print(result)

#Defining default values
def add(a = 0, b = 0) : #The default values of a and b are set to 0
    return a + b

result = add()
print(result)

''' Variable amount of parameters. 
This is for when you have a function and you don't really know how many values you're going to pass. '''
def mysum(*numbers) : #*numbers indicates a variable amount  of parameters
    result = 0
    for number in numbers:
        result += number #Adds the number to the result
    return result

print(mysum(10, 20, 30, 40, 50))
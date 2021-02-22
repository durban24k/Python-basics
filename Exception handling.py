#When an exception happens the rest of the code does not get executed
#Try and accept statements

try: #put in all the code you want executed if an exception happens, you get into the except block
    x = int(input('First number: '))
    y = int(input('Second number: '))
    print(x / y)
except:
    print('There was an error!')

#Predefining the error to be looked out for
try:
    a = int(input('First number: '))
    b = int(input('Second number: '))
    print(a / b)
except ValueError:
    print('Please enter a valid number next time!')
except ZeroDivisionError:
    print('Cannot divide by zero!')
    b = 1
    print(a / b)
finally: #The code will be executed no matter what
    print('DONE!')


#Raising exceptions
def some_function():
    if True:
        raise ValueError ('Something went terribly wrong!')
some_function()


#Indirectly assert something. Asset statements are causing or raising exceptions if the condition they are given is not true
x = 100
y = 20

assert(x < y) #This statement demands that x is less than y otherwise we terminate the script
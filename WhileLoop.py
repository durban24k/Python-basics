#For loop - It iterates over the sequence. It is used for counting or telling how many times to do a certain piece of code
for x in range(1,21):
    print(x)

#x is the control variable that iterates over the range() sequence

#Loop control statement - They allow us to manually control our loops
#The break statement terminates the loop
x = 0

while x < 10:
    if x == 5:
        break
    x += 1
    print(x)

#The continue statement skips the current iteration and proceeds to the rest
x = 0

while x < 10:
    x += 1
    if x == 5:
        continue
    print(x)

#Pass statement
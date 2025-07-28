# for loop needs a start and an end
# while loop doesn't need a start and an end


# Question 1*
x = 1
while x < 10:
    print("hello")
    x = x + 1
print(x)
# 9

# Question 2*
x = 1
while x <= 10:
    print("hello")
    x = x + 1
print(x)
# 10

# Question 3*
x = 1
while x <= 10:
    print("hello")
    x = x * 2
print(x)
# 4

# Question 4 (nested loop) *
x = 1
while x < 10:
    y = 1
    while y < 10:
        print("hello")
        y = y + 1
        x = x + 1
print(x)
# inner loop: 9, by the last loop: y = 10, x = 10 ==> end the outer loop.
# we are always checking y condition first 
# we only checking x condition once the inner loop finishs.

x = 1
while x < 5:
    print("Outer:", x)
    y = 1
    while y < 5:
        print("Inner:", y)
        print("hello")
        y = y + 1
    x = x + 1
print(x)
# 4 * 4 = 16

# Question 5* (this emphasize the difference between for and while)
x = -238
for x in range(0,10):
    print("hello")
print(x)
# 10 (from 0, 1, 2, 3, 4, 5, 6, 7, 9), x = 9

# Question 6*
x = 200
for x in range(0,10,2):
    print("hello")
    x = x + 1
print(x)

# Think carefully about this one! What does x = x + 1 actually do in this for loop?
# Does it have any impact on the for loop? Why? Why not? What about x = x + 10?
# x will go from 0, 2, 4, 6, 8 (5 times), x = x + 1 chỉ để gắn, tuy nhiên khi x quay lại dòng code "for", nó sẽ lại quay về dãy (0,10,2)

x = 200
for x in range(0,10,2):
    print("hello")
    x = x + 1
    print(x)
print(x)

# Question 7*
x = 200
for x in range(1, 5):
    for y in range (0, 5):
        print("hello")
print(x)
# 5 * 4 = 20

# Question 8*
x = 200
for x in range(1, 5):
    for y in range (0, 5, 5):
        print("hello")
print(x)
# 1 (inner loops) * 4 = 4 


# W4 - Question 7.1
for i in range(5, 15 + 1):
    print(i)
# W4 - Question 7.2
for i in range(5, 15 + 1, 2):
    print(i)   
# W4 - Question 7.3
for i in range(5, 15 + 1):
    print(i + 1)

print("\n"*5)
# Question 9a*
x = 1
found = False #boolean
while x < 100 and found != True:
    print("hello")
    print("x:", x, " found:", found)
    if x % 4 == 3:
       found = True
    x = x + 1
print(x)

# this allows the function to run 3 times, until x = 4 (3 + 1), then the loops end when found == True
                                                                                            # not meeting found != True

# Question 9b
x = 1
found = False
while x < 100 and found != True:
    x = x + 1
    print("hello")
    if x % 4 == 3:
        found = True
print(x)

# x = 2 (dư 2, found = False), 3 (dư 3, found = True) 
#                               doesn't meet requirement for the outer loop (found != True)
#                               end the loops.

print("\n"*3)

# Question 9c
x = 0
found = False
while x < 100 and found != True:
    print("hello")
    if x % 4 == 3:
        found = True
    x = x + 4
print(x)
# x = 0 (dư 0), x = 4 (dư 0), x = 8 (dư 0), the loop end when x => 100. 

# Question 10
# Write a while loop that will print the numbers from 1 to 10 (inclusive)
for i in range(1, 10+1):
    print(i)

# Write a while loop that will print the even numbers from 1 to 10 (inclusive)
for i in range(1,10+1):
    if i % 2 == 0:
        print(i)
    i = i + 1

# Now do it with a for loop! 
i = 1
while i <= 10:
    if i % 2 == 0:
        print(i)
    i = i + 1

# Question 11: Using a nested while loop (while loop inside a while loop), write some code that will print the following sequences
    #11.1
for x in range (0,4):
    for y in range (0,4):
        print(x)
    
print("\n"*2)

    #11.2
for x in range (0,3):
    for y in range (0,4):
        print(x + 1)
        x = x + 1

# x = 1
# while x < 4:
#    y = x
#    while y < x + 4:
#        print(y)
#        y += 1

for x in range(1,4):
    for y in range(x, x + 4):
        print (y)

print("\n"*2)

    #11.3
for x in range (0,4):
    for y in range (0,4-x):
        print(x)

print("\n"*2)

# Question 12: Print out the Fibonacci sequence
# The Fibonacci sequence is a sequence that goes 1, 1, 2, 3, 5, 8, 13, ....
    # 12.1
limit = 1000
if (limit > 1):
    print(1, end =", ")
    print(1, end =", ")
    previousprevious = 1
    previous = 1
    currentNumber = 1 + 1

    while currentNumber <= limit:
        print(currentNumber, end =", ")
        previousprevious = previous
        previous = currentNumber
        currentNumber = previous + previousprevious
print(" end")

    #12.2
    # Edit the above code to print out the first "n" Fibonacci numbers, instead of all Fibonnaci numbers up to limit

limit = 4
if (limit > 1):
    print(1, end =", ") 
    print(1, end =", ")
    previousprevious = 1
    previous = 1
    currentNumber = 1 + 1

    y = 3

    while y < limit: #limit = 10, once y = :
        print(currentNumber, end =", ")
        previousprevious = previous
        previous = currentNumber
        currentNumber = previous + previousprevious
        y = y + 1
        print(y)
print(" end")

    #12.3: Lucas sequence 
limit = 10
if (limit > 1):
    print(2, end =", ") 
    y = 1
    print(1, end =", ")
    previousprevious = 2
    previous = 1
    currentNumber = 2 + 1

    y += 1

    while y < limit:
        print(currentNumber, end =", ")
        previousprevious = previous
        previous = currentNumber
        currentNumber = previous + previousprevious
        y = y + 1
print(" end")
# Week 4

a = 5 # 5 is included
while a < 50:
    print(a)
    a = a + 1

for number in range(1,10):
    print(number)

# assume the existence of an end variable, 
    # print out the sum of all variables from 1 to n

end = 80 # 80 is included

sum = 0
for number in range(0,end):
    sum += number
print (sum)

# """"""
# Using loops, print out the following patterns
# 1 2 3 4 5

end = 5
for number in range(1,end+1):
    print(number)

# Assume the existence of an end variable, print out the numbers
    # from 1 to end (inclusive), on a single line, separated by commas

# ver 1: using loops
end = 10
answer = ""
for number in range(1, end + 1):
    if number == end:
        answer += str(number)
    else:
        answer += str(number) +  ", "
print(answer)

# ver 2: using slicing
end = 10
answer = ""
for number in range(1, end + 1):
    answer += str(number) +  ", "
answer = answer[:-2]  # note: it's [-2] not [-1] with the [-x], there is no [0]
print(answer)

# Assume the existence of an end variable, print out the following pattern:
    # 1
    # 1, 2
    # 1, 2, 3
# This problem is similar to the previous problems with end = 1 up to end = the given number
# Two patterns
# - Each starts from 1 and increase as it goes down to one another
# 1
# ... 2
# ... ... 3
# ... ... ... 4
# - Inside each row, we print out the numbers from 1 to the current number
# 1 ... number

end = 10
for limit in range(1, end + 1): # This will give us a seperate row
    # limit = 1, limit tells us how far each row should go
    answer = ""
    for inner_number in range(1, limit + 1): # This gives us the number within
        answer += str(inner_number) +  ", "
    answer = answer[:-2] # remove the last comma and space
    print(answer)

# Notes: when u have a nested loop
    # On each iteration of the outter loop (the outter most loop), 
    # EVERYTHING inside the block must finish executing first,
    # before it repeats.

    # The inner block of code is the same as what we saw before,
    # BUT THIS TIME, the inner loop stops at different points as 
    # specified by the outter loop


# Check if the number if a PRIME number
    
# The original
number = 87
is_prime = True
for check in range (2, number):
    if number % check == 0:
        is_prime = False
print("is prime?", str(is_prime))

# Break down of the original: look at all number from start to end
    # check the current number to see if it is prime
        # to see if the number is prime, check all
        # numbers from 2 to the current number

start = 2
end = 10
# The doing-again
for current_number in range (start, end + 1):
    # look at all numbers from start to end
    # call each one "current_number"

    # check each "current_number" to see if it's prime
    is_prime = True
    for check in range (2, current_number):
        # we check it by comparing it against all numbers
        # from 2 up to the current_number (exclusive)
        if current_number % check == 0:
            is_prime = False
    # We know if the current_number is prime or not
    # We can decide if we want to print it out 
    if is_prime == True:
        print(current_number)
    # End of the loop, move on to the next number to see if it's prime.

# Problem to look at later
# For each even number, print out that number an additional n number of times
# where n is that number
# 1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, ...
        

# Code Runner
# Question 3
for number in range (start, end + 1):
    is_prime = True
    for check in range (2, number):
        if number % check == 0:
            is_prime = False
    if is_prime == True: 
        print(number)

# Question 4
answer = ""
for outer in range (1, 5 + 1):
    for inner in range (1, outer + 1):
        answer += str(inner) + " "
print(answer)

# Question 5
for current_number in range (start, end + 1):
    output = str(current_number) + ": "
   
    for check in range (1, current_number + 1):
        
        if current_number % check == 0:
            output += str(check) + " "
    print(output)

number = 12321
count = len(str(number))
print (count)


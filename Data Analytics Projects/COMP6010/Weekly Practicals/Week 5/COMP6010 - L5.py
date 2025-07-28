

print("\n"*10)

def foo():
#      ^list of arguments (inputs)
    print("The function has been called")
    print("This is another message")
    print("Because i want more than one line")

# We have a function definition - but it doesn't unless it is used
    
# Function call:
# print("Hello")
foo()


def check_is_even(number): # number = 10
#                   ^parameter
    # At this point in the code, number is 10.
    if number % 2 == 0:
        print(str(number) + " is an even number")
    else:
        print(str(number) + " is not an even number")
    # Once we finish, where does the control of the code go to?

check_is_even(10)
check_is_even(5)
check_is_even(13)
check_is_even(21)



# Scoping
a = 10
if a > 3:
    a -= 1
    # run once

a = 10
while a > 3:
    a -= 1
    # run more than once

a = 10
b = 0 # keep track the # of the run(s)
while a > 3:
    a -= 1
    b += 1
print(b)

# Changes to variables in the lopp, change the values outside the loop as well
print("\n"*10)
best_variable = 5

def do_sth(x): # x = best_variable
               # x = 5
    x += 1     # x = 6
    print(x)

do_sth(best_variable)
#best_variable does NOT change, because the function modifies the x variable
print(best_variable) # Is this 5 or 6? ==> still 5

y = 130
def do_something_else(_y): # y = y (it copies y, y inside is different from y outside)
    # Scoping
    # Python uses function scoping
    # This means new variables in a function, are different copies
    _y += 1
    print(_y)
    # Whenever u use a variable, u always use the version "closest" in scope

do_something_else(y)
print(y)

# ""
# Scoping
# Python has different "scopes"
# Scopes: Where a variable can be used
# Python uses function scoping
# ""

number = 10

# def zap(x):
    # for those interested, u can look into global keyword
    #number += 11 # number here will not run

# zap(50)

# returns
# type hints
# checks

print("\n" * 5)

def good_function(k):
    print("Hello")

good_function(10)

abs(-80) # abs doesnt secretly print anything
print(abs(-80)) # We need to print to see our result 

def our_abs(k):
    if k < 0:
        print(-k)
    else:
        print(k)

our_abs(-80)

print(our_abs(-80))

def abs_version_2(k): # k = -80
    if k < 0:
        return -k # 80
    else:
        return k # (never reach)
    # Returning is how a function gives back a value
print("abs version 2")
abs_version_2(-80) #abs_version_2 does not print anything on its own

print(abs_version_2(-80))
# When a function returns a value, the returned value "replaces" the function call
# Once it has been computed

# Return is powerful since this result returned can be used later in the program

number = -42
positive_version = abs_version_2(number) # 42, the number returned
# positive_version = 42
print(positive_version)

test = 4
another_number = abs_version_2(-4) + abs_version_2(-3) * abs_version_2(test)
# order of operation: 
# another_number = abs_version_2(-4) + 3 * abs_version_2(test)
# another_number = abs_version_2(-4) + 3 * 4
# another_number = abs_version_2(-4) + 12
# another_number = 4 + 12
# another_number = 16
print(another_number)


print(print(5)) #none, not all function returns something

# Returns replace the function call
# Return immediately stops the function and gives back the answer

# ""
# Define a function named xyz that takes a int parameter and prints "high" if
# the number is greater than 50
# ""

def xyz(dfkhbefibe):
    if dfkhbefibe > 50:
        print("high")

# ""
# Define a function named is_prime that takes a int parameter, returns True
# if the number is prime and False otherwise
# ""
        
def is_prime(number): # number = 9
    for check in range(2, number):
        if number % check == 0: # if we find a number that can divide the input
            return False
    return True # placement is very important
        
print(is_prime(9))
print(is_prime(13))

# Sometimes we want u to print stuff, sometimes not, please read the questions carefully

# Now, what if our input is a string ("Hello"), there will be an error

def is_prime(number: int): # number = Hello
    for check in range(2, number):
        if number % check == 0: # if we find a number that can divide the input
            return False
    return True 
# Type hints help to show what data a parameter expects
# But it does not ENFORCE the type

def is_prime(number: int): # number = Hello
    if type(number) != int:
        print("Input is not of correct type")
        return # uses to stop it
        # Not putting a value for the return, will make it return None

    for check in range(2, number):
        if number % check == 0: # if we find a number that can divide the input
            return False
    return True 

print(is_prime("Hello?"))

# Assume the existence of a variable start and end,
# print out all the numbers from start to end (that are prime)


# Define a function named number_in_range_that_are_prime that
# when passed the parameters start and end, prints out the numbers
# in the range that are prime numbers. The two numbers are inclusive.

# nested loop question:

def number_in_range(start, end):
    # Get all the numbers between start and end
    for current_number in range(start, end + 1):
        # Check if the current number is prime or not
        # By comparing against numbers from 1 up to current_number (exclusive)
        is_prime = True
        for compare in range(2, current_number):
            if current_number % compare == 0:
                current_number_is_prime = False
        # If we check all numbers from 1 to current_number and is_prime
        # still remains True, it means we didn't find anything that could divide it
        if current_number_is_prime == True: # So we should print it out!
            print(current_number)

def is_prime(n : int):
    for compare in range(2, n):
        if n % compare == 0:
            return False
    return True

def number_in_range(start, end):
    for current_number in range(start, end + 1):
        is_current_number_prime = is_prime(current_number)
        if is_current_number_prime == True:
            print(current_number)

# By breaking down a function into smaller parts, we can 
            # simplify the design of our code.

    
# Question 1:
def foo(n : int, k : int) -> int:
    return n ** 2 + k # foo(5, 1) => 5^2 + 1 = 26

def bar(my_string : str) -> int:
    return len(my_string) # bar('student'): 7

def zoop(n : int):
    return foo(n, n) # zoop(2) => foo(2, 2): 2^2 + 2 = 6

def abc(n : int) -> int:
    return abc(n) #error



 
foo(5, 1) #26
print(foo(5,1))

bar('student') #7
print(bar('student'))

zoop(2) #6
print(zoop(2))

foo(bar('student'), 1) #15
# bar('student') = 7
# foo(7,1) = 7^2 + 1 = 50
print(foo(bar('student'), 1))

foo(zoop(2), bar('student')) #43
# zoop(2) = 6
# bar('student') = 7
# foo(6, 7) = 6^2 + 7 = 36 + 7 = 43
print(foo(zoop(2), bar('student')))

# abc(5) # an error

# Question 2: write a program to convert a decimal number to a binary
n = 13
result = ""
while n > 0:
    if n%2 == 0:
        result = '0' + result
    else:
        result = '1' + result
    n = n//2
print(result)

# Question 3: Given a positive integer in base 10, print the number of 1's in the binary representation of the number.
n = 13
result = ""
count = 0
while n > 0:
    if n%2 == 0:
        result = '0' + result
    else:
        result = '1' + result
        count += 1
    n = n//2
print(result)
print(count)

# Question 4: Given a positive number, output a number that has each digit increased by 1. 
# If the digit is 9, then that digit should be converted to 0

# Question 5: 
# Print out all the prime numbers between 1 and 1000 
# who's digits add up to between 10 (inclusive) and 15 (inclusive).

n = 1000
test = 2
isPrime = True

if type(n) != int or n < 2:
    isPrime = False
else:
    while test < n:
        if n % test == 0:
            isPrime = False
        test += 1

if (isPrime = True):
    print(n)

n = 17
result = 0
while n < 0:
    result = (n % 10) + result
    n = n//10
if result >= 10



""
# LOOPS
#- while
#- for
#- examples

#Starting at 11:03
""

if True:
  # The 1st line inside of a block, determine the indentation level
  print("hi")

import datetime

# Loops
my_number = 0
count = 0
while my_number < 60:
  #^boolean expression
  # The loop will keep iteracting/ going again, while the boolean expression
  print("Still waiting")
  print("Still waiting", "my_number is: " + str(my_number), datetime.datetime.now())
  my_number += 1

  #Unlike a conditional - we go back to the start of the loop
  #Infinite loop - when the loop will never stop


print("count" + str(count))
#Once the boolean expression is False, we continue with the rest of the code 
print(my_number)

name = "Micheal"
#Collection of characters
count = 1
print(name)
for letter in name:
    # The in keyword, lets us go through a collection, one item at a time
    # Each individual value of the collection, will be put into the variable
    # on each loop oteration
    print(str(count)+""+letter)
    count +=1

# print(list(range(0,100)))
# All the numbers from 0 to 100, not including 100
# ((We will talk about lists later))


# range gives us all the number from 0 to 100, not including 100
# [0, 1, 2, 3, 4]
    
# String slicing
# "micheal"[0:4]
    
for number in range(0,100):
   print (number)

# Question 1.1: Add all the numbers form 0 to 5 in a variable named sum
sum = 0 + 1 + 2 + 3 + 4 + 5

# Question 1.2: Add all the numbers form 0 to 9999 in a variable named sum
# Start: 0
# End: 9999 (inclusive)
# Increment: 1
sum = 0
for number in range (0,9999 + 1):
   sum += number
   print(number)
print(sum)

sum = 0
for number in range (0, 5):
   # [0, 1, 2, 3, 4]
   sum += number
   # print(number)
print(sum)


# Question 2: Add all the numbers from 5 to 300 that are even (!!!)
# = 6 + 8 + 10 + ...
# outline:
  # somewhere to store my answer: result
  # somewhere to store the current number: i
  # START: 5
  # END: 300
  # Change: 1 at a time?



result = 0 
i = 5
while i <= 300:
  if i % 2 == 0: 
    result += 1 #add all numbers from 5 to 300
  i = i + 1
print("RESULT IS:" + str(result))

# version 1
result = 0 
i = 5
while i <= 10:
    if i % 2 == 0:
      result += i #add all numbers from 5 to 300
    i = i + 1
print("RESULT IS:" + str(result))

# version 2
start = 5
end = 300

result = 0
i = start
if i % 2 == 1:
   i += 1
while i <= end:
   result += i
   i  = i + 2
print("RESULT IS:" + str(result))

# Assume the existence of the variables start and end , and all the
   # numbers form tart to end that end in the digit 3
   # Example
   # start = 5
   # end = 52
   # 5 - 53
   # 13 + 23 + 33 + 43

start = 5
end = 52

# ver 1
i = start
while i <= end:
  if i % 10 == 3:
      sum += i 
  i = i + 1 # increment
   
# ver 2
for number in range (start, end + 1):
   # range (included, excluded)
   if number % 10 == 3:
      sum += number


# STRINGS
  # "micheal lay" [3 : 8 : 2]
      
for number in range (5, 100, 2):
   print(number)


# Question 3: Getting the first digit of a number
   # number = 58183
   # number // 10 = 5818 integer division by 10, removes the last diogit
   # number // 10 // 1 = 501 if i repeat the division by 10 two times, we remove 2 digits
   # log base 10 of a number, is how many times you need to divide a number by 10
   # log10(100) -> 2
   # number // 10 // 10 // 10
   #            1000
   # number // 10 ^3
   # number // 10 ^ log10(number)

   #Getting the 1st digit of a number
   # integer division by 10, remobves the last digit
   # number = 1828131
   # if number is more than or euqal to 10, we should keep removing digits

number = 83812871
while number >= 10:
   number = number // 10
print(number)

# Question 4: How many digits are in a given number
# assume the existence of a variable number, print out how many digits are in number
number = 18731
# print(len(str(number))) # bad 
count = 0
number_modified = number
while number_modified > 0:
   number_modified = number_modified // 10
   count += 1
# After the loop, number has been modified. However, how can we change that?
print("In the number" + str(number) + "there are" + str(count) + " digits")


# PRIME NUMBERS
# It is a number that can only be divided by 1 and itself
# 127 - try 2, 3, 4, ... 126
# If we tried all numbers from 2 to 127 (exclusive), and none divided it, then it is a  prime
# If we found a single number that could divide it, then it is not a prime number
# 345678

number = 345678
is_prime = True
for i in range(2, number):
   print(i)
   if number % i == 0:
      is_prime = False
      print(str(i) + "could divide" + str(number))
print("is" + str(number) + " prime? " + str(is_prime))

# shorten version (using #break)
number = 345678
is_prime = True
for i in range(2, number):
   print(i)
   if number % i == 0:
      is_prime = False
      print(str(i) + "could divide" + str(number))
      break # break stops the loop immediately
print("is" + str(number) + " prime? " + str(is_prime))

# Check if a number is prime, but ignore if it is divisible by 5
number = 345678
is_prime = True
for i in range(2, number):
   if i == 5:
      continue # countinue menas, immediately go to the END of this loop iteration
   if number % i == 0:
      is_prime = False
      print(str(i) + "could divide" + str(number))
      break # break stops the loop immediately
print("is" + str(number) + " prime? " + str(is_prime))

# Write some code which will print the following pattern
# 3, 6, 9, ... , 60 (3x) (x = 1, 2, 3, ... 20)
# 1, 4, 9, 16, 25, 36 increment: x^2 (x = 1, 2, 3, 4, 5, 6)

for i in range (3, 60 + 1, 3): 
  print(i)

for i in range (1, 6 + 1):
  print(i + 1)


# QUIZ 1: variable, strings, conditional
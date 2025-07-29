# Question 1:
# A function that returns True if the passed number (whole number) is prime, False otherwise
    # check if 13 (prime), 12 (not prime), 0, 1, or - 5 (negative) or 15.5 (float)

# A function that when passed two numbers (a, b), returns the average of the two.
    # check if a and b are (0,0) or (-1,-2) negative, or (13,15) postive or (-1, 7) or (99, 0)


# A function that when passed two numbers (a, b), returns the first number to the power of the second number. 
# For example, 1.2 to the power of 2 is 1.44, 1.2 to the power of 2.5 is 1.5774409
    # check if b is postive, negative, factor, and check if a is 0


# A function that when passed a number (n), returns the number rounded to the nearest integer.
    #  check if n is negative, 0, and postive. 


# Question 2
"""
Consider a function that when passed three numbers (n, min, max), say, val, low, and high, returns True if 
val lies in the range [low, high] (inclusive on both sides), and False otherwise. Google "range 
math" if you don't know what it means. Are the following test cases sufficient to assess the 
correctness of this function? If not, what other tests would you include?
"""

# check when:
# n is in the range (25, 20, 30)
# n is out of the range (5, 20, 30)
# n is out of the range (35, 20, 30)
# range contains one item (21, 20, 20)
# if max < min (21, 30, 20) ==> should return "invalid"
# if one of (n, min, max) is negative (-3, -5, 0)

# Question 3
# What is wrong with the following assertions? 
# You are required to interpret the purpose of the functions based on their names.
print('\n')
def add(a : int, b : int) -> int:
    c = a + b
    return c

result = add(10,12)
print(result)

#######################################
print('\n')
def is_odd(number : int):
    result = True
    if number % 2 == 0:
        result = False
        print("Is", str(number), "an odd number? ", str(result))
    print ("Is", str(number), "an odd number? ", str(result))

is_odd(3)


print('\n')
def isEven(number : int):
    if number % 2 == 0:
        return "even"
    else:
        return "odd"
    
    
result_ver2 = isEven(3)
print("Is the number odd or even?", str.capitalize(result_ver2))

#######################################
# Question 1:
print('\n')
def numeric_grade_to_letter(grade):
    if grade < 50:
        return "F"
    elif grade < 65:
        return "P"
    elif grade < 75:
        return "Cr"
    elif grade < 85:
        return "D"
    elif grade < 100:
        return "HD"
    print("Invalid grade passed")

print(numeric_grade_to_letter(58))

# Using the above code, answer the following:
#   Which part of the code is the function header?
    # The function header is "def numeric_grade_to_letter (parameters)".

#   What symbol is used to mark the end of the function header?
    # A colon (:) to mark the end of the function header.

#   What are the parameters, and what types of values can they take?
    # parameter is "grade", it takes float or int or a list

#   What does the keyword def do?
    # it's used to define a function

#   What is the name of the function?
    # The function name is "numeric_grade_to_letter".

#   What lines are part of the function definition and what lines are part of the function call?
    # numeric_grade_to_letter(grade)

#   How many return statements are there? Will the function always return?
    # 5 return statements, and the function is not always return.

#   Is there an input to the function that would result in "Invalid grade passed" being printed when it shouldn't?
    # 

#   If you were to remove line 14 and then run the code, would the condition on line 2 be checked? Why or why not?\
    # nothing happens

###########################################
print('\n')
# Question 5.1
def is_greater_than(a,b):
    if a > b:
        return "True"
    else:
        return "False"
    
print(is_greater_than(2,3))

print('\n')
# Question 5.2
def get_average(a,b,c):
    average = (a + b + c)/ 3
    return average

print(get_average(2,3,4))

print('\n')
# Question 5.3
print(is_greater_than(5, 5))
print(is_greater_than(5, 6))
print(is_greater_than(0, -1))
print(get_average(5, 5, 5))
print(get_average(5, 6, 7))
print(get_average(5.1, 5.2, 5.3))

# Question 6: equivalence partitions

# Question 7
def numberOfDaysInGregorianMonth( month, year ):
    if type(month) != int or type(year) != int or year == 0 or month < 1 or month > 12:
        return 0
    if month in [1, 3, 5, 7, 10, 12]:
        return 31
    if month in [4, 6, 9, 11]:
        return 30
    if month == 2:
        if year % 4 == 0:
            return 29
        if year % 100 == 0:
            return 28
        if year % 400 == 0:
            return 29
    
numberOfDaysInGregorianMonth( 2, 2000 ) # testing for:  February in a leap year that is divisible by 400
numberOfDaysInGregorianMonth( 2, 1999 ) # testing for:  February in a a non-leap year that is not divisible by 4.

# Question 8:
def foo(num1, num2):
    return num1 + num2

def bar(a, b, c):
    return foo(a,b) * square_num(c)

def square_num(a):
    return foo(a, a ** 2)

# Scenario 1
print(bar(1, 3, 3))

# Scenario 2
for i in range(1,10): # i = 1, 2, 3, 4, 5, 6, 7, 8, 9 (9 results)
    print(bar(i, 3, 2))








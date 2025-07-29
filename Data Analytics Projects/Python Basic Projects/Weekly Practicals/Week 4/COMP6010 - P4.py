# week 4 practical

# Q1
x = 10

if x < 5:
    print("this statement is less than 5")
else:
    print("this statement is NOT less than 5")

# Q2
x = 10

if x < 5: 
    print("this statement is less than 5")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is greater than 5") 

# Q3
if type(x) == int:
    if x < 5: 
       print("this statement is less than 5")
    elif x == 5:
       print("x is equal to 5")
    else:
       print("x is greater than 5")
else:
    print("x is not a number")    

# Q4 (using 1 if, 1 else and as many "elif" as needed)
assignmentMark = 6.5
assignmentMarkedOutOf = 9

grade = assignmentMark / assignmentMarkedOutOf * 100

if grade < 0 or grade > 100:
    print("error")
elif grade < 50:
    print("F")
elif grade < 65:
    print("Pass")
elif grade < 75:
    print("Credit")
elif grade < 85:
    print("Distinction")
else:
    print("High Distinction")

# Q5 (similar to Q4, but only use "if")
assignmentMark = 8
assignmentMarkedOutOf = 8

grade = assignmentMark / assignmentMarkedOutOf * 100

if 0 <= grade <= 100:
    if grade < 50:
        print ("F")
    if grade >= 50 and grade < 65:
        print ("Pass")
    if grade >= 65 and grade < 75:
        print("Credit")
    if grade >= 75 and grade < 85:
        print("Distinction")
    if grade >= 85:
        print("High Distinction")

if grade < 0  or grade > 100:
    print("error")

# Q6
# Example A
for x in range(1,10):
    print(x)

# Example B
x = 1
while x < 10:
    print(x)
    x += 1

# Example C
for x in range(1,11):
    print("printed a line")

# Example D
for x in range(1,1):
    print("printed a line")

# for [x] in range (0,10,(1)):
    # print("hello") ## (start - inclusive, stop - exclusive, step)    

# Example E
# x = -2 
# for x < 3: # an error "for" cannot use in this situation, an "if" function needs to be used
    # print("printed a line")

# Example F
# x = 1
# while x < 10: # this will cause the system running forever
    # print(x)

# Example G
for x in ["Alex","Bob","Chris","Danni"]:
    print("printed a line x")

# Example H
x = int(input())
while x < 10:
    print(x)
    x += #x = x + 1


for i in range(5,15+1)
    print(i)
# Week 3 Variables + Strings
print(4 + 3 * 2 + (2 - 1))

# Question 1
a = 4 + 3 * 2 + (2 - 1)
print (a) # doing the same as previous code

b = 3 ** 2 * 2 ** 2
print (b)

print (a+b)
print (a*b)

# different types of variables in Python
# string - str
# integer - int
# float - float
# bool - bool
# double - double
# long integers - long
print(type(a)) # example
print(type(b))

# Question 2
a = 10 # valid

# 1a = 10 # invalid since it starts with a number

# 10 = a  # invalid since it starts with a number

a, b = 10, 18 # valid
print (a,b)

a, b = a + 5, b + 8 # valid
print (a,b)

a, b = True, "Hello" # valid. noted that if we use "true", it will not work.
print (a,b) # a (boolean value), b (string)

# Question 3
a = 18 #int
print(type(a), "\n")

b = 4.7 #float
print(type(b), "\n")

c = 4/3 #float
print(type(c), "\n")

d = 4//3 #int
print(type(d), "\n")

e = True #bool
print(type(e), "\n")

g = "COMP6010" + " " + "is the best" 
print(type(g), "\n")

f = 4 == 9 
print(f)
print(4==9)
print(type(f), "\n")

h = b + a 
print(type(h), "\n")

i = 'My tutor is _____' 
print(type(i), "\n")

j = 4**2
print(type(j), "\n")


# Question 4: formating
# a) Given the following string myString, without changing the value of myString 
# (no equal sign), print the string in upper case.

# concatenation (, +)
a = 10
b = 67
c = a + b
print ("If you add " + str(a) + " and " + str(b) + " you get " + str(c))
print ("If you add {} and {} you get {}".format(a,b,c)) #format function makes it easier to format a, b, c into blanks
print (f"If you add {a} and {b} you get {c}") 

print("This is Kevin's book.")
print("He goes \"crazy\" if someone touches it.") # you can add \"abc\", so \ makes Python understand "" is strings
print("my url: go yo C:\\") # to print \, u add an additional \ 

# formatted string
myString = "abcdef"
print(myString.capitalize()) #result = Abcdef
print(myString.upper()) #result = ABCDEF


# Question 5: strip
theString = "   Welcome  to  COMP6010       "
anotherString = theString.strip() # # remove spaces on the right and left of the sentence
print(anotherString)
print(theString)

print(theString.rstrip()) # remove spaces on the right of the sentence
print(theString.lstrip()) # remove spaces on the left of the sentence

# Question 6: Slicing
myString = "abcdefghijklmnop"
print( "line 1-" + myString[ : : ] ) #myString[inclusive:exclusive:jumping_step]
print( "line 2-" + myString[5 : 2] ) 
print( "line 3-" + myString[5 : -2] ) # -2 = how many characters we will skip counting from the right
print( "line 4-" + myString[5 : 6] )
print( "line 5-" + myString[5 : 12] )
print( "line 6-" + myString[1 : : 2] ) # starting from the second index, skipping one each of every two characters.
print( "line 7-" + myString[1 : : 3] ) # starting from the second index, skipping two each of every three characters.
print( "line 8-" + myString[ : : 2] ) # starting from the first index, skipping one each of every two characters.
print( "line 9-" + myString[ : : 3] ) # starting from the first index, skipping two each of every three characters.

# Question 7: 
myString = "abcdefghijklmnop"
print( "line 10-" + myString[ : : -1] ) # starting from the last index and printing all to the first one.
print( "line 11-" + myString[ : : -2] ) # starting from the last index, skipping one each of every two characters.
print( "line 12-" + myString[2:7:2]) # no characters
print( "line 13-" + myString[3: :-1]) # starting from the forth index [position number 4], and printing backwards.



# Week 3 Conditions
# Question 1: Write an if statement that prints "This is amazing!!!." with the condition 5 > 3.
if 5 > 3:
    print("This is amazing!!!.")
else:
    print("This is not amazing!!!.")

# Question 2: Use conditions to print out statements about x:
    # If x is odd, then print out "x is odd".
    # If x is divisible by 3, then print out "x is divisible by 3".
    # If both, then print out "x is odd" on one line and then print out  "x is divisible by 3" on another line.

x = 9
print(x)
if x % 2 == 1:
    print(str(x),"is odd")

if x % 3 == 0:
    print(str(x), "is divisible by 3")

if x % 2 == 1 and x % 3 == 0:
    print(str(x), "is odd")
    print(str(x), "is divisible by 3")


# Question 3: Write a piece of code using conditions to print "x is positive", 
    # "x is negative", or "x is zero" depending on what the value of x is.'
print("pleas enter a number")
x = input()
x = int(x)

if x > 0:
    print(str(x), "is positive")
elif x < 0:
    print(str(x), "is negative")
else:
    print(str(x), "is zero")



# Question 4:

x = 2
if x > 3:
    x = x * 2
    if x == 3:
        x = x + 5
        if x % 2 == 0:
            x = 4
        else:
            x = x * 4
elif x < 0:
    if x % 2 == 0:
        x = x + 1
    elif x == 15:
        x = x - 1
    x = x + 6
else:
    x + 1 # this line doesn't work; to correct it, we have: x = x + 1
    if x == 3:
        x = x + 2
    else:
        x = x + 10
    x = x + 50




print(x)

x = -5
if x > 3:
    x = x * 2
    if x == 3:
        x = x + 5
        if x % 2 == 0:
            x = 4
        else:
            x = x * 4
elif x < 0:
    if x % 2 == 0:
        x = x + 1
    elif x == 15:
        x = x - 1
    x = x + 6
else:
    x + 1
    if x == 3:
        x = x + 2
    else:
        x = x + 10
    x = x + 50
print(x)

x = 10
if x > 3:
    x = x * 2
    if x == 3:
        x = x + 5
        if x % 2 == 0:
            x = 4
        else:
            x = x * 4
elif x < 0:
    if x % 2 == 0:
        x = x + 1
    elif x == 15:
        x = x - 1
    x = x + 6
else:
    x + 1
    if x == 3:
        x = x + 2
    else:
        x = x + 10
    x = x + 50
print(x)
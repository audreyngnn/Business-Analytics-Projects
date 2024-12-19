###### Week 2
#Question 1
print(15 + 4)
print(15 - 4)
print(15 * 4)
print(15 ** 4)
print(15 / 4)
print(15 // 4)
print(15 % 4)

#Question 2 (order of operations)
print(5 + 7 + 12 + 3 * 2 + 7)
print(5 + 7 + (12 + 3) * 2 + 7)
print((5 + 7 + (12 + 3)) * (2 + 7))

#Question 3 (change of base)
print(37)
print(bin(37)) 
    #base 2 (0,2)
print(oct(37)) 
    #base 8 (0,1,2,...,7,8)
print(hex(37)) 
    #base 16 (0,1,2,...,8,9,A,B,C,D,E,F,G)

#covert into binary
#(19)_10 
# 32 16 8 4 2 1
#covert into oct will require us to convert into binary first, then divide bits into 
    #group of 3 (4,2,1)
    #finally, only count the numbers with an "1" below
#convert into hex will also require us to convert into binary first, then divide bits into 
    #group of 4 (8,4,2,1)
    #finally, only count the numbers with an "1" below

#a, covert 127 into bin, oct, and hex
print(2**7,2**6,2**5,2**4,2**3,2**2,2**1,2**0)
#starting from 2**6
print(127-2**6)
print(63-2**5)
#bin(127)=11

print(bin(177))
print(oct(177))
print(hex(177))

#convert binary to decimals
#(10001)₂ = (1 × 2⁴) + (0 × 2³) + (0 × 2²) + (0 × 2¹) + (1 × 2⁰) = (17)₁₀



## Find the 'nth' digit of a number
print(5263**4)

#Question 5: Write a piece of python code that will take a decimal number
#print out only the right-most digit.
print(5263%10)

#Question 6: Write a piece of python code that will take a decimal number 
#print out only second right-most digit
print((5263%100)//10)

#Question 6.1: Write a piece of python code that will take a decimal number
#print out its second left-most digit.
print(5263%1000//100)

#Question 7: Write a piece of python code that will take a decimal number
#print out its left-most digit.
print(5263//1000)

import math
print(math.log10(100))


###### Week 2 Strings
#Question 1: what is the difference?
#print( 5 + 3 )
#print( "5 + 3" )

#Question 2: Write some python code that will print out your full name 
#as a string but with each name on a new line.
print("Nguyen Khuat Son Tra")
print("Nguyen\nKhuat\nSon\nTra")

#Question 4: Write some python code that prints out 3 strings on the same line using 1 print statement.
print("Welcome"+"to"+"Fundamentals of Computer Science!")

#Question 5: How would you add spaces in between the strings listed above? Can you come up with two 
#different ways of doing this?
print("Welcome "+"to "+"Fundamentals of Computer Science!")
print("Welcome","to","Fundamentals of Computer Science!")
print("Welcome to Fundamentals of Computer Science!")

#Question 6: Why does the following code not work?
#print("welcome to COMP" + 6010)
#They can't add two different types of data, "welcome to COMP" is string while 6010 is integer 
#All the code fuctions

### boolean, which is only True or False
has_passed = True
has_passed = False


### Operators
# + - * / 
# % - finds you the remainder
# //

print(3 + 4) # 7
print(3 - 4) # -1
print(3 * 2) # 6
print(4 / 3)
print(12 % 7)   # Module gives us the remainder

number = 27
print(number % 2 == 0) # Check if even
print(number % 2 == 1)  # Check if odd

print(4//3)  # Integer division - removes the decimal (no rounding)


### Comparison operators
# == equality
# != inequality
# > left is more then right
# < left is less then right
# >= left is more than or equal to right
# <= left is less than equal to right

### # Logical operators
# and/ or/ not

# and checks that the left AND the right is True
# We want to purchase milk and it is a restricted product
print("Can purchase? " + str( can_purchase_thing and (bank_balance >= 6)  )  )
                               # ^ boolean           |                 | -> boolean


# or checks that at least one side is True
bank_balance = 5
mums_bank_balance = 100

print("Can purchase?:" + str(bank_balance >= 5 or mums_bank_balance >= 5) )

# not
is_raining = True
print( not is_raining)

empty_variable = None
print(type(None))


### binary, octal, hexadecimal
# 1101
# (1 * 2^3) + (1 * 2^2) + (0 * 2^1) + (1 * 2 ^ 0)
# 8 + 4 + 0 + 1
# 13

# Decimal
# 5195 
# (5 * 1000) + (1 * 100) + (9 * 10) + (5 * 1)
# (5 * 10^3) + (1 * 10^2) + (9 * 10^1) + (5 * 10^0)

"""
#15 -> binary

15 // 2 = 7   15 % 2 = 1
7 // 2 = 3    7 % 2 = 1
3 // 2 = 1    3 % 2 = 1
1 // 2 = 0    1 % 2 = 1

1111
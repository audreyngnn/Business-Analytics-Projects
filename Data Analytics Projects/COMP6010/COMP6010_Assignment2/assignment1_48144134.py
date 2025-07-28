"""
# Student Declaration
# I [Nguyen Khuat Son Tra and 48144134] declare that this is my own work and that
# I have not used any code or logic from other people or from sources outside of the unit. 
# I understand that it is ok to look at COMP6010 videos and COMP6010 resources
# and that researching how certain python operators / functions work is ok.
# [x] <== put an x in here to indicate you have read and agree to the above statements.
"""

def main():
    print("--- is_number ---")
    print(is_number(15)) # expected answer: True
    print(is_number(58.3)) # expected answer: True
    print(is_number(-12.4)) # expected answer: True
    print(is_number(-9192)) # expected answer: True
    print(is_number("Hello")) # expected answer: False
    print(is_number(False)) # expected answer: False

    print("--- process_number ---")
    print(process_number(58979943)) # expected answer: :ac+
    print(process_number(58979983)) # expected answer: :acS
    print(process_number(99985878)) # expected answer: cb:N

    print("--- ascii_sum_is_even ---")
    print(ascii_sum_is_even(False)) # expected answer: None
    print(ascii_sum_is_even(58182)) # expected answer: None
    print(ascii_sum_is_even("cat")) # expected answer: True
    print(ascii_sum_is_even("CATS")) # expected answer: False
    print(ascii_sum_is_even("This is a test")) # expected answer: False
    print(ascii_sum_is_even("!8rja#!@")) # expected answer: True

    print(" --- sum_two_lowest ---")
    print(sum_two_lowest("apjkdic")) # expected answer: 196
    print(sum_two_lowest("aakf")) # expected answer: 194
    print(sum_two_lowest("018kanciuq ")) # expected answer: 80
    print(sum_two_lowest("! a")) # expected answer: 65

    print(" --- ordered_by_lowest ---")
    print(ordered_by_lowest("abc", "oojf", "0anv")) # expected answer: 0anvabcoojf
    print(ordered_by_lowest("abc", "bb", "0anv")) # expected answer: 0anvabcbb
    print(ordered_by_lowest("abc", "aa", "0anv")) # expected answer: 0anvaaabc
    print(ordered_by_lowest("abc", "bb", "0~")) # expected answer: 0~abcbb
    print(ordered_by_lowest("abc", "bb", "~~")) # expected answer: abcbb~~

    print(" --- blat ---")
    print(blat(1, 5, 4.8)) # expected answer: True
    print(blat(1, 5, 4.8)) # expected answer: True
    print(blat(1, 2.4, 4.8)) # expected answer: True
    print(blat(9.1, 3.1, 4.8)) # expected answer: True
    print(blat(4, 5, 0)) # expected answer: True
    print(blat(True, 6, 8)) # expected answer: True
    print(blat(True, 6, 9)) # expected answer: False
    print(blat(True, False, 2)) # expected answer: False
    print(blat(4, False, 8)) # expected answer: True
    print(blat("This is a long string", False, "smol")) # expected answer: False
    print(blat("This is a long string", False, "large")) # expected answer: False
    print(blat("This is a long string", False, "larger")) # expected answer: True

    print(" --- get_information ---")
    print(get_information(192391)) # expected answer: The number 192391 contains 1 even digits, 5 odd digits and 2 prime digits
    print(get_information(-192391)) # expected answer: The number 192391 contains 1 even digits, 5 odd digits and 2 prime digits
    print(get_information(2818361)) # expected answer: The number 2818361 contains 4 even digits, 3 odd digits and 2 prime digits
    print(get_information(7777)) # expected answer: The number 7777 contains 0 even digits, 4 odd digits and 4 prime digits
    print(get_information(-19529)) # expected answer: The number 19529 contains 1 even digits, 4 odd digits and 2 prime digits
    print(get_information(2286)) # expected answer: The number 2286 contains 4 even digits, 0 odd digits and 2 prime digits
    
    print(" --- what ---")
    print(what("abc")) # expected answer: aabc
    print(what("abbc")) # expected answer: aabc
    print(what("abbcc")) # expected answer: aabc
    print(what("abbcceiou")) # expected answer: aabceeiioouu
    print(what("aaaeeeioio")) # expected answer: aaaaaaeeeeeeiiooiioo
    print(what("abbayeioub")) # expected answer: aabaayeeiioouu
    print(what("192391")) # expected answer: 1923


def is_number(value):
    """
    (12.5 marks)
    Given a variable, return True if the variable is of type int or float,
    False otherwise.
    """
    if isinstance (value, bool): # bool type check
        return False
    if isinstance (value, int): # int type check
        return True
    elif isinstance (value, float): # float type check
        return True
    else: # other cases check
        return False


def process_number(n : int):
    """
    (12.5 marks)
    Given an int, convert each group of two digits into their associated ascii 
    character value (hint: chr(int) function) and return a string with all the 
    characters. You may assume that the number has an even number of digits and
    is a positive number.
    Example:
    58979943 -> 58 97 99 43 -> ":ac+"

    You must perform type checking to ensure the inputs are of correct type. If
    the input is not of correct type, your function should return None
    """
    if not isinstance(n, int): # int type check
        return None
    
    n_str = str(n)  # convert the integer to a string to prepare for character convertion
    result = '' # define a string 

    for i in range(0, len(n_str), 2): 
        group = n_str[i:i+2] # group the number string to group of two
        result += chr(int(group)) # convert the groups and add them to the 'result' string
    
    return result # return final converted string


def ascii_sum_is_even(s : str):
    """
    (12.5 marks)
    Given a string, find the sum of ascii values of each character and return 
    True if the sum is even, False otherwise. You can find the ascii value of
    a character by using the ord() function.

    You must perform type checking to ensure the inputs are of correct type. If
    the input is not of correct type, your function should return None
    """
    if not isinstance (s, str): # str type check
        return None
    
    ascii_sum = 0 # give 'sum' an initial value
    for character in s:
        ascii_sum += ord(character) # calculate the sum of each character in the string

    if ascii_sum % 2 == 0: # odd or even check
        return True # return the final result
    else:
        return False # return the final result


def sum_two_lowest(s : str):
    """
    (12.5 marks)
    Given a string, find the two characters with the two lowest ascii values 
    in the string and return the sum of their ascii values
    """
    if not isinstance(s, str):  # type check
        return None

    # Give an initial value (highest possible ASCII value) to 2 lowest variables 
    lowest_1 = chr(127)  
    lowest_2 = chr(127)  

    # Loop through the string to find the two lowest characters
    for char in s: 
        if ord(char) < ord(lowest_1): # find the lowest ascii value 
            lowest_2 = lowest_1   
            lowest_1 = char  
                           
        elif ord(char) < ord(lowest_2): # find the second lowest ascii value
            lowest_2 = char 

    ascii_sum = ord(lowest_1) + ord(lowest_2) # calculate the sum

    return ascii_sum  # return the final result


def ordered_by_lowest(a, b, c):
    """
    (12.5 marks)
    Given three strings, calculate the sum of the two lowest ascii values for each string
    and return a string containing all three strings combined in ascending order based
    on the sum of their lowest ascii values

    You must complete this without sorting or lists.

    You must perform type checking to ensure the inputs are of correct type. If
    the input is not of correct type, your function should return None
    """
    if not (isinstance(a, str) and isinstance(b, str) and isinstance(c, str)):  # type check
        return None
    
    # redefine the sum_two_lowest function
    def sum_two_lowest(s : str):
        if not isinstance(s, str):  # type check
            return None

        # Give an initial value (highest possible ASCII value) to 2 lowest variables 
        lowest_1 = chr(127)  
        lowest_2 = chr(127)  

        # Loop through the string to find the two lowest characters
        for char in s: 
            if ord(char) < ord(lowest_1): # find the lowest ascii value 
                lowest_2 = lowest_1   
                lowest_1 = char  
                            
            elif ord(char) < ord(lowest_2): # find the second lowest ascii value
                lowest_2 = char 

        ascii_sum = ord(lowest_1) + ord(lowest_2) # calculate the sum

        return ascii_sum  # return the final result
    
    # Calculate sum of two lowest ascii values for each string
    sum_a = sum_two_lowest(a)
    sum_b = sum_two_lowest(b)
    sum_c = sum_two_lowest(c)
    
    # Combine strings according to ascending order of three previously calculated sum(s)
    if sum_c > sum_a and sum_c > sum_b: # sum_c is the largest
        if sum_a < sum_b:
            return a + b + c
        else:
            return b + a + c
    elif sum_b > sum_a and sum_b > sum_c: # sum_b is the largest
        if sum_a < sum_c:
            return a + c + b
        else: 
            return c + a + b
    else: # sum_a is the largest
        if sum_b < sum_c:
            return b + c + a
        else: 
            return c + b + a


def blat(a, b, c) -> bool:
    """
    (12.5 marks)
    Given three variables, return based on the following
    True if ANY of the following apply:
    - All variables are numbers (ints or floats)
    - At least two of the variables are even numbers
    - At least two of the variables are strings that are longer than 5 characters (exclusive)

    False otherwise.
    """
    if isinstance(a, bool) and isinstance(b, bool):
        return False
    elif isinstance(b, bool) and isinstance(c, bool):
        return False
    elif isinstance(c, bool) and isinstance(a, bool):
        return False
    else:
        # Check: At least two of the variables are even numbers
        if isinstance(b, int) and isinstance(c, int):
            if b % 2 == 0 and c % 2 == 0:
                return True 
        # Check: At least two of the variables are strings that are longer than 5 characters (exclusive)
        elif isinstance(b, str) and isinstance(c, str):
            if len(b) > 5 and len(c) > 5:
                return True
             
        # Check: At least two of the variables are even numbers
        if isinstance(a, int) and isinstance(c, int):
            if a % 2 == 0 and c % 2 == 0:
                return True
        # Check: At least two of the variables are strings that are longer than 5 characters (exclusive)
        elif isinstance(a, str) and isinstance(c, str):
            if len(a) > 5 and len(c) > 5:
                return True
        
        # Check: At least two of the variables are even numbers
        if isinstance(a, int) and isinstance(b, int):
            if a % 2 == 0 and b % 2 == 0:
                return True
        # Check: At least two of the variables are strings that are longer than 5 characters (exclusive)
        elif isinstance(a, str) and isinstance(b, str):
            if len(a) > 5 and len(b) > 5:
                return True
            
    # Check: All variables are numbers (ints or floats)
    if type(a) == int or type(a) == float:
        if type(b) == int or type(b) == float:
            if type(c) == int or type(c) == float:
                return True
         
    return False # return False as none previous conditions are met


def get_information(n : int):
    """
    (12.5 marks)
    Given an int, calculate the number of even digits, odd digits and prime digits.
    Return this information using the string format provided below.
    The number ____ contains ____ even digits, ____ odd digits and ____ prime digits

    For example if the number was 1838359, then the function should return the string:
    The number 1838359 contains 2 even digits, 5 odd digits and 4 prime digits

    For example if the number was 19, then the function should return the string:
    The number 15 contains 0 even digits, 2 odd digits and 1 prime digits

    You must perform type checking to ensure the inputs are of correct type. If
    the input is not of correct type, your function should return None

    You must complete this question without performing any string conversions
    """
    # Step 0: Type check
    if not type(n) == int:  
        return None

    # Step 1: Define is_prime function to check prime numbers
    def is_prime(digit):
        if digit < 2:
            return False
        for i in range(2, digit):
            if digit % i == 0:
                return False
        return True

    # Step 2: Assign the initial number to a variable name 'number' to store the initial number
    number = n
    
    # Step 3: Ensure both negative and positive number are counted
    if n < 0:
        n = n*(-1)
    else:
        n=n
    
    # Step 4: Initialize counters for each type of numbers (even, odd and prime)
    even_count = 0
    odd_count = 0
    prime_count = 0

    # Step 5: Loop through every digit in the number by respectively dividing the number (by 10)
    while n > 0:
        digit = n % 10
        if is_prime(digit) == True:
            prime_count += 1 # count prime digits
                
        if digit % 2 == 0: 
            even_count += 1 # count even digits
        else: 
            odd_count += 1 # count odd digits
        n //= 10 # assign back to value to n, after finishing every loop dividing n by 10

    return "The number", str(number), "contains", str(even_count), "even digits,", str(odd_count), "odd digits and", str(prime_count), "prime digits"


def what(s : str):
    """
    (12.5 marks)
    Given a string, perform the following operations:
    - Duplicate any vowels in the string. 
    - Keep only the first occurrence of each non vowel character in the string

    Note: the character b is not the same as the character B

    For example if the string was:
    abbayeioub
    then the string should become:
    aabaayeeiioouu

    Return the resulting string.

    You must perform type checking to ensure the inputs are of correct type. If
    the input is not of correct type, your function should return None
    """
    if not type(s) == str:   # type check
        return None

    seen_non_vowels = set()   # create a set to keep track of seen non-vowel characters
    result = ""   # create an empty string to store the result

    # Loop through each character in the string
    for char in s:
        if char.lower() in 'aeiou':
            result += char * 2 # duplicate the vowels
        elif char.lower() not in seen_non_vowels: 
            result += char # only add the 1st occurrence of each non-vowel character
            seen_non_vowels.add(char.lower()) # keep track of the seen_non_vowels

    return result # return the final result


if __name__ == "__main__":
    main()


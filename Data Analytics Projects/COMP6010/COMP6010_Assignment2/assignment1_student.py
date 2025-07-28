"""
# Student Declaration
# I [insert name and Student ID here] declare that this is my own work and that
# I have not used any code or logic from other people or from sources outside of the unit. 
# I understand that it is ok to look at COMP6010 videos and COMP6010 resources
# and that researching how certain python operators / functions work is ok.
# [] <== put an x in here to indicate you have read and agree to the above statements.
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
    # TODO To be completed
    return None


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
    # TODO To be completed
    return None


def ascii_sum_is_even(s : str):
    """
    (12.5 marks)
    Given a string, find the sum of ascii values of each character and return 
    True if the sum is even, False otherwise. You can find the ascii value of
    a character by using the ord() function.

    You must perform type checking to ensure the inputs are of correct type. If
    the input is not of correct type, your function should return None
    """
    # TODO To be completed
    return None


def sum_two_lowest(s : str):
    """
    (12.5 marks)
    Given a string, find the two characters with the two lowest ascii values 
    in the string and return the sum of their ascii values
    """
    # TODO To be completed
    return None


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
    # TODO To be completed
    return None


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
    # Check if all variables are numbers (ints or floats)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and isinstance(c, (int, float)):
        return True

    # Check if at least two of the variables are even numbers
    if (a % 2 == 0 and b % 2 == 0) or (a % 2 == 0 and c % 2 == 0) or (b % 2 == 0 and c % 2 == 0):
        return True

    # Check if at least two of the variables are strings that are longer than 5 characters
    if (isinstance(a, str) and len(a) > 5) and (isinstance(b, str) and len(b) > 5):
        return True
    if (isinstance(a, str) and len(a) > 5) and (isinstance(c, str) and len(c) > 5):
        return True
    if (isinstance(b, str) and len(b) > 5) and (isinstance(c, str) and len(c) > 5):
        return True

    # Return False if none of the conditions are met
    return False



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
    # TODO To be completed
    return None


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
    # TODO To be completed
    return None


if __name__ == "__main__":
    main()


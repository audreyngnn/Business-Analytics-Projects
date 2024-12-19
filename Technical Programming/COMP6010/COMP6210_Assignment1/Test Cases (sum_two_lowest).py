def sum_two_lowest(s: str):
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

print(" --- sum_two_lowest ---")
print(sum_two_lowest("apjkdic")) # expected answer: 196
print(sum_two_lowest("aakf")) # expected answer: 194
print(sum_two_lowest("018kanciuq ")) # expected answer: 80
print(sum_two_lowest("! a")) # expected answer: 65
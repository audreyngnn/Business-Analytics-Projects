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

print(" --- get_information ---")
print(get_information(192391)) # expected answer: The number 192391 contains 1 even digits, 5 odd digits and 2 prime digits
print(get_information(-192391)) # expected answer: The number 192391 contains 1 even digits, 5 odd digits and 2 prime digits
print(get_information(2818361)) # expected answer: The number 2818361 contains 4 even digits, 3 odd digits and 2 prime digits
print(get_information(7777)) # expected answer: The number 7777 contains 0 even digits, 4 odd digits and 4 prime digits
print(get_information(-19529)) # expected answer: The number 19529 contains 1 even digits, 4 odd digits and 2 prime digits
print(get_information(2286)) # expected answer: The number 2286 contains 4 even digits, 0 odd digits and 2 prime digits
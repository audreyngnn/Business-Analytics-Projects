def is_prime(n):
    if n == 1:
        return False
    for number in range(2,n):
        if n% number == 0:
            return False
    return True

def is_odd(n):
    return n % 2 == 1

def is_even(n):
    return not is_odd

print("Name in number_service " + __name__)

# Is this the file the program
# was launched with?
# If it is, execute some code

if __name__ == "__main__":
    number = 9
    print("is " + str(number) + " prime?" + str(is_prime(number)))
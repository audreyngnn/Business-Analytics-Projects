from cmath import log
from distutils.log import Log
from gettext import find
from random import random

def sum(n):
    """
    Return the sum of all integers in the range [1, n]
    """
    None

def count_divisible_by(n, start, end):
    """
    Count the numbers that are divisible by n in the range [start, end]. 
    Assume start <= end
    """
    None

def sum_even(start, end):
    """
    Return the sum of all even numbers in the range [start, end).
    Assume start < end and start is positive
    Challenge: solve it without using any if statement
    """
    None

def sum_even_2(n):
    """
    Return the sum of the first n positive EVEN integers (2+4+...+(2*n))
    """

def divisible_in_range(val, start, end):
    """
    Return true if val has a factor in the range [low, high] and false otherwise.
    remember that n%0 is undefined!
    """
    None

def is_prime(n):
    None

def num_primes(start, end):
    """
    Return the number of primes in the range (start, end)
    Assume start < end and start is non-negative
    """
    None

def binary(n):
    """
    Convert the positive number n to binary (base 2).
    Do not use the bin() function
    """
    None

def first_power(val, n):
    """
    return the first power of n that is
    not smaller than val. Do NOT use the
    built in pow() functions.
    
    For example: 
    val = 124, n = 5 -> since 5^3 = 125 return 125
    """
    None

def palindrome(str):
    """
    Return true is str is a palindrome and false otherwise.
    A palindrome is String that reads the same backwards and forwards.
    """
    None

def pyramids(n):
    """
    ADVANCED
    Based on https://open.kattis.com/problems/pyramids
    The number of bricks to build a pyramid of the following heights are:
        1: 1
        2: 10
        3: 35
        4: 84
    Given n blocks, what is the highest pyramid that can be built?
    """
    None

def scrambled_letters(str):
    """
    ADVANCED
    Given that the length of the input String is n, it will 
    contain n-1 of the first n lowercase letters of the 
    alphabet and 'z'.
    
    Every letter represents an index (a=0, b=1, c=2, ..) 
    that you should jump to. Given that you start at the 
    first letter in the String, how many jumps are needed to 
    reach 'z'?
    
    For example
        n = 3: 'bcz' will jump b -> c -> z. Answer 2
        n = 5: 'czecb' will jump c -> e -> b -> j. Answer 3
        
    Assume that the input will always have a valid solution.
    ord() function may be helpful.
    """
    None

def sum_multiple_even(start, end):
    """
    Sum the numbers in the range (start, end].
    But for every even number, add the sum of all
    later odd numbers (in the range) to the total sum.
    
    For example:
    start = 3, end = 8 -> sum = 3 + 4 + (5 + 7) + 5 + 6 + (7) + 7 = 44
    """
    None

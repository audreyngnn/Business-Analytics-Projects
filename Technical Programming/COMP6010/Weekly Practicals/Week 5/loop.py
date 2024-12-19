    #12.2
    # Edit the above code to print out the first "n" Fibonacci numbers, instead of all Fibonnaci numbers up to limit

limit = 4
if (limit > 1):
    print(1, end =", ") 
    print(1, end =", ")
    previousprevious = 1
    previous = 1
    currentNumber = 1 + 1

    y = 2

    while y < limit: #limit = 10, once y = :
        print(currentNumber, end =", ")
        previousprevious = previous
        previous = currentNumber
        currentNumber = previous + previousprevious
        y = y + 1

print(" end")
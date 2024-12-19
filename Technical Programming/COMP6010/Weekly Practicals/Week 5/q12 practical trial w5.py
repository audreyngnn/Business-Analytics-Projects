limit = 1000
if (limit > 1):
    print(1, end =", ")
    print(1, end =", ")
    currentNumber = 1 + 1
    previous = 1
    previousprevious = 1

    while currentNumber <= limit:
        print(currentNumber, end =", ")
        previousprevious = previous
        previous = currentNumber
        currentNumber = previous + previousprevious
print("end")
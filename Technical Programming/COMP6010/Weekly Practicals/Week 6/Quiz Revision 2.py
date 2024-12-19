def checkDivisible(n):
    for i in range (1, n):
        if n % i == 0:
            counter = 1
            if counter % 2 == 1:
                print("divisible")
                counter += 1
            else:
                print("DIVISIBLE")
                counter += 1
        else:
            print("no")

print(checkDivisible(20))
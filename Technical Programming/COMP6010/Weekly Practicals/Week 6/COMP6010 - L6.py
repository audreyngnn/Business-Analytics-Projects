# Week 6

#################################

def foo(n): # old version (week 5)
    k = 4
    return k + n

#ver2
def foo(n): # n = 20
    return n + bar(n - 3)
    #      20 + bar(17)
    #      20 + 5
    #      25

def bar(p): # p = 17
    return 5

print(foo(20)) #25

print('\n')
#ver3
def foo(n): # n = 20
    return n + bar(n - 3)
    #      20 + bar(17)
    #      20 + 33
    #      53

def bar(p): # p = 17
    number = zap(p - 3)     # zap(14) --> 28
    return 5 + number       # 5 + 28 -> returns 33

def zap(m):         # m = 14
    return m * 2    # returns 28

print(foo(20))      #53

# foo -> bar -> zap
# u go to the function call, and u return to the function call.


print('\n'*5)

def zap(n): # n = 11 (4)
            # n = 14
    return n + 1

def foo(n): # n = 10 (1)
    result = bar(n + 1) + bar(n + 4) + zap(n + 5)
    #        bar(11)    + bar(n + 4) + zap(n + 5) (2)
    #        12         + bar(14)    + zap(n + 5) (6)
    #        12         + 15         + zap(n + 5)
    #        12         + 15         + zap(15)
    #        12         + 15         + 16
    #        43
    return result

def bar(n): # n = 11 (3)
            # n = 14
    return zap(n) 
            # return 12 (5)
            # return 15

print(foo(10))






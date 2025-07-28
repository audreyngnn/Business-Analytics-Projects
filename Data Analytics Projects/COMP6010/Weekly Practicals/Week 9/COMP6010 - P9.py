"""Question 1: 
Create a list list_1 that contains any 10 numbers of your choice."""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

"""Question 2:
Display each item of the list separated by a comma and space, except 
there should be no comma or space after the last item."""

result = ""
for item in list_1:   
    if item < 10:
        result += str(item) + ", "
    else:
        result += str(item)
print(result)


result = ""
for i in range(0, len(list_1)-1):
    result += str(list_1[i]) + ", "
result += str(list_1[len(list_1)-1])
print(result)

for i in range (0, len(list_1)):
    print(str(list_1[i]), end = "")
    if i != len(list_1)-1:
        print(", ", end="")

print("\n")
"""Question 3: 
Create a list list_2 that contains any 5 numbers of your choice. 
Append list_2 to list_1."""

list_2 = [11, 12, 13, 14, 15]
list_12 = list_1 + list_2
print(list_12)

print("\n")
"""Question 4: 
Create a list list_3 that contains the pattern 0, 1, 2 repeated 
100 times (300 items in all)"""

# list = [0, 1, 2]
# list_3 = []

#while i < 100:
#    list_3 += list

"""Question 5: 
Define a function that when passed a list, returns the average of all 
the items in the list. Display the averages of the three lists created"""


def avg(list_i):
    sum = 0
    for i in range (0, len(list_i)):
        sum += i
    return sum/ len(list_i)
print(avg(list_1))


def avg_ver2(list):
    return sum(list)/ len(list)
print(avg_ver2(list_1))


"""Question 6: 
Define a function that when passed a list, returns the highest item in the list. 
Display the highest values in each of the three lists created"""

def max(list):
    max = list[0]
    for i in range (0, len(list)):
        if list[i] > max:
            max = list[i]
    return max

print(max(list_1))


"""Question 7: 
Define a function that when passed a list, returns a list containing 
all even numbers. The list passed should not be modified. Call the function by 
passing list_3 and store the result in list_4"""

def even(list):
    even_list = []
    for i in range (0, len(list)):
        if list[i] % 2 == 0:
            even_list.append(list[i])
    return even_list

print(even(list_1))

"""Question 8:
Define a function that when passed two lists, returns a merged list in a "zipline" fashion. 
That is, first item of the first list, followed by the first item of the second list, followed 
by the second item of the first list, followed by the second item of the second list, and so on.  
The two lists passed should not be modified. Call the function by passing list_1 and list_3, 
and store the result in list_5."""

list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_3 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def zip (list_a, list_b):
    final = []

    for i in range(0, len(list_a)):
        final.append(list_a[i])
        final.append(list_b[i])
    return final

print(zip(list_1, list_3))


list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_3 = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 30, 40]
def zipline(list1, list2):
    result = []
    i = 0
    while i < len(list1) and i < len(list2):
        result.append(list1[i])
        result.append(list2[i])
        i += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while i < len(list2):
        result.append(list2[i])
        i += 1
    
    return result

list_5 = zipline(list_1, list_3)
print(list_5)


"""Question 9:
Define a function that when passed two lists, returns True if they contain the same items 
(even though in a different order). Create a list list_7 = [10, 70, 20, 90, 30, 30, 80] and 
list_8 = [70, 80, 20, 90, 30, 30] and call the function on these two lists. Then append a 10 
at the end of list_8 and call the function again.""" 
list_7 = [10, 70, 20, 90, 30, 30, 80]
list_8 = [70, 80, 20, 90, 30, 30]

def same(list1, list2):
    r = False
    for i in range (len(list1)):
        for j in range (len(list2)):
            if list1[i] == list2[j]:
                r = True
    return r

print(same(list_7, list_8))

# solution chuan
def same_items(list1, list2):
    # import sort from math
    # c_list1 = sort(list1, True)
    # c_list2 = sort(list2, True)

    # return c_list1 == c_list2

    same = True
    for item in list1:
        if item not in list2:
            same = False
    return same
print(same(list_7, list_8))


"""Question 10:
For the remaining time, please work on the "d_list_tuples.py" file in the COMP6010 Practice Package."""



"""Question 11:
Define a function that when passed a list and a boolean value, returns the sorted version of the list. 
The passed list should not be modified. You cannot call any built-in function. The order of sorting should 
be based on the boolean value. If True, return in ascending order. If False, return in descending order. 
Call the function on list_1 and store the result in list_6."""

def min (list):
    m = list[0]
    for i in range (len(list)):
        if list[i]<m:
            m = list[i]
    return m

def max (list):
    m = list[0]
    for i in range (len(list)):
        if list[0]>m:
            m = list[i]
    return m

def sorted (list, bool):
    min_item = min(list)
    max_item = max(list)

    final = []

    if bool == True:
        for i in range(0, len(list)):
            min_item = min(list)
            final.append[min_item]
            list.pop(min_item) 
        
    if bool == False:
        for i in range(0, len(list)):
            max_item = max(list)
            final.append[max_item]
            list.pop(max_item) 


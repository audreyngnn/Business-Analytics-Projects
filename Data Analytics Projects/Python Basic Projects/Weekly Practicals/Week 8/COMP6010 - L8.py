name = "Micheal"
numbers = [1, 7, 2, 9, 1]
# index   0  1  2  3  4 

# Lists are a collection of items
# There are different types of collections
# Lists can be modified
# So u can change the contents of a list, and update them

print(type(numbers))
print(numbers)

name = "Micheal"
#With a String how do we access the 1st character?
print(name[0]) #M
print(numbers[3])
print(numbers)
print(numbers[-1]) # last item on the list
print(numbers[4])
print(numbers[ len(numbers) - 1 ])

print(numbers[1:3])
print(numbers)

numbers = numbers[1:3]

values = [True, "Hello", 58, 123.1]
print(values[1])
print(values[1][4])
#        Hello[4] the 4th character of the index [1]
#        the order does matter

print(values[1][4].upper())


# How do we know if something is inside of a list
values = [True, "Hello", 58, 123.1]
print(values.index(58)) # returns the index of the FIRST occurence of a match
                        # ValueError if it cannot find the given value

print((58 in values)) # will give us True or False

print("michael" in "My name is Micheal")


grades = [50, 99, 24, 75, 24, 0, 95, 75, 85, 38]
if 38 in grades:
    print("There was a 38")
else:
    print("No one got a 38")

#target_grade = input("Please enter a grade to look for")
#if target_grade in grades:
#    print("The target grade was found at index: " + str(grades.index(target_grade)))
#else:
#    print("No one got the given grade")

# Modifying the list
values = [True, "Hello", 58, 123.1]
print(values)
values[0] = "Modified"
print(values)

values[2] += 100
values[2] = values[2] + 100
print(values)

# Adding a new value to the list
values += [False, True, True]
print(values)

values.append(["number", 1, 2, 3])
print(values)

values += ["something", "else"]
print(values)

# Extend 
other_list = [1, 2, 3, 4]
values.extend(other_list) # Given another list, add all elements of the passed list
                          # to the list the method is called on
print(values)

# values.insert(index, value)
values.insert(3, "New string")
print(values)

values = [True, "Hello", 58, 123.1]
values.insert(10, "Test") # Adding to an index not in the list, will add to the end
print(values)

values.insert(-1, "Test") # Adding to the last index

# Geting rid of an index
values = [True, "Hello", 58, 123.1]
print(values)
values.remove(True)
print(values)

# Quick exercise
# What if we want to remove all of the Hellos
while "Hello" in values:
    values.remove("Hello")

# values.remove("This is not in the list") # will get an error

# Removing by giving an INDEX
values = [True, "Hello", 58, 123.1]
print(values)
values.pop() # Without a parameter, it removes the last item
values.pop(2) # With one number, pop removes what is at the given index
print(values)

# lists of lists
def foo(something: list):
    something += ['Something']

foo(values)
print("outside of function", values)

# Traversal
for character in "abd":
    print(character)

print("\n"*5)

items = [1, 2, 3, False, "Hello"]
for abc in items:
    if type(abc) == int:
        print(abc)
    else:
        print("Not value")

# Given a list of strings,count how many strings in the list, start with 'a'
items = ["hello", "apple", "Apricot", "John", "Michael", "amy"]
count_a = 0
for item in items:
    if item[0] == 'a':
        count_a += 1
print(count_a)

# Define a function, that when passed a list of items and a target character
# list = ["Caspoas", "apple", False, "Dog", "Cat", 58, 39.3]
# target = 'C'

# Returns how many times that character appears at the start of any
# items in the list

def count_occurences_at_start(values : list, character : str):
    count = 0
    for value in values:
        if type(value) == str and value[0] == character:
            count += 1
    return count

# Count how many times the character appears at any point in the string
# values = ['CCC, 'CC', 'ab']
# target = 'c'

def count_occurences(values : list, target : str):
    count_of_target = 0
    for item in values:
        for character in item:
            if character == target:
                count_of_target += 1
    return count_of_target

values = ['ccc', 'cc', 'djheugiegiegdiebk']
target = 'c'
print(count_occurences(values, target))

# All unique
# Given a list, return True if everything in the list in unique
# False otherwise
# What does unique mean?
# list = [1, 2, 3, 2, 5]


def is_unique(items: list):
    for i in range(0, len(items)):
        print(i)
        print(items[i])
    
    for i in range(0, len(items)):
        # i represents the index of the character 

        for j in range(i + 1, len(items)):
            # j represents the index of the other number we are comparing
            
            if items[i] == item[j]:
                return False
    return True

# given a list, return True if all items in the list are ordered in ascending order
# list = [1, 2, 3, 4, 5, 5, 6, 100, 104, 104, 105]

def is_ascending(values : list):
    for i in range(0, len(values)):
        if values[i] > values[i + 1]:
            return False
    return True




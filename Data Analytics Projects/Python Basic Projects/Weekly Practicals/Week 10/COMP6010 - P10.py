"""
Question 1:
Create a dictionary named countryCodes which will map country names to country codes based on this link. """
countryCodes = {}

"""
Question 2:
Add the following pairings, in the listed order, to countryCodes. """

countryCodes["China"] = "CN"
countryCodes["India"] = "IN"
countryCodes["Australia"] = "AU"
countryCodes["Croatia"] = "HR"
countryCodes["Turkey"] = "TR"

print(countryCodes)
print(countryCodes.keys())
print(countryCodes.values())

"""
Question 3:
Extract the full names of countries from countryCodes and 
Store them in a variable named extractedNames as a list.

"""
extractedNames = []
extractedNames.append(countryCodes.keys())
print(extractedNames)

extractedCodes = list(countryCodes.values())

"""
Question 5:

Store a mapping of room numbers to the floors on which the rooms exist. 

Rooms 100 to 199 should be designated as "First floor"
Rooms 200 to 299 should be designated as "Second floor"
...
Rooms 1000 to 1099 should be designated as "Tenth floor"
"""

floors = ["first", "second", "third", "forth", "fifth", "sixth",
          "seventh", "eighth", "ninth", "tenth"]
floormaps = {}
for i in range (100, 1100, 1):
    floormaps[i] = floors[(i//100)-1] # 100 - 199 -> 1, but what we need is index 0 (1-1)

    #if i // 100 == 1:
    #    floormaps[i] = "first"
    
    #if i // 100 == 2:
    #    floormaps[i] = "second"
    
    #...
    #if i // 100 == 10:
    #    floormaps[i] = "tenth"

"""
Question 6:
Given a room number, look-up the floor on which it exists and display it in the console. """

floors = ["first", "second", "third", "forth", "fifth", "sixth",
          "seventh", "eighth", "ninth", "tenth"]
floormaps = {}
for i in range (100, 1100, 1):
    floormaps[i] = floors[(i//100)-1] # 100 - 199 -> 1, but what we need is index 0 (1-1)

room = 1034
print(floormaps[room])


"""
Question 7:

Assume we have student names in a list students and their corresponding marks in a list grades. 
You may assume that marks of student at index i in students exist at index i in grades.

Create a dictionary of mappings from student names to their grades.

For example, if students = ["a", "b"] and grades = [17, 29], the dictionary would be {"a":17, "b":29}

"""
grades_dict = {}
students = ["a", "b", "c"]
grades = [100, 99, 95]

for i in range (0, len(students)):
    grades_dict[students[i]] = grades[i]

print(grades_dict)

"""
Question 8 *

Define a function that when passed a dictionary containing Account Holder to Account Balance mappings, 
returns the Account Holder with the highest balance. In case of a tie, return the first account holder encountered.

"""

def get_max (adict):
    max = 0
    maxholder = ""
    for holder, balance in adict.items():
        if balance > max:
            max = balance
            maxholder = holder
    
    print("Holder with highest balance:", str(maxholder))

AccountDict = {
    "A" : 17000,
    "B" : 1600500,
    "C" : 21000,
}


print("\n")
get_max(AccountDict)
        


""" Question 9 *

Define a function that when passed a dictionary containing Account Holder to Account Balance mappings, 
and another dictionary containing Account Holder to Telephone number, returns the phone number of the 
account holder with the highest balance. 

In case of a tie, return the phone number of the first account holder encountered.

"""
# dict = {
# "key" : "value",
# }

# dict.keys()
# dict.values()
# dict.items()



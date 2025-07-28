"""
Dictionaries
"""

numbers = [1, 2, 3]
#indexed    0  1  2
print(numbers[1])

numbers = [80, 91, 83, 19, 41]
#indexed    0   1   2   3   4
print(numbers[4])
print(numbers[-1])
print(numbers[len(numbers)-1])

# lists are accessed using index to value pairs

numbers = [80, 91, 83, 19, 41] # a list

student_grades = {
    "michael": 32,
    "akshidh": 75,
    "raya": 90,
    "nafi": 85,
} # a dictionary

if "michael" in student_grades:
    print("the KEY michael is in the dictionary")


if 32 in student_grades:
    print("Y")
else:
    print("N")


print("\n"*5)
print(student_grades["akshidh"])
print(student_grades["michael"])

names = ["michael", "bob", "miku"]
if "michael" in names:
    print("Michael is in the list")

# key value pairs
# key of any data type
# which goea to a value of any daya type

# IF we want to access a dictionary, but we don't know
# whether a key EXISTS, we must first check it is in the dictionary.

if "sarah" in student_grades:
    # do something
    pass

print(student_grades.get("michael", 0))
#                        ^ key we are trying to access
#                                   ^ default value

print("Next thing is to")
student_grades = {
    "michael": 32,
    "akshidh": 75,
    "raya": 90,
    "nafi": 85,
} # a dictionary

numbers = [10, 20, 30]
numbers[2] = 40
print(numbers)

student_grades["miku"] = 100
print(student_grades)

# keys can be ALMOST anything
# the keys have to be imutiable (can't be changed)

my_data = {
    False : 0,
    True : 1,
}

my_other_data = {
    1 : "one",
    10 : "ten",
    100: "100",
}

my_other_other_data = {
    False: 0,
    "Michael" : 50,
    59.2 : "Hello",
} # data type doesn't matter

print(student_grades)
student_grades.pop("michael") # must be a key
print(student_grades)

print(student_grades)
if "john" in student_grades:
    student_grades.pop("john") # must be a key
print(student_grades)

print(student_grades.keys())

student_names = student_grades.keys()
print(student_names)
# keys, gives you back the keys as a dict_key object
# we can wrap it in the list() conversion call
# which will convert it to an actual list

student_names = list(student_grades.keys())
for name in student_names: # student_names is a list
    # this loop takes one name from the list and
    # stores it into the name variable
    print(student_grades[name])
    # we are specificying a key (which is a name)
    # and using that key to access the dictionary

the_actual_grade_of_students = student_grades.values()
print(the_actual_grade_of_students)


print(student_grades.items())

my_numbers = [1, 2, 3]
my_tuple = (1, 2, 3)

# a list is similar to a tuple but 
# a tuple can't be modified.

a, b, c = [1, 2, 3]
# unpacking 
print(a + b + c)
# unpacking for a tuple

for something in student_grades.items():
    print(something[0] + " has a grade of " + str(something[1]))

print("\n")

for key, value in student_grades.items():
    print(key + " has a grade of " + str(value))


student_information = {
    4581813: {
        "name: ["michael","lay"],
        "email": "michael.lay@mq.edu.au",
        "bod": {
            "year": 1938,
            "month": 5,
            "day": 24
        }
    },

    4818131: {
        "name": "Carl",
        "email": "carl.svenson@edu.au"
    }
}

print("\n"*5)
print(student_information)
print(student_information[4581813]["name"][1])

for key in student_information:
    print(student_information[key]["email"])

for values in student_information.values():
    print(values["email"])


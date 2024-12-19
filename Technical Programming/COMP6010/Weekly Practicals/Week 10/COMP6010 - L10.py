# Week 10

# lists, dicts = collections
names = ["michael", "sarah"]
id = [12314, 151512]
email = ["michael.lay@mq.edu.au", "sarah@mq.edu.au"]
dob = ["12/12/20","10/10/10"]

information = [
    {"michael", 12314, "michael.lay@mq.edu.au", "12/12/20"},
    {"sarah", 151512, "sarah@mq.edu.au", "10/10/10"},
]

print(information[0][0])

information = {
    12314: {
        "name" : "michael",
        "email" : "michael.lay@mq.edu.au",
        "dob" : "12/12/20",
        "phone" : 90218181,
    },
    151512 : {
        "name" : "sarah",
        "email" : "sarah@mq.edu.au",
        "dob" : "10/10/10",
    },
}

# information{151251} = {
#    "name" : "john",
#    "address" : "macquarie university",
#}

# information[12314]["name"]


# Class definition
class Student:
    name = "Michael"
    email = "michael.lay@mq.edu.au"
    dob = "10/10/10"

# object -  make an instance of the class

student_1 = Student() # This makes an object that u can interact with

# The variable contains a reference to a Student object

print(student_1)

name = "michael"
name.upper # (name = location, "." go to the location, and add that location, what do u want?)

# our object holds location,
print(student_1.name)
print(student_1.email)

student_2 = Student()

print(student_1.name)
print(student_2.name)

# Change the object value
student_1.name = "John"
student_2.name = "Bella"

print(student_1.name)
print(student_2.name)

student_1 = Student() # student_1 contains a Student object   0x81271
student_2 = student_2 # copy the old location of the object   0x81271
student_1.name = "clara"
print(student_2.name)



student_3 = Student()
student_3.name = "Carl"
student_3.email = "carl.svensson@mq.edu.au"
student_3.dob = "9/9/9"

class Student:
    name = "Michael"
    email = "michael.lay@mq.edu.au"
    dob = "10/10/10"

    # method - function that belongs to an object/ instance
    # instance method
    def __init__(self, n, e, d):
        # self is a reference to the object being used
        # don't need to pass self to use it
        self.name = n
        # without self. name is making a LOCAL variable
        # can only be used in the def
        self.email = e
        self.dob = d

student_4 = Student("Bob", "bob@mq.edu.au", "5/5/5")
print(student_4.name)
print(student_4.email)
print(student_4.dob)


class Student:
    def __init__(self, n, e, d, g):
        self.name = n
        self.email = e
        self.dob = d
        self.grades = g

student_5 = Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 31, 90, 100])
print(student_5.name)
print(student_5.email)
print(student_5.dob)
print(student_5.grades)

# Objects can hold any type of data
# In the above, ex, it now also holds a list

sum = 0
for value in student_5.grades:
    sum += value
average = sum / len(student_5.grades)
print(average)

student_6 = Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 51, 20, 10])
print(student_6.name)
print(student_6.email)
print(student_6.dob)
print(student_6.grades)

sum = 0
for value in student_5.grades:
    sum += value
average = sum / len(student_5.grades)
print(average)

class Student:
    def __init__(self, n, e, d, g):
        self.name = n
        self.email = e
        self.dob = d
        self.grades = g

    def get_wam(self):
        sum = 0
        for value in self.grades:
            sum += value
        average = sum/ len(self.grades)
        return average

student_6 = Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 51, 23, 20, 10])
print("student_6", student_6)
student_6.get_wam()

students = [
    Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 51, 23, 20, 10]),
    Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 51, 23, 20, 10]),
    Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 51, 23, 20, 10]),
    Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 51, 23, 20, 10])
]


class Student:
    def __init__(self, name, email, dob, grades = [], years_to_complete = 3):
        self.name = name
        self.email = email
        self.dob = dob
        self.grades = grades
        self.years_to_complete = years_to_complete

    def get_wam(self):
        sum = 0
        for value in self.grades:
            sum += value
        average = sum/ len(self.grades)
        return average

student_7 = Student("Bob", "bob@mq.edu.au", "5/5/5", [80, 5, 15, 51, 23, 20, 10], 10)
print(student_7.years_to_complete)

student_7 = Student("Bob", "bob@mq.edu.au")

class Student:
    def __init__(self, name, email, dob, grades = [], years_to_complete = 3):
        if "@" not in email:
            email = email + "@mq.edu.au"

        self.name = name
        self.email = email
        self.dob = dob
        self.grades = grades
        self.years_to_complete = years_to_complete

    def get_wam(self):
        sum = 0
        for value in self.grades:
            sum += value
        average = sum/ len(self.grades)
        return average

student_7 = Student("Bob", "bob.mq.edu.au")
print(student_7.email)

class Student:
    def __init__(self, name, email, dob, grades = [], years_to_complete = 3):
        if "@" not in email:
            email = email + "@mq.edu.au"

        self.name = name
        self.email = email
        self.dob = dob
        self.grades = grades
        self.years_to_complete = years_to_complete

    def get_wam(self):
        sum = 0
        for value in self.grades:
            sum += value
        average = sum/ len(self.grades)
        return average
    
    def reduce_study_time(self):
        self.years_to_complete -= 1


student_8 = Student("Bob", "bob.mq.edu.au")
student_8.years_to_complete -= 1

student_10 = Student("Bob", "bob.mq.edu.au")
student_11 = Student("Bob", "bob.mq.edu.au")
if student_10 == student_11:
    print("The same student")
else:
    print("Not the same student")
# compare outside, but what we need to is compare what inside

if student_10.name == student_11.name and student_10.email == student_11.email:
    print("The same student")
else:
    print("Not the same student")


class Student:
    def __init__(self, name, email, dob, grades = [], years_to_complete = 3):
        if "@" not in email:
            email = email + "@mq.edu.au"

        self.name = name
        self.email = email
        self.dob = dob
        self.grades = grades
        self.years_to_complete = years_to_complete

    def get_wam(self):
        sum = 0
        for value in self.grades:
            sum += value
        average = sum/ len(self.grades)
        return average
    
    def reduce_study_time(self):
        self.years_to_complete -= 1

    def is_the_same(self, other):
        # To compare two students,
        # How many student do we need?
        if self.name == other.name and self.email == other.email:
            return True
        else:
            return False
        

student_10.is_the_same(student_11)

class Student:
    def __init__(self, name, email, dob, grades = [], years_to_complete = 3):
        if "@" not in email:
            email = email + "@mq.edu.au"

        self.name = name
        self.email = email
        self.dob = dob
        self.grades = grades
        self.years_to_complete = years_to_complete

    def get_wam(self):
        sum = 0
        for value in self.grades:
            sum += value
        average = sum/ len(self.grades)
        return average
    
    def reduce_study_time(self):
        self.years_to_complete -= 1

    def __eq__(self, other):
        # by calling the function __eq__, we can rewrite how the "==" works
        # To compare two students,
        # How many student do we need?
        if self.name == other.name and self.email == other.email:
            return True
        else:
            return False

student_10 = Student("Bob", "bob.mq.edu.au")
student_11 = Student("Bob", "bob.mq.edu.au")

if student_10 == student_11:
    print("The same student")
else:
    print("Not the same student")


class Student:
    def __init__(self, name, email, dob, grades = [], years_to_complete = 3):
        if "@" not in email:
            email = email + "@mq.edu.au"

        self.name = name
        self.email = email
        self.dob = dob
        self.grades = grades
        self.years_to_complete = years_to_complete

    def get_wam(self):
        sum = 0
        for value in self.grades:
            sum += value
        average = sum/ len(self.grades)
        return average
    
    def reduce_study_time(self):
        self.years_to_complete -= 1

    def __eq__(self, other):
        # by calling the function __eq__, we can rewrite how the "==" works
        # To compare two students,
        # How many student do we need?
        if self.name == other.name and self.email == other.email:
            return True
        else:
            return False
        
    def __str__(self):
        return "Student(name=" + self.name + ", bod=" + self.dob + ", grades=" +str(self.grades)"
        # return ("Student(name={self.name}), dob={self.dob}, grades = {self.grades}")

student_10 = Student("Bob", "bob.mq.edu.au")
student_11 = Student("Bob", "bob.mq.edu.au")
print(student_10)

class DOB:
    def __init__(Self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

class Student:
    def __init__(self, name, email, dob, grades = [], years_to_complete = 3):
        self.name = name
        self.email = email
        self.dob = dob

"""
Student ===> name
            email
            dob ------> year
                        month
                        day
"""

student_20 = Student("Michael", "michael.lay@mq.edu,au", DOB("1923, "13, "4"))
student_20.dob.year



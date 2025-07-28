"""
[COMP6010] Week 11
"""

import pprint

# f = open("fav_words.txt","r")
#       path to a file
# relative paths
# absolute paths

# print(f)

# data = f.read()
# print(data)

# When reading in a file, Python uses a 'cursor' system
# When you first open a file, the cursor is placed
# at the start of the file

# Read advances the cursor through all the character
# in the file
# when we call read again, the cursor is at the end 
# so there are no characters in the file

f = open("Week 11/fav_words.txt","r")
data = f.readline()
print(data)
# data = f.readline()
print(data)

for i in range (len(data) - 1):
# before I before the last line of the list
    data[i] = data[i][:-1]

print(data)

f = open("Week 11/fav_words.txt","r")
"""
- r read
- r+ read and write (non destructive, doesn't make it if doesn't exist)
- w write (destructive, creates if doesn't exist)
- w+ write and read (destructive, creates if doesn't exist)
- a write but handle is at the end (append)
- a+ write and read, (creates if doesn't exist)
"""

# f = open("Week 11/file.txt","w")
f = open("Week 11/fav_words.txt","a+")
f.write("Hello")
new_information = ['Hello','this','is','some','data']
for word in new_information:
    f.write("\n" + word)

f.close()

with open("Week 11/fav_words", "a+") as f:
    print(f)

print("Up to here")

print("\n"*10)

with open("Week 11/student_information.csv","r") as f:
    clean_data = []
    for line in f.readlines():
        # doing some cleaning
        line = line[:-1]
        line = line.split(",")
        # '31890191, Michael, 40

        parts = []
        for i in range (len(line)):
            if line[i] == ',':
                parts += line[:i]

        clean_data += [parts]
    
    pprint.pprint(clean_data)

with open("Week 11/student_information.csv","r") as f:
    clean_data = []
    for line in f.readlines():
        # doing some cleaning
        line = line[:-1]
        line = line.split(",")
        # '31890191, Michael, 40
        clean_data += [line]
    
    pprint.pprint(clean_data)

    for row in clean_data[1:]:
        print(row[1])

with open("Week 11/student_information.csv","r") as f:
    clean_data = {
        "1231231" : {
            "name" : "Michael",
            "grade" : 50
        }
    }
    cleaned_data = {}
    for line in f.readlines():
        # doing some cleaning
        line = line[:-1]
        line = line.split(",")
        # '31890191, Michael, 40
        clean_data[line[0]] = {
            'name' : line[1],
            'grade' : line[2],
        }
    
    pprint.pprint(clean_data)

class Student():
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.naem = name
        self.grade = grade
    





# CodeAcademy course: Student Becomes the Teacher
# http://www.codecademy.com/courses/python-beginner-en-qzsCL

# initialize the student data
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

students = [lloyd, alice, tyler]

for person in students:
    print person["name"]
    print person["homework"]
    print person["quizzes"]
    print person["tests"]
    
def average(lst):
    return float(sum(lst))/len(lst)
    
def get_average(student):
    return average(student["homework"])*0.1 + average(student["quizzes"])*0.3 + average(student["tests"])*0.6

# Jennie's comment - I am really far behind! Also, if this were real code,
# I would want to keep these values in a CSV and import them into this script :)

# Linda: This is lesson 8:
class_list = [lloyd, alice, tyler]

def get_class_average(class_list):
    x = 0
    for item in class_list:
        x += (get_average(item))
    return x / len(class_list)

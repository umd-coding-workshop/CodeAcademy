# CodeAcademy course: Student Becomes the Teacher
# http://www.codecademy.com/courses/python-beginner-en-qzsCL

import json

# open the data file in read mode
f = open("data.json", "r")
# load the data (stored as a json object) into the students list
students = json.load(f)
    
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

def get_letter_grade(score):
    if score >= 90: 
        return "A"
    if score >= 80 and score <90: 
        return "B"
    if score >=70 and score <80:
        return "C"
    if score >=60 and score <70:
        return "D"
    if score <60:
        return "F"
        
grade = get_average(lloyd)
print get_letter_grade(grade)

# Linda: This is lesson 8:

def get_class_average(class_list):
    x = 0
    for item in class_list:
        x += (get_average(item))
    return x / len(class_list)

get_class_average(students)

# list comprehension examples
#
numbers = [1, 2, 3]
new_numbers = [n + 1 for n in numbers]
print(new_numbers)

name = 'Angela'
new_list = [letter for letter in name]
print(new_list)

new_range = [n * 2 for n in range(1, 5)]
print(new_range)

names = ['Luis', 'Monika', 'Beth', 'Caroline', 'Dave', ]
short_names = [name for name in names if len(name) < 5]
upper_names = [name.upper() for name in names if len(name) > 5]
print(short_names)
print(upper_names)
# Exercise 1 - Squaring Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n * n for n in numbers]

print(squared_numbers)
# Exercise 2 - Filtering Even Numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

result = [num for num in numbers if int(num % 2) == 0]

print(result)
# Exercise 3 - Data Overlap
# with open('file2.txt', 'r') as f:
#     print(f.readlines())

list1 = ['3\n', '6\n', '5\n', '8\n', '33\n', '12\n', '7\n', '4\n', '72\n', '2\n', '42\n', '13\n']
list2 = ['3\n', '6\n', '13\n', '5\n', '7\n', '89\n', '12\n', '3\n', '33\n', '34\n', '1\n', '344\n', '42\n']
result = [int(element) for element in list1 if element in list2]
print(result)

# Dictionary Comprehension
import random

names = ['Luis', 'Monika', 'Beth', 'Caroline', 'Dave', ]

student_score = {student: random.randint(1, 100) for student in names}
print(student_score)

passed_students = {student: grade for (student, grade) in student_score.items() if grade >= 60}
print(passed_students)

# Exercise 4 - Dictionary Comprehension 1
sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

sentences = ['What', 'is', 'the', 'Airspeed', 'Velocity', 'of', 'an', 'Unladen', 'Swallow?']
result = {letter: len(letter) for letter in sentences}

print(result)

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

weather_f = {days: ((temp * 9 / 5) + 32) for (days, temp) in weather_c.items()}

print(weather_f)
# Iterate over a Pandas DataFrame
import pandas as pd

students_dict = {
    'students': ['luis', 'monika', 'Pepe'],
    'score': [62, 78, 55]
}
students_dict_frame = pd.DataFrame(students_dict)
print(students_dict_frame)
for (index, row) in students_dict_frame.iterrows():
    print(row.students)

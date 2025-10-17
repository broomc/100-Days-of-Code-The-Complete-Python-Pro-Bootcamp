# List Comprehension
numbers = [1,2,3]
new_list = [n + 1 for n in numbers]
#print(new_list)

name = "Clive"      
new_name = [l for l in name]

new_range = [r*2 for r in range(1,5)]

names = ['Alex','Beth',"Caroline","Dave","Eleanor","Freddie"]

short_names = [ short for short in names if len(short) <= 4]
#print(short_names)
upper_5_names = [upper.upper() for upper in names if len(upper) >= 5]
#print(upper_5_names)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n**2 for n in numbers]
#print(squared_numbers)

list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(n) for n in list_of_strings]
result = [n for n in numbers if n % 2 == 0]
#print(result)
print(names)

import random

student_scores = {student:random.randint(1,100) for student in names}
print(student_scores)

passed_students = {student:score for (student,score) in student_scores.items() if score >= 60}
print(passed_students)

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
words = sentence.split()
result = {word:len(word) for word in words }
print(words)
print(result) 

weather_c = {"Monday": 12, "Tuesday": 14, "Wednesday": 15, "Thursday": 14, "Friday": 21, "Saturday": 22, "Sunday": 24}

weather_f = {day:c*9/5 + 32 for (day,c) in weather_c.items()}

print(weather_f)
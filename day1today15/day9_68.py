programming_dictionary = {"Bug": "An error in a program that prevents the program from running as expected.", "Function": "A piece of code that you can easily call over and over again.","Loop": "The action of doing something over and over again"}


print(programming_dictionary["Bug"])

empty_dictionary = {}
#programming_dictionary = {}
#print(programming_dictionary)
#programming_dictionary["Bug"] = "A moth in a computer"

#print(programming_dictionary)

for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])

student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = student_scores

print(student_grades)

for grade in student_grades:
    if student_grades[grade] >= 91 and student_grades[grade] <= 100:
        student_grades[grade] = 'Outstanding'
    elif student_grades[grade] >= 81 and student_grades[grade] <= 90:
        student_grades[grade] = 'Exceeds Expectations'
    elif student_grades[grade] >= 71 and student_grades[grade] <= 80:
        student_grades[grade] = 'Acceptable'
    elif student_grades[grade] <= 70:
        student_grades[grade] = 'Fail'


print(student_grades)
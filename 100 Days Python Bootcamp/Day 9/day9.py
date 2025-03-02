student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = student_scores

# print(student_grades)

for name, grade in student_grades.items():
    print(name, grade)
    # if grades <= 70:
    #     student_grades[grades] = "Fail"
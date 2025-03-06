student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}

student_grades = student_scores

print(student_grades)

for name, grade in student_grades.items():
    if grade >= 91:
        print(f"{name} você tirou {grade}: Outstanding")
    elif grade >= 81:
        print(f"{name} você tirou {grade}: Exceeds")
    elif grade >= 71:
        print(f"{name} você tirou {grade}: Acceptable")
    else:
        print(f"{name} você tirou {grade}: Fail")
grade_book = {
    'Aisha': 97,
    'Donald': 78,
    'Emil': 89,
    'Sandy': 36,
    'Angelina': 29
}

print('The class average is : ',average)
lowest_score = min(grade_book.values())
print('The lowest score is', lowest_score)
highest_score = max(grade_book.values())
print('The Highest score is ', highest_score)
student_name = input('Enter a student name: ')

grade = grade_book.get(student_name)

if grade is not None:
    print(student_name, ':', grade)
else:
    print('Student not found')

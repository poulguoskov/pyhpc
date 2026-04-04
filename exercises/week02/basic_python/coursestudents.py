from student import Student

def coursestudents(students, course):
    return [s.name for s in students if s.attends(course)]

students = [Student('A', ['01005']), Student('B', ['02613']), Student('C', ['01005', '02613'])]
print(coursestudents(students, '02613'))
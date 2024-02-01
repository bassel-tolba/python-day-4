students_heights = input("input a list of student heights ").split()
for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])
print(students_heights)
total = 0
for student in students_heights:
    total = total + student
print(total)
lee = 0
for num in students_heights:
    lee = lee + 1
print(round(total / lee, 2))
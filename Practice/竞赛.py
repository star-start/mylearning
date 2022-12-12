# # Read the input
# n, c = input().split()
# n = int(n)
#
# # Parse the input data
# data = []
# for i in range(n):
#     line = input().split()
#     data.append({
#         'id': line[0],
#         'chinese': int(line[1]),
#         'math': int(line[2]),
#         'physics': int(line[3]),
#         'chemistry': int(line[4]),
#         'politics': int(line[5]),
#         'history': int(line[6])
#
#     })
#
# # Compute the total scores for each student
# for student in data:
#     student['total'] = student['chemistry'] + student['physics'] + student['politics'] + student['history'] + student['chinese'] + student['math']
#
# # Select the top students for each contest
# b_students = sorted(data, key=lambda x: (x['chemistry'] + x['math'], x['id']), reverse=True)
# i_students = sorted(data, key=lambda x: (x['physics'] + x['math'], x['id']), reverse=True)
# h_students = sorted(data, key=lambda x: (x['politics'] + x['history'], x['id']), reverse=True)
#
# # Print the selected students for the specified contest
# if c == 'B':
#     for student in b_students[:1]:
#         print(student['id'])
# elif c == 'I':
#     for student in i_students[:]:
#         print(student['id'])
# elif c == 'H':
#     for student in h_students[:1]:
#         print(student['id'])


"""
n, s = input().split()
n = int(n)
students = []
for i in range(n):
    a, *sc = list(map(int, input().split()))
    sc = [a, *sc]
    students.append(sc)

students.sort(key=lambda x: (-x[s == 'B' and 4 or s == 'I' and 3 or 6], -x[2]))
for i in range(n):
    if students[i][1:] == students[0][1:]:
        print(students[i][0])

"""
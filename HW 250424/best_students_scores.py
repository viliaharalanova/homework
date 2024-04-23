student_scores = [
    ['Ivan', 5.00],
    ['Alex', 3.50],
    ['Maria', 5.50],
    ['Georgy', 5.00]
]

# best_students_scores = [
#     score
#     for score
#     in student_scores
#     if score[1] > 4
# ]

best_students_scores = []
for i in range(len(student_scores)):
    if student_scores[i][1] > 4.00:
        best_students_scores.append(student_scores[i])

for i in range(0, len(best_students_scores)):
    print(f'{best_students_scores[i][0].ljust(8, ' ')} - {best_students_scores[i][1]}')
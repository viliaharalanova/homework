student_scores = [
    ['Ivan', 5.00],
    ['Alex', 3.50],
    ['Maria', 5.50],
    ['Georgy', 5.00]
]

scores=[
    score[1]
    for score
    in student_scores
]

max_index = scores.index(max(scores))
min_index = scores.index(min(scores))

print(f'Student with max score: {student_scores[max_index][0]} ({student_scores[max_index][1]})')
print(f'Student with min score: {student_scores[min_index][0]} ({student_scores[min_index][1]})')
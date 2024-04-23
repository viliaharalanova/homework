w = float( input('Enter weight in kg:') )
h = float( input('Enter height in cm:') )
hm = h/100

bmi = w / hm**2
bmi =round(bmi, 2)
print(f'BMI={bmi}')

# print(f'BMI={bmi}')
# if bmi < 16:
#     print('Underweight (Severe thinness)')
# elif bmi < 17:
#     print('Underweight (Moderate thinness)')
# elif bmi < 18.5:
#     print('Underweight (Mild thinness)')
# elif bmi < 25:
#     print('Normal range')
# elif bmi < 30:
#     print('Overweight (Pre-obese)')
# elif bmi < 35:
#     print('Obese (Class I)')
# elif bmi < 40:
#     print('Overweight (Class II)')
# else:
#     print('Overweight (Class III)')



levels = [
    (16, 'Underweight (Severe thinness)'),
    (17, 'Underweight 2 (Moderate thinness)'),
    (18.5, 'Underweight 3 (Mild thinness)'),
    (25, 'Normal range'),
    (30, 'Overweight (Pre-obese)'),
    (35, 'Obese (Class I)'),
    (40, 'Overweight (Class II)'),
    (99999, 'Overweight (Class III)')
]

for level in levels:
    min_score, level_name = level
    if bmi < min_score:
        print(level_name)
        break

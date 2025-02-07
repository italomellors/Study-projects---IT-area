'''

Develop logic that reads a person's weight and height, calculates their BMI
and show your status, according to the table below:

- below 18.5: underweight
- between 18.5 and 25: ideal weight
- 25 to 30: overweight
- 30 to 40: obesity
- above 40: morbid obesity
'''
print('-----' * 10)
print('BMI CALCULATOR')
print('-----' * 10)

weight = float(input('Digite your weight: '))
height = float(input('Digite your height: '))

bmi = (weight / (height * height))
print(f'BMI: {bmi:.2f}')

if bmi <= 18.5 :
    print('underweight')
elif 18.5 < bmi <= 25 :
    print('ideal weight')
elif 25 < bmi <= 30 :
    print('overweight')
elif 30 < bmi <= 40 :
    print('obesity')
elif bmi >= 40 :
    print('morbid obesity')
#completed

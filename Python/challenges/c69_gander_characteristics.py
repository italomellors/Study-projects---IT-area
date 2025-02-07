'''
Create a program that reads the age and gender of multiple people.
For each registered person, the program must ask
whether the user wants to continue or not.
At the end, show:
a) how many people are over 18 years old
b) how many men were registered
c) how many women are under 20 years old
'''
count = 1
continue_register = ' '
over_18 = 0
men_count = 0
women_under_20 = 0
age = 0

while continue_register != 'n':
    try:
        print(f'Person ({count})')
        age = int(input('Enter the age: '))
        gender = str(input('Enter the gender (M / F): '))
        
        if gender == 'm':
            gender_type = 'Male'
        elif gender == 'f':
            gender_type = 'Female'
        else:
            print('Invalid gender! Enter (M / F)')
            continue
    except ValueError:
        print('Error! Enter a valid value.')
    
    if age > 18:
        over_18 += 1
    if gender == 'm':
        men_count += 1
    if gender == 'f' and age < 20:
        women_under_20 += 1
    
    count += 1
    print('---' * 10)
    print(f'RESULT ({count - 1})')
    print(f'People over 18: {over_18}')
    print(f'Number of men: {men_count}')
    print(f'Women under 20: {women_under_20}')
    continue_register = input('Do you want to continue? [S / N]: ')
    print('---' * 10)

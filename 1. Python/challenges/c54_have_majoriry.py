from datetime import date
''' Create a program that reads the birth year of seven people
At the end, show how many people have not yet reached the age of majority
and how many are already bigger'''
# Create a program that reads the birth year of seven people
# At the end, show how many are minors and how many are adults
print("Adults and Minors")
adults = 0
minors = 0
current_year = 2025
for p in range(1, 8):
    birth_year = int(input('Enter birth year: '))
    if current_year < birth_year:
        print('Invalid year!!')
        continue
    if (current_year - birth_year) < 18:
        minors += 1
    else:
        adults += 1
print(f'Minors: {minors}')
print(f'Adults: {adults}')
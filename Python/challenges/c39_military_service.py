'''
Make a program that reads the year of birth of a young person and informs
according to your age:

- If he will still enlist for military service
- If it's time to enlist
- If it is past the enlistment time

Your program should also show the time left or past the deadline
'''
from datetime import datetime
print('-----' * 10)
print('MILITARY SERVICE')
print('-----' * 10)

age_brith = int(input('when is your year of birth: '))
current_year = 2025
personal_age = current_year - age_brith
print(f'Pesonal age: {personal_age} years')

if personal_age < 18 :
    time_enlist = 18 - personal_age
    print(f'Time to enlist: {time_enlist} years ')
elif personal_age > 18 :
    past_elisment = personal_age - 18
    print(f'past the enlistment time: {past_elisment} years')
elif personal_age == 18 :
    print('time to enlist')
    
# completed
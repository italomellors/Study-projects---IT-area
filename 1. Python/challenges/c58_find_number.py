''' game where the computer will "think"
to a number between 0 and 100. 
- Choose a number from 0 to 100. 
- you have 10 attempts to find the chosen number.
- the program will tell you if the user's number 
is greater or less than the one chosen.
But now the player will try to guess until he gets it right, 
showing at the end how many guesses were needed to win
'''
import random
print('-----' * 10)
print('Find Number')
print('-----' * 10)
print('* Instrutions * ')
print(' - Choose a number from 0 to 100.')
print(' - you have 10 attempts to find the chosen number')
attempts = 1
chosen_number = random.randint(1,100)
#print(f'chosen_number: {chosen_number}')
while attempts < 11 :
    print(f'Attempts {attempts} at 10:  ')
    user_number = int(input('Chose a number the 0 a 100: '))
    if user_number < 0 or user_number > 100:
        print('invalid user number')
        continue
    if user_number == chosen_number:
        print(" you acert number !!! :)")
        break
    elif user_number < chosen_number: 
        print('User number is low the chosen number')
        print('chosen_number: hing')
        attempts += 1
    elif user_number > chosen_number:
        print('User number is hing the chosen number')
        print('chosen_number: low')
        attempts += 1
    else: 
        print('invalid user number')

print('---Results ---')
print(f'attempts: {attempts}')
if attempts <= 10:
    print(' you win !!!! :) ')
if attempts > 10:
    print(' you Lose !!!! :( ')

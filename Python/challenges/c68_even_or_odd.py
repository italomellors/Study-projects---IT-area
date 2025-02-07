'''
Create a program that plays Even or Odd with the computer.
The game will only be interrupted when the player loses,
displaying the total number of consecutive wins achieved
at the end of the game.
'''
import random

print('---' * 10)
print('Even or Odd')
print('---' * 10)

round_number = 1
system_choice = 0
user_type = ''
system_type = ''
wins = 0
losses = 0
winner = ''

while losses < 3 and wins < 3:
    print(f'Match ({round_number})')
    print('1 - Odd')
    print('2 - Even')
    user_choice = int(input('Choose an option: '))

    if user_choice < 1 or user_choice > 2:
        print('Invalid option! Enter 1 or 2.')
        continue
    elif user_choice == 1:
        user_type = 'Odd'
        system_choice = 2
        system_type = 'Even'
    elif user_choice == 2:
        user_type = 'Even'
        system_choice = 1
        system_type = 'Odd'
    else:
        print("Error! Condition not listed.")
    
    print(f'You chose: {user_type}')
    print(f'The computer chose: {system_type}')

    user_number = int(input('(represents fingers) | Enter a number (0 - 10): '))
    if user_number < 0 or user_number > 10:
        print('Invalid number! Enter a number (0 - 10).')
        continue

    print(f'You chose the number: {user_number}')
    system_number = random.randint(0, 10)
    print(f'The computer chose: {system_number}')

    sum_numbers = user_number + system_number
    print(f'Sum of numbers: {sum_numbers}')

    if sum_numbers % 2 == 1:
        result = 1
        result_type = 'Odd'
    elif sum_numbers % 2 == 0:
        result = 2
        result_type = 'Even'

    if user_choice == result:
        print('Congratulations, you won! :)')
        wins += 1
        winner = 'you'
        print(f'Wins: {wins} | Losses: {losses}')
        round_number += 1
        print('---' * 10)
    else:
        print('Unfortunately, you lost. :(')
        losses += 1
        winner = 'computer'
        print(f'Wins: {wins} | Losses: {losses}')
        round_number += 1
        print('---' * 10)

print('---' * 10)
print('RESULT')
print(f'The winner was: {winner}')
print(f'Wins: {wins} | Losses: {losses}')
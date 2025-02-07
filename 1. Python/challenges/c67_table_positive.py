'''
Create a program that displays the multiplication table of several numbers,
one at a time, for each value entered by the user.
The program will be interrupted when the requested number is negative.
'''
print('---' * 10)
print('Multiplication Table')
print('---' * 10)
number = 1
while number > 0:
    number = float(input('Enter the number: '))
    if number < 0:
        print('Program interrupted')
        break
    for i in range(1, 10):
        result = i * number
        print(f'{i} X {number} = {result}')
print('End of program')
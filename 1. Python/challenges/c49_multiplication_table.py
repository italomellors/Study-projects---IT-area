'''show the multiplication table of a number
that the user chooses, but now using a for loop'''
print('--- Multiplication Table ---')
number = int(input('Enter a number: '))
print(f'Multiplication table for: {number}')
for n in range(1, 11):
    result = number * n
    print(f'{n} x {number} = {result}')
print('End of multiplication table')
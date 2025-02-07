''' Write a program that reads any number and displays
your factorial 

example: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''
print('-----' * 10)
print('Factorial Number')
print('-----' * 10)

number_user = int(input('digite a number: '))
fatorial = 1
n = number_user

while n > 1:
    fatorial *= n
    n -= 1
print(f'the result of factorial: {number_user} = {fatorial}')

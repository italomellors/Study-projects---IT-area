'''
Create a program that reads several numbers and places them in a list.
After that, show:
a) how many numbers were entered.
b) the list of values, sorted in descending order.
c) whether the number 5 was entered and is or isn't in the list.
'''
'''
Crie um programa que vai ler vários números e colocá-los em uma lista
Depois disso, mostre:
a) quantos números foram digitados.
b) a lista de valores, ordenada de forma decrescente
c) se o valor 5 foi digitado e está ou não na lista.
'''
print('---'*10)
print('registion feature')
print('---'*10)
continue_ = ''
number_list = []
n = 1
while continue_ != 'n':
    print(f'- {n} -')
    number_user = int(input('enter a numbers: '))
    number_list.append(number_user)
    n += 1
    continue_ = input('Continue? [S | N]: ')
quantative_number = len(number_list)
number_list.sort(reverse = True)
print(f"Quantative of elements: {quantative_number}")
print(f'Decrese number: {number_list}')
if 5 in number_list:
    print('number 5 in list')
else:
    print("don't have number 5")
'''
Create a program that reads several numbers and stores them in a list.
After that, create two extra lists that will contain only the even
and odd values, respectively.

In the end, show the contents of the three generated lists.
'''
'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente.

Ao final, mostre o conteúdo das três listas geradas.
'''
print('---'*10)
print('three list')
print('---'*10)
c = 1
continue_ =''
list_number = []
even_number = []
odd_number = []
while continue_ != 'n':
    number_list = int(input('Enter a number: '))
    list_number.append(number_list)
    if number_list % 2 == 0:
        even_number.append(number_list)
    elif number_list % 2 == 1: 
        odd_number.append(number_list)
    continue_ = input('Continue? [S | N] :')
print('---'*10)
print('RESULTS')
print(f'list number: {sorted(list_number)}')
print(f'even number: {sorted(even_number)}')
print(f'Odd number: {sorted(odd_number)}')
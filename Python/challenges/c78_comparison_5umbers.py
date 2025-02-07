'''
Make a program that reads 5 numerical values and stores them in a list.
In the end, display the highest and lowest values entered
and their respective positions in the list.
'''
'''
Faça um programa que leia 5 valores números e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitados
e as suas respectivas posições na lista.
'''
print('---'*10)
print('Comparision_5numbers')
print('---'*10)
numbers_5 = []
c = 1
for i in range(0,5):
    print(f'list - {c}')
    number_user = int(input('1. Digite a number: '))
    numbers_5.append(number_user)
    c += 1
    print(f'five numbers: {numbers_5} ')
    numbers_5.sort()
    print(f'Order number: {numbers_5}')
    print(f'Higgest: {numbers_5[-1]}')
    print(f'Lowest: {numbers_5[0]}')
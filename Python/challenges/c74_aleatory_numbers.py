'''
Crie um programa que vai gerar cinco números aleatórios 
e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados
e também indice o menor e o maior valor que estão na tupla
'''
print('---'*10)
print('Aleatory Number')
print('---'*10)
import random

highest = 0
lowest = 1000000 # infinity
aleatory_numbers = ()  # Inicializando uma tupla vazia

for i in range(5):
    number_aleatory = random.randint(0, 10)
    aleatory_numbers += (number_aleatory,)  # coloque (,) Adiciona cada número gerado à tupla
    print(f'{number_aleatory}, ', end='',)  
   

    if highest < number_aleatory:
        highest = number_aleatory
    if lowest > number_aleatory:
        lowest = number_aleatory

order_numbers = tuple(sorted(aleatory_numbers))
print(f'\n Ordem dos numeros: {order_numbers} ')
print(f'\nHighest number: {highest} | Lowest number: {lowest}')
print(f'{max(aleatory_numbers)} | {min(aleatory_numbers)}')
print(f'Aleatory numbers tuple: {aleatory_numbers}')

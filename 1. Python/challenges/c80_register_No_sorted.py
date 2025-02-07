'''
Create a program where the user can enter five numerical values
and register them in a list, already in the correct insertion position
(without using sort()).

In the end, display the sorted list on the screen.
'''
'''
Crie um programa onde o usuário possa digitar cinco valores numéricos
e cadastre-os em uma lista, já na posição correta de inserção
(sem usar o sort()).

No final, mostre a lista ordenada na tela.
'''
print('---'*10)
print('Register number no sorted')
print('---'*10)
c = 1
n = 0
continue_ = ''
number_list = []
while c < 6:
    print(f'{c} of 5:')
    try:
        number_user = int(input('Enter a number: '))
        number_list.append(number_user)
        c += 1
    except ValueError:
        print("Please enter a valid integer.")
        print(f'Number list: {number_list}')
max_value = max(number_list)  # Encontra o maior valor
number_list.remove(max_value)  # Remove o maior valor da posição original
number_list.append(max_value)  # Adiciona o maior valor ao final

print(f'List order with the max at the end: {number_list}')



    



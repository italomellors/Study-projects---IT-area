'''
Create a program where the user can enter several numerical values
and store them in a list.

If the number already exists in the list, it will not be added.
At the end, all unique values entered will be displayed in ascending order.
'''
'''
Crie um programa onde o usuário possa digitar vários valores numéricos
e cadastre-os em uma lista.

Caso o número já exista lá dentro, ele não será adicionado.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''
print('---'*10)
print('Only different Numbers ')
print('---'*10)
continue_ = ''
number_list = []
n = 1
while continue_ != 'n':
    print(f'- {n} -')
    number_user = input('enter different numbers: ')
    if number_user not in number_list:
        number_list.append(number_user)
    number_list.sort()
    print(f'Number list order: {number_list} ')
    n += 1 
    continue_ = input(' continue ? [s | n]: ')
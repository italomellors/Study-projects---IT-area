'''
Desenvolva um programa que leia quatro valores pelo teclado
e guarde-os em uma tupla.
No final, mostre:

a) quantas vezes apareceu o valor 9
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares
'''
print('---' * 10)
print('Identification Tuple')
print('---' * 10)

tuple_numbers = ()
quantitative_even = ()
count = 1

while count <= 4:  # Mantendo a lógica original
    print(f'{count} - Tuple Input -')
    try:
        number_user = int(input('Digite um número: '))
    except ValueError:
        print("Por favor, insira um número válido.")
        continue

    tuple_numbers += (number_user,)
    print(f'Números na tupla até agora: {tuple_numbers}')
    count += 1

    if number_user % 2 == 0:
        quantitative_even += (number_user,)

print(f'A tupla final é: {tuple_numbers}')
print(f'Quantidade de vezes que o número 9 aparece: {tuple_numbers.count(9)}')

# Evitar erro se o número 3 não estiver na tupla
if 3 in tuple_numbers:
    print(f'Índice da primeira ocorrência do número 3: {tuple_numbers.index(3)}')
else:
    print('O número 3 não está presente na tupla.')

print(f'Números pares na tupla: {quantitative_even}')








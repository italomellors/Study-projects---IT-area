'''
Crie um programa que tenha uma tupla totalmente preenchida
com uma contagem por extenso de zero até vinte

Seu programa deverá ler um número pelo teclado
(entre 0 e 20)
e mostrá-lo por extenso'''
print('---'*10)
print('Extend number')
print('---'*10)

numbers = (1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20)
number_name = ('one', 'two', 'three','four','five', \
               'six', 'seven', 'eigth', 'nine', 'ten', \
               'eleven', 'twelve', 'Thirteen', 'fourteen', 'fiveteen', \
               'sixteen', 'seventeen', 'eighteen','nineteen', 'twenty')

while True:
    try:
        number_user = int(input('Digite a number (0 - 20): '))
        if number_user < 0 and number_user >= 20:
            print('ivalid number ! try again')
            continue
        break
    except ValueError:
        print('inavalid comand ! plese insert correct value')
print(f'Number choise:{number_user} | Exentend number: {number_name[number_user - 1]} ')
    
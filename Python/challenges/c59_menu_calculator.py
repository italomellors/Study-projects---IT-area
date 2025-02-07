''' Create a program that reads two values and displays a menu
on screen:

1: add
2: multiply
3: biggest
4: new numbers
5: exit the program

Your program must perform the requested operation in each case '''
choise_user = 0
new_number = 0
print('-----' * 10)
print('Menu calculator')
print('-----' * 10)
while choise_user != 5 :
    try:
        number_1 = float(input('Digite the fist number: '))
        number_2 = float(input('Digite the second number: ')) 
        print('1: add')
        print('2: multiply')
        print('3: biggest')
        print('4: new numbers')
        print('5: exit the program')
        choise_user = int(input('Choise one option: '))
        if choise_user < 1 or choise_user > 5:
            print('Erro imput a valid number ! (1 - 5)')
            continue
    except ValueError:
        print('Erro imput a valid number ! (1 - 5)')
        continue
    if choise_user == 1:
        add = number_1 + number_2
        print(f'Add the numbers: {add} ')
        print('-----' * 10)
    elif choise_user == 2:
        multiply = number_1 * number_2
        print(f'multiply the numbers: {multiply} ')
        print('-----' * 10)
    elif choise_user == 3:
        if number_1 == number_2:
            print('Same value')
        elif number_1 > number_2:
            biggest = number_1
            print(f'the biggest number: {biggest}')
            print('-----' * 10)
        elif number_1 < number_2:
            biggest = number_2
            print(f'the biggest number: {biggest}')
            print('-----' * 10)
    elif choise_user == 4:
        #number_1 = float(input('Digite the fist number: '))
        #number_2 = float(input('Digite the second number: ')) 
        print('-----' * 10)
        print('the new numbers: ')
        continue
    elif choise_user == 5:
        print( 'Close the program')
        print('-----' * 10)
    else:
        print('Erro no conditions list')




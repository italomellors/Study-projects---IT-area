''' Write a program that reads any integer
and ask the user to choose what the conversion basis will be:
1 for binary
2 for octal
3 for hexadecimal
'''
print('-----' * 10)
print('CONVERSION BASES')
print('-----' * 10)
# Instructions
print(' Covert base (10) to:  ')
print('1 - for binary ')
print('2 - for octal ')
print('3 - for hexadecimal ')

# correct input
while True:
    try:
        conversion_type = int(input('Choose the type of conversion 1, 2, or 3: '))
        if conversion_type < 1 or conversion_type > 3:
            print('Invalid command! Please insert a valid number 1, 2, or 3.\n')
            continue
        number_base10 = float(input('Insert the number ,base 10, to convert: '))  
    except ValueError:
        print('Wrong value! Please enter a valid integer.\n')
# conversion types
    if conversion_type == 1 : 
        print('1 - for binary ')
        break
    elif conversion_type == 2:
        print('2 - for octal ')
        break
    elif conversion_type == 3 :
        print('3 - for hexadecimal ')
        break
#continue
   


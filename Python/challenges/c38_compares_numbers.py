'''
Write a program that reads two integers and compares them,
showing a message on the screen:
- the first value is greater
- the second value is higher
- there is no greater value; both are the same
'''
print('-----' * 10)
print('COMPARES NUMBERS')
print('-----' * 10)

# correct input
while True:
    try:
        number_1 = float(input("digite first number : "))
        number_2 = float(input("digite second number: "))
        number_3 = float(input("digite third number: "))
         
    except ValueError:
        print('Wrong value! Please enter a valid integer.\n')
# comparates 
    if number_1 > number_2 and number_1 > number_3:
        print('the first value is greater')
        break
    elif number_2 > number_1 and number_2 > number_3:
        print('the second value is greater')
        break
    elif number_3 > number_1 and number_3 > number_2:
        print('the third value is greater')
        break

    elif number_1 == number_2 and number_1 > number_3:
        print('the first and second value is greater')
        break
    elif number_2 == number_1 and number_2 > number_3:
        print('the second and third value is greater')
        break
    elif number_3 == number_1 and number_3 > number_2:
        print('the first and third value is greater')
        break

    elif number_1 == number_2 == number_3 :
        print('Every number are same')
        break
  

#Completed
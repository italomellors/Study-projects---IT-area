'''
Create a program that calculates the amount to be paid for a product,
considering its normal price and payment conditions:

- cash/check: 10% discount
- cash on card: 5% discount
- up to 2x on card: normal price
- in 3 installments or more on the card: 20% interest
'''
print('-----' * 10)
print('PAYMENT_CONDITIONS')
print('-----' * 10)
while True:
    try:
        print('1 - cash/check: (10%) discount')
        print('2 - cash on card: (5%) discount')
        print('3 - up to 2x on card: normal price')
        print('4 - in 3 installments or more on the card: (20%) interest \n')
        price = float(input('What is price of product : $ '))
        pay_form = int(input('what is is payment form: '))
    except ValueError:
        print('Erro insert the value number')
    if  pay_form < 1 or pay_form > 4 :
        print('Invalid payment ! plesa insert the valid choose')
        continue
    elif pay_form == 1 :
        print('1 - cash/check: (10%) discount')
        price = price * 0.9
        print(f'price: $ {price}')
        break
    elif pay_form == 2 :
        print('2 - cash on card: (5%) discount')
        price = price * 0.95
        print(f'price: $ {price}')
        break
    elif pay_form == 3 :
        print('3 - up to 2x on card: normal price')
        print(f'price: $ {price}')
        break
    elif pay_form == 4 :
        print('4 - in 3 installments or more on the card: (20%) interest')
        price = price * 1.2
        print(f'price: $ {price}')
        break

#completed




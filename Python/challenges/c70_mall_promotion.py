'''
Create a program that reads the name and price of several products.
The program should ask if the user wants to continue.
At the end, show:
a) the total amount spent
b) how many products cost more than $1000
c) the name of the cheapest product
'''
print('---' * 10)
print('Shopping System')
print('---' * 10)

count = 1
continue_shopping = ' '
total_spent = 0
over_thousand = 0
lowest_price = 1000000  # infinity
cheapest_product = ''

while continue_shopping != 'n':
    print(f'Item: {count}')
    product = input("Product name: ")
    price = float(input('Enter the product price: $ '))
    total_spent += price
    
    if price > 1000:
        over_thousand += 1
    
    if lowest_price > price:
        lowest_price = price
        cheapest_product = product
    
    print('---' * 10)
    print(f'Results ({count})')
    print(f'A) Total spent: {total_spent}')
    print(f'B) Products costing more than $1000: {over_thousand}')
    print(f'C) Cheapest product: {cheapest_product}')
    continue_shopping = input('Do you want to continue? [S / N]: ')
    count += 1
    print('---' * 10)
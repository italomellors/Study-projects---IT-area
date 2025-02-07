'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''
'''
Crie um programa que tenha uma tupla única
com nomes de produtos e seus respectivos precos,
na sequência

No final, mostre uma listagem de precos,
organizando os dados em forma tabular
'''

listagem = (
    "pão", 1,
    "leite", 3.50,
    "frango", 10.90
      )

print("=" * 35)
print("Listagem de  precos.")
print("=" * 35)

for pos in range(0,len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end= '')
    else:
        print(f'R$ {listagem[pos]:.>10}')
'''
print('---'*10)
print('Store List')
print('---'*10)
continue_ = ''
name_list = ()
price_list = ()
item = 1
while continue_ != 'n':
    try:
        print(f'item: {item} ')
        product_name = str(input('Digite the name of product: '))
        product_price = float(input('digite price of product: $ '))
    except ValueError:
        print('invalid value ! ')
        continue

    name_list += (product_name,)
    price_list += (product_price,)

    print(f'product: {product_name} --------- price: $ {product_price}')
    item += 1
    continue_ = input('do you wnat continue ? [S / N] ')
print('---'*10)
print('STORE LIST')
for i in range( len(name_list)):
    print(f'product: {name_list[i]} --------- price: $ {price_list[i]}')
print('---'*10)
'''

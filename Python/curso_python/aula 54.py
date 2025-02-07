""" Faça uma lista de compras com listas
O usuario deve ter a posssibilidade de 
inserir,apagar e listar valores na sua lista
não permita que o programa quebre com erros de 
indices inexistentes na lista """
print('----' * 10)
print(' LISTA DE COMPRAS')
print('----' * 10)
digito = input('Digite a ação [i]nserir | [a]pagar | [l]istar | [s]air: ').lower()
digito_certo = ['a','i','l']
lista_compras = []
tamanho_lista = enumerate(lista_compras) 
# inserir
while digito != 's' :
    #inserir
    if digito == 'i' :
        item = input('Digite o item: ')
        lista_compras.append(item)
        print(lista_compras)
    # Apagar 
    elif digito == 'a' :
        print('Apagar item')
    # Listar 
    elif digito == 'l': 
        print('Lista de Itens: ')
        for i, item in enumerate(lista_compras, start=1):
            print(f"{i}. {item}")
    else: 
        print('Digito invalido Tente novamente: ')
    #entrada   
    digito = input('Digite a ação [i]nserir | [a]pagar | [l]istar | [s]air: ').lower()








 


'''
lanche = ['hamburguer','suco','pizza','picole'] # declarar a lista []
lanche.append('cookie') # soma um elemento ao final da lista
lanche.insert(0,'salgado') # posiciona elemento no final da lista
del lanche[3] # deleta elemento da lista | reposiciona a contagem
lanche.pop(3) # remove o elemento
lanche.remove('pizza') # deleta apartir do valor
if 'pizza' in lanche:
    lanche.remove('pizza')
valores = list(range(4,11))
valores.sort(reverse= True)
len(valores)
print(lanche)
'''
'''
print('---'*10)
num = [2, 5, 9, 1]
num[2] = 3
num.append(7)
num.sort(reverse= True)
num.insert(2,0)
num.pop(2)
if 4 in num:
    num.remove(5)
num.remove(2)
print(num)
print(f'Essa lista em 5 elementos: {num}')
print('---'*10)
valores = []
valores.append(5)
valores.append(9)
valores.append(4)
for v in valores:
    print(f'{v}...',end='')
for i,v in enumerate(valores):
    print(f'{v}',end='-')
print('cheguei no final da lista')
print('---'*10)
valores = list()
for cont in range(0,5):
    valores.append(int(input('Digite um valor: ')))
'''
a = [2,3,4,7]
# b = a Une as lista
b = a[:] # copia alista de maneira diferente
b[2] = 8
print(f'lista A: {a}')

print(f'lista B: {b}')
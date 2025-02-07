'''lanche = ('hamburguer','suco','pizza','pudim')
for comida in lanche:
    print(f'eu vou comer: {comida}')
    quantidade = len(lanche)
print(f'Nossa comi pra caramba ! {quantidade} coisas')
for cont in range (0, len(lanche)):
    print(f'elementos: {lanche}')
for pos,comida in enumerate(lanche):
    print(f'Eu vou comer a {comida} na posisção {pos}')
TUPLA SÃO IMUTÁVEIS
print(sorted(lanche))'''
a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) # exibe o numero
print(len(c)) # quantidade de elementos 
print(c.count(5)) # quantas vezes o elemento repete
print(c.index(8, 1)) # em que posição esta o elemnto
pessoa = ('italo', 29, 95.3) #  permite diversas classes
tupla = (5, 9, 2, 3, 7)

# Ordem crescente
ordenada_crescente = tuple(sorted(tupla))
print(f"Ordem crescente: {ordenada_crescente}")

# Ordem decrescente
ordenada_decrescente = tuple(sorted(tupla, reverse=True))
print(f"Ordem decrescente: {ordenada_decrescente}")
print(pessoa)
#  del (pessoa)
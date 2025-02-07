'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''
'''
Crie um programa que tenha uma tupla com várias palavras
(não usar acentos).
Depois disso, você deve mostrar, para cada palavra,
quais são as suas vogais
'''

tupla = (
    "Galadriel", "Luthien Tinuviel", "Erik Killmonger", 
    "Kendrick Lamar", "Charlotte Galves", "Roberta Pires", "Amanda"
    )

vogais = ["a", "e", "i", "o", "u"]

for nome in tupla:
    nome = str(nome).lower()
    lista = []

    for letra in nome:
        for i in vogais:
            if letra == i:
                lista.append(letra)

    print(f"{nome.capitalize()}: {lista} - {len(lista)} vogais")
    del(lista)
"""
vogal = ('a', 'e', 'i', 'o', 'u')
palavra = input('Digite a palavra: ')
tamanho_palavra = len(palavra)
resultado = []

for letra in palavra:
    if letra.lower() in vogal:
        resultado.append(letra)

print(f'Vogais na palavra: {resultado}')
"""

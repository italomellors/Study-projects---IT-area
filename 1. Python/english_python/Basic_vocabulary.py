'''
Claro! Aqui estão palavras mais simples:  

### Inglês - Português  
1. **Cat** – Gato  
2. **Dog** – Cachorro  
3. **House** – Casa  
4. **Sun** – Sol  
5. **Water** – Água  
6. **Book** – Livro  
7. **Car** – Carro  
8. **Tree** – Árvore  
9. **Food** – Comida  
10. **Milk** – Leite  
'''
import random
print('---'*10)
print('Basic vocabulary ')
print('---'*10)
ponts = 0
# lista de palavras em ingles 
ingles = ['cat','dog','house','sun','water',
          'book','car','tree','food','milk']
# lista de palavras em portugues 
portugues = ['gato','cachorro','casa','sol','agua',
             'livro','carro','arvore','comida','milk']
for i in range(0,10):
    # escolhe uma palvra aletória
    chosen_word = random.randint(0, 10)
    print(chosen_word)
    print(f'Qual tradução da palavra: {ingles[chosen_word]} ')
    word = input('Digite a tradução:  ')
    if word == portugues[chosen_word] :
        print('correct !')
        ponts += 1
    else:
        print('errado !')
        print(f'A tradução: {portugues[chosen_word]}')

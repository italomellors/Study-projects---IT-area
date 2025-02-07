import random

# Conjunto de palavras organizadas por temas
themes = {
    "Frutas": ["apple", "banana", "grape", "orange", "strawberry"],
    "Animais": ["dog", "cat", "elephant", "lion", "tiger"],
    "Profissões": ["doctor", "teacher", "engineer", "lawyer", "nurse"],
    "Objetos": ["chair", "table", "backpack", "laptop", "pencil"],
    "Verbos": ["run", "eat", "write", "read", "jump"],
    "Adjetivos": ["happy", "sad", "angry", "beautiful", "strong"],
    "Cores": ["red", "blue", "green", "yellow", "purple"],
    "Partes do corpo": ["head", "arm", "leg", "eye", "ear"],
    "Países": ["Brazil", "Ireland", "Japan", "Canada", "Spain"],
    "Natureza": ["river", "mountain", "tree", "flower", "ocean"]
}

# Lista correspondente em português
themes_pt = {
    "Frutas": ["maçã", "banana", "uva", "laranja", "morango"],
    "Animais": ["cachorro", "gato", "elefante", "leão", "tigre"],
    "Profissões": ["médico", "professor", "engenheiro", "advogado", "enfermeiro"],
    "Objetos": ["cadeira", "mesa", "mochila", "notebook", "lápis"],
    "Verbos": ["correr", "comer", "escrever", "ler", "pular"],
    "Adjetivos": ["feliz", "triste", "irritado", "bonito", "forte"],
    "Cores": ["vermelho", "azul", "verde", "amarelo", "roxo"],
    "Partes do corpo": ["cabeça", "braço", "perna", "olho", "orelha"],
    "Países": ["Brasil", "Irlanda", "Japão", "Canadá", "Espanha"],
    "Natureza": ["rio", "montanha", "árvore", "flor", "oceano"]
}

# Escolha aleatória de 50 palavras
en_words = []
pt_words = []
for key in themes.keys():
    en_words.extend(themes[key])
    pt_words.extend(themes_pt[key])

selected_pairs = random.sample(list(zip(pt_words, en_words)), 50)

# Jogo de perguntas e respostas
score = 0
print("=== JOGO DE VOCABULÁRIO EM INGLÊS ===")
print("Traduza para o inglês a palavra exibida!")

for pt_word, en_word in selected_pairs:
    answer = input(f"Qual é a tradução para '{pt_word}'? ").strip().lower()
    if answer == en_word.lower():
        print("Correto!")
        score += 1
    else:
        print(f"Errado. A resposta correta era '{en_word}'.")

# Avaliação final
print("\n=== RESULTADO FINAL ===")
print(f"Você acertou {score} de 50 palavras.")

if score < 20:
    print("Você precisa estudar mais vocabulário básico.")
elif 20 <= score < 35:
    print("Você está no caminho certo, mas ainda há espaço para melhorar.")
elif 35 <= score < 45:
    print("Você tem um bom vocabulário! Continue praticando.")
else:
    print("Parabéns! Você possui um ótimo vocabulário em inglês.")
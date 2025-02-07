"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
try:
        # Solicita que o usuário digite um número
        numero = int(input("Digite um número inteiro: "))  
        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            print(f"O número {numero} é par.")
        else:
            print(f"O número {numero} é ímpar.")
except ValueError:
        # Trata a exceção caso o usuário não digite um número inteiro
        print("Você não digitou um número inteiro.")


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
hora = input('Que horas são: ')
hora_int = int(hora)
if 0 < hora_int <= 12 : 
      print('Bom dia')
elif 12 < hora_int < 18: 
      print('Boa tarde')
elif 18 <= hora_int <= 24:
      print('Boa noite')
else : 
      print('Hora inexistente')
      

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu nome: ')
letras_nome = len(nome)
print(letras_nome)
if letras_nome < 4 : print("Seu nome é curto")
elif 3 < letras_nome < 6 : print("Seu nome é normal")
elif  6 >= letras_nome : print("Seu nome é grande")
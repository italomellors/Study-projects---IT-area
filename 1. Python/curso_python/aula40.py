while True:
    try:
        # Entrada
        n1 = input('Digite o primeiro número: ')
        n2 = input('Digite o segundo número: ')
        numero_1 = float(n1)
        numero_2 = float(n2)
        resultado = None

        # Operador
        operador = input('Digite o operador: +, -, *, /: ')
        if operador == '+':
            resultado = numero_1 + numero_2
        elif operador == '-':
            resultado = numero_1 - numero_2
        elif operador == '*':
            resultado = numero_1 * numero_2
        elif operador == '/':
            if numero_2 != 0:  # Verifica divisão por zero
                resultado = numero_1 / numero_2
            else:
                print('Erro: Divisão por zero não é permitida.')
        else:
            print('Operador inválido.')

        # Saída do resultado
        if resultado is not None:
            print(f'O resultado é: {resultado}')

    except ValueError:
        print('Erro: Digite números válidos.')

    # Comando de saída
    sair = input('Quer sair? [s]im: ').lower().startswith('s')
    if sair:
        break

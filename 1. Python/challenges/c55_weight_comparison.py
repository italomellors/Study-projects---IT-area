''' Make a program that reads the weight of five people
At the end, show which was the highest and lowest weight read'''
print('Weight Comparison Program')

# Inicialização das variáveis
highest = 0
lowest = float('inf')
sum_weight = 0

# Solicita a quantidade de entradas do usuário
try:
    num_entries = int(input('How many weights do you want to compare? '))
    if num_entries <= 0:
        print('The number of entries must be greater than 0.')
        exit()
except ValueError:
    print('Invalid input. Please enter an integer.')
    exit()

# Loop para coletar e comparar os pesos
for i in range(1, num_entries + 1):
    try:
        user_weight = float(input(f'Enter weight #{i} (KG): '))
        if user_weight <= 0:
            print('Weight must be a positive number.')
            continue
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        continue

    # Atualiza maior, menor e soma dos pesos
    if user_weight > highest:
        highest = user_weight
    if user_weight < lowest:
        lowest = user_weight
    sum_weight += user_weight

# Exibe os resultados
if sum_weight > 0:
    average_weight = sum_weight / num_entries
    print(f'\nResults:')
    print(f'Highest weight: {highest} KG')
    print(f'Lowest weight: {lowest} KG')
    print(f'Average weight: {average_weight:.2f} KG')
else:
    print('No valid weights were entered.')
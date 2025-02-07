'''
Type of triangle will be formed:

- equilateral: all sides equal
- isosceles: two equal sides
- scalene: all different sides
|b - c| < a < b + c
|a - c| < b < a + c
|a - b| < c < a + b
'''
import math
print('-----' * 10)
print('Type of triangle')
print('-----' * 10)

while True:
    try:
        side_a = float(input('Digite the size of Side A: '))
        side_b = float(input('Digite the size of Side B: '))
        side_c = float(input('Digite the size of SIde C: '))
        if side_a >= (side_b + side_c) or \
        side_b >= (side_a + side_c) \
        or side_c >= (side_a + side_b):
            print("Impossible to form a real triangle! Please add new values.")
    except ValueError:
        print('Erro ! insert the valid number')

    print(f'side a: {side_a} ')
    print(f'side a: {side_b} ')
    print(f'side a: {side_c} ')

    if side_a == side_b == side_c :
        print('Type: Equilateral')
        break
    elif ((side_a == side_b) != side_c) or \
    ((side_b == side_c) != side_a) or \
    ((side_c == side_a) != side_b) :
        print('Type: Isosceles')
        break
    elif side_a != side_b != side_c :
        print('Type: Escalene')
        break


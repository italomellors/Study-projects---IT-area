'''
Develop a program that reads six integers
and show the sum only of those that are even
If the value entered is odd, disregard it.'''
sum_even = 0
print('Sum of even numbers')
for n in range(0, 6):
    num = int(input(f'Enter number {n + 1}: '))
    if num % 2 == 0:
        sum_even += num
print(f'The sum of even numbers: {sum_even}')
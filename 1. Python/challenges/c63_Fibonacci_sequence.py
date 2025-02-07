'''
Write a program that reads any integer n
and show on the screen the first n elements and a Fibonacci sequence

1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584 (...)

'''
print('-----' * 10)
print('Fibonacci sequence')
print('-----' * 10)
c = 1
n = int(input('Digite a number of terms: '))
f = 2
print(f'Fibonacci sequence in {n} terms: ')
while c < n :
    f = ((f - 1) + ( f - 2)) * c
    
    c += 1
    n -= 1
#continue

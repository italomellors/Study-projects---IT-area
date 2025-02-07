''' Write a program that reads an integer and tells you whether or not it is
a prime number'''
print("Identifying prime numbers")
divisors = 0
num = int(input("Enter a number: "))
for n in range(1, num +1):
    if num % n == 0:
        print(f'Divisible by {n}')
        divisors += 1
print(f'Divisors: {divisors}')
if divisors <= 2:
    print('PRIME NUMBER')
else:
    print('Not a Prime Number')
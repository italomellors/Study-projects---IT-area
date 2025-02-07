# Write a program that calculates the sum of all odd numbers
# that are multiples of three (3) and that lie in the range of 1 to 500.
# Create a program that calculates the sum of all odd numbers
# that are multiples of three (3) within the range from 1 to 500.
total_sum = 0
for n in range(1, 501):
    if n % 2 == 1 and n % 3 == 0:
        total_sum += n
print(f'The sum of odd numbers that are multiples of 3: {total_sum}')
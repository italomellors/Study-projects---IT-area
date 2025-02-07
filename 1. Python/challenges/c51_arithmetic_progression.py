''' Develop a program that reads the first term and the reason
of a PA (Arithmetic Progression).
At the end, show the first 10 terms of this progression.'''
print('Arithmetic Progression')
# User input
first_term = int(input('Enter the first term: '))
common_difference = int(input('Enter the common difference: '))
# Define the number of terms (in this case, 10 terms)
num_terms = 10
# Generate and display the arithmetic progression
ap = [first_term + (common_difference * i) for i in
range(num_terms)]
print(*ap)
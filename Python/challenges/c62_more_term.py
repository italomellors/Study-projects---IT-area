'''
Improve exercise 61 by asking the user
if he wants to show some more terms
The program ends when it says it wants to show "0 terms"
'''
print('-----' * 10)
print('PA with while')
print('-----' * 10)
first_term = int(input('Digite the first term: '))
razen_terms = int(input('digite the razen of PA: '))
quantitive_terms = int(input('digite of quantitive of terms: '))
range_terms = razen_terms * quantitive_terms
last_term = first_term + range_terms
position_term = first_term
print(f'first_term: {position_term} ')
while position_term < last_term :
    position_term = position_term + razen_terms
    print(f'Position_term: {position_term} ')
print('-----' * 10)
print('RESULT')
print(f"first term: {first_term}")
print(f'razen terms: {razen_terms}')
print(f'range terms: {range_terms}')
print(f'last term: {last_term}')
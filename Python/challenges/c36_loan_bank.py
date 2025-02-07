'''
Write a program to approve bank loan
to buy a house
The program will ask the value of the house, the buyer's salary and in how many
years he will pay

Calculate the amount of the monthly installment,
knowing that it cannot exceed 30% of the salary
or else the loan will be denied
'''
print('-----' * 10)
print('Loan Bank House')
print('-----' * 10)

# Correct input
while True:
    try:
        house_price = float(input('What is the value of the house: $ '))
        salary_current = float(input('What is your salary: $ '))
        long_pay = float(input('How long will you pay (years): '))
        interest_rate = float(input('What is the interest rate (%): '))
        break  
    except ValueError:
        print('Wrong value! Please enter a valid number.\n')
# Calculator
monthly_installment = (house_price / (long_pay * 12 )) * ( 1 + (interest_rate / 100))

# loan status:
if (monthly_installment / salary_current) <= 0.3 : 
    status = ' APPROVED '
else: 
    status = ' DENIED'
# Resultado
print('-----' * 10)
print('RESULT')
print(f'loan status: {status} ')
print(f'monthly installment: $ {monthly_installment:.2f}')
print(f'House price: $ {house_price:.2f}')
print(f'Salary: $ {salary_current:.2f}')
print(f'Time to pay: {long_pay:.0f} years')
print(f'Interest rate: {interest_rate:.2f} % per year')
print('-----' * 10)
#completed
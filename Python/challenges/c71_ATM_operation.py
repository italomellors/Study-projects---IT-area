'''
Create a program that simulates the operation of an ATM.
At the beginning, ask the user how much they want to withdraw (integer)
and the program will inform how many bills of each value will be delivered.
Note: Consider that the ATM has bills of $50, $20, $10, and $1.
'''
#num = int(input("How much do you want to withdraw? \n"))
#bills = [50, 20, 10, 1]

print('---' * 10)
print('ATM Withdrawal')
print('---' * 10)

withdrawal_value = int(input('How much do you want to withdraw? $ '))
total = withdrawal_value
note = 50
total_note = 0

while total > 0:
    if total >= note:
        total -= note
        total_note += 1
    else:
        if total_note > 0:
            print(f'Total of {total_note} notes of ${note}')
        if note == 50:
            note = 20
        elif note == 20:
            note = 10
        elif note == 10:
            note = 1
        total_note = 0

print('Withdrawal completed!')

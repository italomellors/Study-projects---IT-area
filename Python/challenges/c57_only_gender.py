'''
Make a program that reads a person's gender
but only accept the values ​​"M" or "F".
If it's wrong, ask for it to be entered again.
until you have a correct value.
'''
gander = ' '
c = 0
while c < 1:
    gander_user = str(input("digite the gender: (M / F ): "))
    if gander_user == 'm':
        gander = 'male'
        c += 1
    elif gander_user == 'f':
        gander = 'female'
        c += 1
    else:
        print('invalid comand !')
print(f"gender choise: {gander}")



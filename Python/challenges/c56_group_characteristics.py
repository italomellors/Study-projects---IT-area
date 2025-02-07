
''' Develop a program that reads the name, age and gender of 4 people
At the end of the program, show:
 - The average age of the group
 - What is the older man's name
 - How many women are under 20 years old
 '''
print('-----' * 10)
print('Group_comparasion')
print('-----' * 10)
sum_age = 0
hingest = 0
lowest_20 = 0
gander_user = ' '
old_men = ' '
for p in range(0,4) :
    try: 
        # input values 
        name = str(input('Digite se nome: '))
        age_user = float(input('Digite your age: '))
        # avarange age
        sum_age += age_user
        avarange_age = sum_age / 4
        # type of gender
        gander = str(input('Digite the gender (M / F): '))
        if gander == 'm' :
            gander_user = 'male'
            # older man's name
            if hingest < age_user:
                hingest = age_user
                old_men = name
            print(f' - Name: {name}, age user: {age_user} years, gender user: {gander_user}')
            print(f"older man's name: {old_men}")
            print(f'The oldest man age: {hingest} years')
            print(f'average age of the group: {avarange_age}')
        elif gander == 'f':
            gander_user = 'female'
            # women are under 20 years old
            if age_user < 20 :
                lowest_20 += 1
            print(f'- Name: {name}, age user: {age_user} years, gender user: {gander_user}')
            print(f'women are under 20 years old: {lowest_20}')
            print(f'average age of the group: {avarange_age}')
        else:
            print('Insert M / F , invalid comand !')
            continue
    except ValueError:
        print('Ivalid comand ! try again')
        continue
# results
print('-----' * 10)
print('RESULTS')
print(f'average age of the group: {avarange_age}')
print(f"older man's name: {old_men}")
print(f'The oldest man age: {hingest} years')
print(f'women are under 20 years old: {lowest_20}')
print('-----' * 10)


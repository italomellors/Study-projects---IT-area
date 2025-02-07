'''
Create a program that reads two grades from a student and calculates their average,
showing a message at the end, according to the average achieved:

- average below 5.0: failed
- average between 5.0 and 6.9: recovery, provide a retry
- average 7.0 or higher: approved
'''
print('-----' * 10)
print('SCHOOL ASSESSMENT')
print('-----' * 10)

while True:
    try:
        # Solicita as notas das avaliações e verifica se estão no intervalo válido
        assessment_1 = float(input('What is the first assessment (0-10): '))
        if assessment_1 < 0 or assessment_1 > 10:
            print('The score must be between 0 and 10. Try again.\n')
            continue

        assessment_2 = float(input('What is the second assessment (0-10): '))
        if assessment_2 < 0 or assessment_2 > 10:
            print('The score must be between 0 and 10. Try again.\n')
            continue

        # Calcula a média
        rating_average = (assessment_1 + assessment_2) / 2
        print(f'Rating average: {rating_average:.2f}')

        # Verifica os critérios de aprovação
        if rating_average < 5:
            print('REPROVED :|')
            break
        elif 5 <= rating_average < 7:
            print('RECOVERY')
            try:
                # Solicita a nota da recuperação e verifica se está no intervalo válido
                recovery_assessment = float(input('What is the recovery assessment (0-10): '))
                if recovery_assessment < 0 or recovery_assessment > 10:
                    print('The score must be between 0 and 10. Try again.\n')
                    continue

                # Calcula a média final
                finally_average = (rating_average + recovery_assessment) / 2
                print(f'Final average: {finally_average:.2f}')
                if finally_average >= 7:
                    print('APPROVED :)')
                else:
                    print('REPROVED :|')
                break
            except ValueError:
                print('Wrong value! Please enter a valid number.\n')
        elif rating_average >= 7:
            print('APPROVED :)')
            break
    except ValueError:
        print('Wrong value! Please enter a valid number.\n')
#completed
'''
The National Swimming Confederation needs a program that reads
the year of birth of an athlete and show their category, according to age:

	      Ponts_    Age	        Ponts   pratice	    Ponts
Child    |lees 2 |    Less 9	|  1	  | less   2 |      1
Children |	4	 |    9 to 14   |  2	  |    4	 |      2
Junior	 |  6	 |    15 to 19  |  3	  |    6	 |      3
Senior	 |  8	 |    20 to 23  |  4	  |    8	 |      4
Master	 |  10   |    More 23   |  5	  |  more 10 |      5

'''
from datetime import date
print('-----' * 10)
print('Swimming age')
print('-----' * 10)
current_year = 2025
while True: 
    try:
        year_brith = int(input('when is your year of birth: '))
        if year_brith > current_year or year_brith < 1900 :
            print('Date invalid ! isert the valid year')
            continue
        begginer_year = int(input('When you begginer in swimming: '))
        if begginer_year < year_brith :
            print('Date invalid ! isert the valid year')
            continue
    except ValueError:
        print('erro! plese insert the valid comand')
    
    personal_age = current_year - year_brith
    print(f'Pesonal age: {personal_age} years')
    pratice_years = current_year - begginer_year
    print(f'Pratice years: {pratice_years} years')
    ponts = 0
    
    if personal_age <= 9 : ponts += 1 
    elif 9 < personal_age <= 14 : ponts += 2 
    elif 14 < personal_age <= 19 : ponts += 3 
    elif 19 < personal_age <= 23 : ponts += 4 
    elif personal_age > 23 : ponts += 5 
    
    if pratice_years <= 2 : ponts += 1
    elif 2 < pratice_years <= 4 : ponts += 2
    elif 4 < pratice_years <= 6 : ponts += 3
    elif 6 < pratice_years <= 8 : ponts += 4
    elif pratice_years > 8 : ponts += 5

    print(f'ponts: {ponts}')
    if  ponts < 6 :
        print('Category: Child ')
    elif 6 <= ponts < 8 :
        print('Category: Children')
    elif 8 <= ponts < 10 :
        print('Category: Junior')
    elif ponts == 10 :
        print('Category: Master')
        
#complete
   

  








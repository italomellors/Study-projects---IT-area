'''
Crie uma tupla preenchida com os 20 primeiros colocados
da Tabela do Campeonato Brasileiro,
na ordem de colocação.
Depois mostre:
a) apenas os 5 primeiros colocados
b) os últimos 4 colocados da tabela
c) uma lista com os times em ordem alfabética
d) em que posição na tabela está o time da Chapecoense
'''
"""
Tabela Final do Brasileirão Série A 2024

1. Botafogo – 79 pontos
2. Palmeiras – 73 pontos
3. Flamengo – 70 pontos
4. Fortaleza – 68 pontos
5. Internacional – 65 pontos
6. São Paulo – 59 pontos
7. Corinthians – 56 pontos
8. Bahia – 53 pontos
9. Cruzeiro – 52 pontos
10. Vasco da Gama – 50 pontos
11. Vitória – 47 pontos
12. Atlético-MG – 47 pontos
13. Fluminense – 46 pontos
14. Grêmio – 45 pontos
15. Juventude – 45 pontos
16. Bragantino – 44 pontos
17. Athletico-PR – 42 pontos
18. Criciúma – 38 pontos
19. Atlético-GO – 30 pontos
20. Cuiabá – 30 pontos

Rebaixados para a Série B 2025: Athletico-PR, Criciúma, Atlético-GO, Cuiabá.
"""
print('---'*10)
print('championship table')
print('---'*10)

campioship_table = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional', \
 'São Paulo', 'Corinthians', 'Bahia', 'Cruzeiro','Vasco' \
 'Vitória','Atlético-MG','Fluminense','Grêmio','Juventude' \
 'Bragantino', 'Athletico-PR', 'Criciúma', 'Atlético-GO','Cuiabá')
ponts_table = ( 79, 73, 70, 68, 65, 59, 56, 53, 52, 50, \
                47, 47, 46, 45, 45, 44, 42, 38, 30, 30)
a = 'a) apenas os 5 primeiros colocados'
b = 'b) os últimos 4 colocados da tabela'
c = 'c) uma lista com os times em ordem alfabética'
d = 'd) em que posição na tabela está o time do Flamengo'

print(f'{a}: {campioship_table[:6]}')
print(f'{b}: {campioship_table[-4:]}')
alphabetic_campioship = tuple(sorted(campioship_table))
print(f'{c}: {alphabetic_campioship}')
position = campioship_table.index("Flamengo") + 1 
print(f'{d}: {position}')
                
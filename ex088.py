# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
from random import randint

games = []
temp = []

print('-'*30)
print('        JOGA NA MEGA SENA      ')
print('-'*30)

q = int(input('Quantos jogos você quer que eu sortei? '))
tot = 1

while tot <= q:
    cont = 0
    while True:
        num = randint(1, 60)

        if num not in temp:
            temp.append(num)
            cont += 1

            if cont >= 6:
                break

    temp.sort()
    games.append(temp[:])
    temp.clear()
    tot += 1

print(f'=-'*3, f'SORTEANDO {q} JOGOS', '-='*3)
for i, l in enumerate(games):
    print(f'Jogo {i+1}: {l}')

print('-='*5, 'BOA SORTE', '-='*5)




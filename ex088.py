# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
list = list()
games = []
print('-'*30)
print('    JOGA NA MEGA SENA   ')
print('-'*30)
answer = int(input('Quantos jogos você quer que eu sortei?: '))
tot_games = 1
while tot_games <= answer:
    cont = 0
    while True:
        num = randint(1, 60)
        if num not in list:
            list.append(num)
            cont += 1
        if cont >= 6:
            break

    list.sort()
    games.append(list[:])
    list.clear()
    tot_games += 1
    print(f'Os números sorteados foram {games}')
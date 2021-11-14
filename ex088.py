# Faça um programa que ajude um jogador da MEGA SENA a criar palpites. O programa vai perguntar quantos jogos serão
# gerados e vai sortear 6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
from time import sleep

list = []
games = []
print('-'*30)
print('        JOGA NA MEGA SENA      ')
print('-'*30)

# User input
q = int(input('Quantos jogos você quer que eu sorteie?: '))
tot = 1
# Initializing the master loop with "tot" variable
while tot <= q:
    cont = 0
    # Numbers random validation loop
    while True:
        num = randint(1, 60)
        # If the number will be new in the list, 'cause it don't exist in the list, we'll index it
        if num not in list:
            list.append(num)
            cont += 1
            # The numbers that were drawn must be 6
            if cont >= 6:
                break
    # Organize in order
    list.sort()
    # Adding a copy of "list" variable in the master list "games"
    games.append(list[:])
    # Clear the copy of "list" variable in the time of it was index in "games" variable
    list.clear()
    # Stop the loop with this variable cont
    tot += 1

print(f'=-'*3, f'SORTEANDO {q} JOGOS', '-='*3)
for i, l in enumerate(games):
    print(f'Jogo {i+1}: {l}')
    sleep(0.5)
print('-='*5, '<BOA SORTE>','-='*5)
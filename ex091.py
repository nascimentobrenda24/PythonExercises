# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep

game = {}

print('Valores Sorteados: ')
for p in range(0, 4):
    dado = randint(1, 10)

    game = {f"Jogador{p+1}": dado}


    for k, v in game.items():
        sleep(1)
        print(f'{k} tirou {v} no dado')





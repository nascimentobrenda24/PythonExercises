# Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um
# dicionário em Python. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.

from random import randint
from time import sleep
from operator import itemgetter

print('Valores Sorteados: ')
game = {"Jogador 1": randint(1, 10),
        "Jogador 2": randint(1, 10),
        "Jogador 3": randint(1, 10),
        "Jogador 4": randint(1, 10)
        }
ranking = []
# Sweeping the keys and values (players and the randomizing)
for k, v in game.items():
    print(f'{k} tirou {v} no dado.')
    sleep(1)
# Organizing the "game" dict in a reversed list
ranking = sorted(game.items(), key=itemgetter(1), reverse=True)

print('-='*30)
# Ranking the players
print('===RANKING DOS JOGADORES===')
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)


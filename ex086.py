# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.
# **Matrix whose have 3 lines and 3 columns
from time import sleep

# Each columns will have 3 lines
matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# Sweeping each lines and after columns
for l in range(0, 3):
    for c in range(0, 3):
        # Adding values of the users in "matrix" varible, but in "l" variable time
        matrix[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
print('A matriz será gerada em alguns segundos...')
sleep(3)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()


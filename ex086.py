# Crie um programa que declare uma matriz de dimensão 3×3 e preencha com valores lidos pelo teclado. No final,
# mostre a matriz na tela, com a formatação correta.

matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]

# Sweeping each lines and, after, columns along of the matrix. In the final, we may computed values for each positions
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))

# Showing the matrix
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()



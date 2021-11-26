# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados.
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.
from time import sleep
tot_sum_pairs = three_collum_sum = bigger_value = 0

# Creating the matrix
matrix = [[0, 0, 0],
          [0, 0, 0],
          [0, 0, 0]]
# Feeding the values entered by the user into the matrix
for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para  posição [{l},{c}]: '))
        # Looking for even pairs values to add them
        if matrix[l][c] % 2 == 0:
            tot_sum_pairs += matrix[l][c]

print('\nAguarde alguns segundos...')
sleep(2)
print('A matriz gerada foi:\n')

# Showing the matrix
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()
# Adding the values from the third column
for l in range(0, 3):
    three_collum_sum += matrix[l][2]
# The biggest of the second line
for c in range(0, 3):
    if c == 0 or matrix[1][c] > bigger_value:
        bigger_value = matrix[1][c]


print()
print('-='*20)
print(f'A soma de todos os valores pares desta matriz equivale a {tot_sum_pairs}')
print(f'A soma dos valores da terceira coluna resultam no valor {three_collum_sum}')
print(f'O maior valor da segunda linha é o {bigger_value}')
input()
input()


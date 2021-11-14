# Aprimore o desafio anterior, mostrando no final:
# A) A soma de todos os valores pares digitados. CHECK
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

tot_sum = 0
three_collum_sum = 0
bigger = 0

for l in range(0, 3):
    for c in range(0, 3):
        matrix[l][c] = int(input(f'Digite um valor para a posição [{l}, {c}]: '))
        # Summing every pairs values
        if matrix[l][c] % 2 == 0:
            tot_sum += matrix[l][c]

# Showing the matrix database
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matrix[l][c]:^5}]', end='')
    print()

# Summing every lines of 3 collum
for l in range(0, 3):
    three_collum_sum += matrix[l][2]
# Finding the bigger value
for c in range(0, 3):
    if c == 0 or matrix[1][c] > bigger:
        bigger = matrix[1][c]

print(f'\nA soma de todos os valores pares desta matriz equivale a {tot_sum}')
print(f'\nA soma dos valores da 3ª coluna são: {three_collum_sum}')
print(f'\nO maior valor da segunda linha é o {bigger}')

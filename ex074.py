# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso, mostre a listagem de
# números gerados e também indique o menor e o maior valor que estão na tupla.

# Randomizing numbers with random library and it features
from random import sample, randint
# Basically, we'll randomizing numbers between 0 and 10 five times, giving it in a tuple structure
num = tuple(sample(range(10), 5))
# num = (randint(1, 10), randint(1,10), randint(1, 10), randint(1, 10), randint(1, 10))
print('Os valores sorteados foram:', end=' ')
# Now, it was used "for" to index num elements in a variable c, each time in this looping, then eliminating
# the parentheses in the tuple
for c in num:
    print(f'{c}', end=' ')
print(f'\nMaior valor sorteado: {max(num)}\n'
      f'Menor valor sorteado: {min(num)}')
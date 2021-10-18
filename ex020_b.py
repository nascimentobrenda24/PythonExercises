# Sorteando item listado
import random


cores = {'limpar': '\033[m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'roxo': '\033[1;35m',
         'azul_marinho': '\033[1;36m',
         'vermelho': '\033[1;31m'}



aluno_a = str(input('{}Nome do aluno:'.format(cores['vermelho'])))
aluno_b = str(input('{}Nome do aluno:'.format(cores['azul'])))
aluno_c = str(input('{}Nome do aluno:'.format(cores['amarelo'])))
aluno_d = str(input('{}Nome do aluno:'.format(cores['azul_marinho'])))


classificacao = [aluno_a, aluno_b, aluno_c, aluno_d]

colocacao = random.shuffle(classificacao)

print(f'\033[1;4;32mOs classificados são {classificacao}')

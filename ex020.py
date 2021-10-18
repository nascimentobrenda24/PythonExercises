# Sorteando uma ordem na lista
import random

cores = {'limpar': '\033[m',
         'azul': '\033[1;34m',
         'amarelo': '\033[1;33m',
         'roxo': '\033[1;35m',
         'azul_marinho': '\033[1;36m',
         'vermelho': '\033[1;31m', 'verde': '\033[1;32m'}




aluno_a = str(input('{}Primeiro Aluno:{}'.format(cores['azul'], cores['limpar'] )))
aluno_b = str(input('{}Segundo Aluno:{} '.format(cores['amarelo'], cores['limpar'] )))
aluno_c = str(input('{}Terceiro Aluno:{}'.format(cores['vermelho'], cores['limpar'])))
aluno_d = str(input('\033[1;37mQuarto Aluno:'))


candidatos = [aluno_a, aluno_b, aluno_c, aluno_d]
classificacao = random.choices(candidatos)



print('\033[1;4;32mA classificação no TOP10 é {}\033[m '.format(candidatos))




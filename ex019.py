#Sorteando um item na lista

import random

aluno_a = str(input('Primeiro Aluno:'))
aluno_b = str(input('Segundo Aluno:'))
aluno_c = str(input('Terceiro Aluno:'))
aluno_d = str(input('Quarto Aluno:'))


lista = [aluno_a, aluno_b, aluno_c, aluno_d]
sorteado= random.choice(lista)


print('O aluno(a) que foi SORTEADA(A) foi {}'.format(sorteado))

# Crie um programa que faça o computador jogar Jokenpô com você.
from random import choice
from time import sleep

#Armazenamento de Dados
escolha_do_jogador = str(input('\033[1;4;31;40mSUAS OPÇÕES:'
                               '\n[PEDRA]'
                               '\n[PAPEL]'
                               '\n[TESOURA]'
                               '\nQual é a sua escolha?:')).upper().strip()
jokenpo = ['PEDRA', 'PAPEL', 'TESOURA']
escolha_do_pc = choice(jokenpo)

#Animação
print('\033[1;4;34;40mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!!!')

#Condicionais
print('\033[1;4;33m')
print('=*'*200)
print('VOCÊ ESCOLHEU {}\n        VS\nO PC ESCOLHEU {}\n'.format(escolha_do_jogador, escolha_do_pc))

#Hipotese de EMPATE
if escolha_do_pc == escolha_do_jogador:
    print('EMPATOU!!'.format(escolha_do_jogador, jokenpo))

#QUANDO JOGADOR GANHA
elif escolha_do_jogador == 'PEDRA' and escolha_do_pc == 'TESOURA':
    print('VOCÊ GANHOU!')

elif escolha_do_jogador == 'PAPEL' and escolha_do_pc == 'PEDRA':
    print('VOCÊ GANHOU!')

elif escolha_do_jogador == 'TESOURA' and escolha_do_pc == 'PAPEL':
    print('VOCÊ GANHOU!!')

#SENÃO
else:
    print('VOCÊ PERDEU!!')
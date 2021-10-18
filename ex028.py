#Escreva um programa que faça o computador
# "pensar" em um número inteiro entre 0
# e 5 e peça para o usuário tentar descobrir
# qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o
# usuário venceu ou perdeu.


from random import randint
from emoji import emojize
from time import sleep

#Otimização e interface
print('=*'*20, 'JOGO DA ADIVINHAÇÃO', '=*'*20)
usuário = str(input('Qual seu nome, pequeno gafanhoto?:')).upper().strip()


#Randomizando valores no pc
pc = randint(0, 5)

#Erro do usuário sendo previsto
escolha = int(input('Pensei em um número de 0 a 5, {}\nDuvido tu acertares!\nR='.format(usuário)))

#Analisando
print('ANALISANDO...')

sleep(5)


if escolha > 5:
    print('Número inválido. Tente Novamente!')

#Caso seja tudo normal(0 a 5)
if escolha <= 5 or escolha >= 0:
    print('A escolha do PC foi {}\nA sua escolha foi {}\n\n'.format(pc, escolha))

    #Validando o VENCEDOR
    if pc == escolha:
        print('AH, NÃO!. VOCÊ VENCEU!!!!!')

    else:
        print('HAHAHA. VENCI DE VOCÊ!!!!!!!!!!!!!!!!!!!!!!!!!')


print('FIM.')




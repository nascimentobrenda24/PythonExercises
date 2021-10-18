# Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites
# foram necessários para vencer.

#Importações
from random import randint

#Interface Gráfica
print('\033[1;36;43m =*'*200)
print('                                        JOGO DA ADIVINHAÇÃO\n'
      'REGRAS:EU(SEU PC) PENSAREI EM UM VALOR DE 1 A 10\nVENÇA-ME SE FOR CAPAZ!!')
print('=*'*200, '\033[m')

#Código Fonte

# Váriaveis

tentativas = 0# Nº de tentativas

pc = randint(1, 10)
jogador = int(input('\033[1;4;30mPensei em um valor entre(0,10)...\n\033[1;4;35mTente Adivinhar:'))
tentativas += 1 #Tentivas sendo sumuladas

# Se o jogador acertar de 1ª tentativa
if tentativas == 1 and jogador == pc:

    print('\033[1;36m=*' * 3000)
    print('\033[1;4;34;43mPARABÉNS. VOCÊ ACERTOU DE 1ª!!!')
    print(f'\033[1;4;31;40mA ESCOLHA DO PC FOI {pc}', '\033[1;4;30m\n              VS               '
                                                      f'\n\033[1;4;33mA ESCOLHA DO JOGADOR FOI {jogador}')
    print('\033[1;36m=*' * 3000)

# Se não acertar de primeira
#Laço de Repetição com teste Lógico(while)
while jogador != pc: #enquanto o pc e o jogador diferirem, ele roda um loop de novas chances ao usuário
    # Ajudando o usuário
    if jogador > pc:
        print('\033[1;30mMenos...Tente Novamente')
    else:
        print('\033[1;30mMais...Tente Novamente')
    tentativas += 1 #Tentativas sendo sumuladas
    jogador = int(input('\033[1;4;31mHahahaha. Errou!!\nTente Novamente: ')) #Outra Chance ao usuário


print('\033[1;36m=*'*3000)

# Mostrando o PLACAR
print(f'\033[1;4;30mFINALMENTE CONSEGUIU!!!. DEPOIS DE {tentativas} TENTATIVAS')
print(f'\033[1;4;31;40mA ESCOLHA DO PC FOI {pc}', '\033[1;4;30m\n              VS               '
      f'\n\033[1;4;33mA ESCOLHA DO JOGADOR FOI {jogador}')

print('\033[1;36m=*'*3000)





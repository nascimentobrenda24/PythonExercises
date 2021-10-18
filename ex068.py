# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

print(20 * '\033[1;33m=*', 'JOGO PAR & ÍMPAR', '=*' * 20)

print('\033[1;34m~~' * 20, 'MANUAL DE INSTRUÇÕES DO GAME:', '~~' * 200,

      '\n1º) Impar e Par, aqui, são representados como: \033[1;4;31mI; \033[1;4;33mP \033[1;34m'
      '\n2º) NO EMPATE TODOS GANHAM +0 pts'
      '\n3º) TENHA UM BOM JOGO E DIVIRTA-SE\033[m')

print('\033[1;34m~~' * 200)

# Importações Necessárias
from random import choice, randint
from emoji import emojize

# Variávies de controle de 'while', contabilizadoras e aleatorização.
vitoria = False
vitoria_pc = False
usuario = pc = par_impar_pc = impar = par = 0
escolha_pc = ['P', 'I']  # PAR E IMPAR

# Enquanto a vitória do computador for falsa, rodaremos o loop.
while vitoria_pc == False:
    # Definindo a função do usuário e suas escolhas
    usuario = int(input('\033[1;31;40mESCOLHA UM NÚMERO INTEIRO: '))
    par_impar_user = str(input('\033[1;34;40mAPOSTA EM QUAL?[PAR VS ÍMPAR]:\nR=')).upper()[0]

    # Definindo a função e randomização do PC
    pc = randint(1, 1000)  # Possíveis escolhas do PC
    par_impar_pc = choice(escolha_pc)

    # Verificando vencedor VS perdedor

    # 1ª hipótese: EMPATE. PC = USER.
    if par_impar_user == par_impar_pc:
        print(f'\033[1;4;31mO Usuário escolheu: {par_impar_user} e O PC escolheu: {par_impar_pc}')
        # Se fora empate, os dois recebem 0 pt.
        vitoria += 0
        vitoria_pc += 0

        # PLACAR ATUAL DE EMPATE
        print('\033[1;30;46m')
        print('~' * 200)
        print(f'|       PLACAR ATUAL      |\n'
              f'\n  Vitórias do usuário: {vitoria} \n'
              f'\n          VS                    \n'
              f'\n   Vitórias do PC: {vitoria_pc}      \n\033[m')
        print('~' * 200)

    # Passando dessa verificação
    # (2ª hipótese: JOGO NORMAL)
    else:
        # Somaremos o número escolhido pelo usuário pelo do pc, para sabermos se é: PAR ou ÍMPAR.
        valor_final = usuario + pc

        # Definindo Números Ímpares
        if valor_final % 2 != 0:  # Número Ímpar é definido por seu quosciente não ser exato na divisão por 2.
            impar += 1  # Números ímpares sendo contabilizados(Qualifica se é ímpar, nessa contagem)

            # Classificando quem igualou-se, no palpite, ao Ímpar(PC OU USER).
            # Quando for o user, o programa parabeniza-o e continua nesse loop infinito.
            if par_impar_user == 'I' and impar != 0 and par_impar_pc == 'P':
                print(f'|       USUÁRIO: {usuario} VS PC: {pc} = {valor_final} = ÍMPAR|')
                print(emojize('PARABÉNS, VOCÊ VENCEU, ESCOLHEU ÍMPAR!!!:sweat_smile:\nDA PRÓXIMA TE GANHAREI!!',
                              use_aliases=True))
                vitoria += 1  # contabilizando as quantidades de vitórias do user

                # PLACAR DA VITÓRIA DO USER
                print('\033[1;30;46m')
                print('~' * 200)
                print(f'|       PLACAR ATUAL      |\n'
                      f'\n  Vitórias do usuário: {vitoria} \n'
                      f'\n          VS                    \n'
                      f'\n   Vitórias do PC: {vitoria_pc}      \n\033[m')
                print('~' * 200)


            # Quando for o PC, o programa, como pedido, parará. (break)
            elif par_impar_pc == 'I' and impar != 0 and par_impar_user == 'P':
                print(f'|       USUÁRIO: {usuario} VS PC: {pc} = {valor_final} = ÍMPAR|')
                print(emojize('\nHAHAHAHAHAHA VENCI. ESCOLHI ÍMPAR!!:joy:', use_aliases=True))
                vitoria_pc += 1  # contabilizando as quantidades de vitórias do pc
                break

        # Definindo Números Pares
        if valor_final % 2 == 0:
            par += 1  # Números Pares sendo contabilizados(Qualifica se é Par, nessa contagem)

            # Classificando quem igualou-se, no palpite, ao valor Par(PC OU USER).
            # Quando for o user, o programa parabeniza-o e continua nesse loop infinito.
            if par_impar_user == 'P' and par != 0 and par_impar_user == 'I':
                print(f'|       USUÁRIO: {usuario} VS PC: {pc} = {valor_final} = PAR|')
                print(emojize('PARABÉNS, VOCÊ GANHOU, ESCOLHEU PAR!!:sweat_smile:\nDA PRÓXIMA TE GANHAREI!!',
                              use_aliases=True))
                vitoria += 1  # contabilizando as quantidades de vitórias do usuário

                # PLACAR DA VITÓRIA DO USER
                print('\033[1;30;46m')
                print('~' * 200)
                print(f'|       PLACAR ATUAL      |\n'
                      f'\n  Vitórias do usuário: {vitoria} \n'
                      f'\n          VS                    \n'
                      f'\n   Vitórias do PC: {vitoria_pc}      \n\033[m')
                print('~' * 200)

            # Quando for o PC, o programa, como pedido, parará. (break)
            elif par_impar_pc == 'P' and par != 0 and par_impar_user == 'I':
                print(f'|       USUÁRIO: {usuario} VS PC: {pc} = {valor_final} = PAR|')
                print(emojize('HAHAHA VENCI, ESCOLHI PAR!!:joy:', use_aliases=True))
                vitoria_pc += 1  # contabilizando as quantidades de vitórias do pc
                break

'''# PLACAR FINAL( USUÁRIO VS PC )
print('\033[1;30;46m')
print('~' * 200)
print(f'|       PLACAR FINAL      |\n'
      f'\n  Vitórias do usuário: {vitoria} \n'
      f'\n          VS                    \n'
      f'\n   Vitórias do PC: {vitoria_pc}      \n\033[m')
print('~' * 200)


# Outra solução própria
# Faça um programa para jogar par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Adaptation: The game will stop when user request

from random import randint, choice
from emoji import emojize

victories_user = 0
victories_pc = 0

print('\033[1;30;41m=*'*20, 'BEM VINDOS AO' ' \033[1;30;46mPAIR OR OPP´s GAME\033[1;30;41m', '=*'*20)

while True:

    proceed = str(input('Deseja prosseguir com o jogo? [S/N]')).upper()[0]

    if proceed == 'N':
        print('\033[1;33;40mJOGO FINALIZADO COM SUCESSO')
        break

    else:
        # USER
        user = int(input('\033[1;34;40mEscolha um valor de 0 a 10: '))
        while user > 10:
            print(emojize('\033[1;40;33mOps...Excedeu o valor proposto!!!\nTente Novamente:thumbs_up:'))
            user = int(input('\033[1;34;40mEscolha um valor de 0 a 10: \033[m '))

        user_choice = str(input('PAR OU IMPAR?[P/I]:')).upper()[0]

        print(f'Você escolheu o número {user} e apostou no {user_choice}' if user_choice == 'PAR'
              else f'Você escolheu o número {user} e apostou no {user_choice}MPAR \033[m')

        # PC

        random_pc_numbers = randint(0, 10)
        pc_pair_opp = ['PAR', 'IMPAR']
        random_pair_opp = choice(pc_pair_opp)

        print(f'\033[1;33mO PC escolheu o número {random_pc_numbers} e apostou no {random_pair_opp}  \033[m')

        # Final Number's Winner
        winner = random_pc_numbers + user

        # Final Validation

        #1) Winner
        # 1º case : Sum pair
        if winner % 2 == 0:
            if user_choice == 'P' and random_pair_opp == 'IMPAR':
                print(f'\033[1;30;42m PARABÉNS!! VOCÊ APOSTOU NO PAR E DEU {winner}')
                victories_user += 1

            elif user_choice == 'I' and random_pair_opp == 'PAR':
                print(f'\033[1;30;42mOPS...VOCÊ APOSTOU IMPAR E PERDEU!!!\n O PC APOSTOU PAR E DEU JUSTAMENTE {winner}')
                victories_pc += 1

            else:
                print(f'\033[1;30;42mCOINCIDÊNCIA OU NÃO...HOUVE EMPATE!!!\n VOCÊ APOSTOU {user_choice}AR E O PC TAMBÉM {random_pair_opp} '
                        f'E DEU JUSTAMENTE {winner}'if user_choice == 'P'
                        else f'COINCIDÊNCIA OU NÃO...HOUVE EMPATE!!!\n VOCÊ APOSTOU NO {user_choice}MPAR E O PC TAMBÉM APOSTOU NO {random_pair_opp}'
                        f'E DEU JUSTAMENTE {winner}')
                victories_user += 1
                victories_pc += 1

        # 2 º case : Sum opp
        if winner % 2 != 0:
            if user_choice == 'I' and random_pair_opp == 'PAR':
                    print(f'\033[1;30;42mPARABÉNS!! VOCÊ APOSTOU NO IMPAR E DEU {winner}')
                    victories_user += 1
            elif user_choice == 'P' and random_pair_opp == 'IMPAR':
                    print(f'\033[1;30;42mOPS...VOCÊ APOSTOU PAR E PERDEU!!\n O PC APOSTOU IMPAR E DEU {winner}')
                    victories_pc += 1

            else:
                print(f'\033[1;30;42mCOINCIDÊNCIA OU NÃO...HOUVE EMPATE!!!\n VOCÊ APOSTOU {user_choice}AR E O PC TAMBÉM APOSTOU NO {random_pair_opp} '
                        f'  E DEU JUSTAMENTE {winner}' if user_choice == 'P'
                        else f'COINCIDÊNCIA OU NÃO...HOUVE EMPATE!!!\n VOCÊ APOSTOU {user_choice}MPAR E O PC TAMBÉM APOSTOU NO {random_pair_opp}'
                                f'  E DEU JUSTAMENTE {winner}')
                victories_user += 1
                victories_pc += 1

# Final Score
print('=*'*15, f'PLACAR FINAL', '=*'*15)
print(f'\033[1;36;40m\n\nVOCÊ\033[m : {victories_user} \n\033[1;33;40m VS \n\033[1;35;40mPC\033[m : {victories_pc}')
print('\033[1;33;40m=*'*37)

# Score Validation
if victories_user > victories_pc:
    print('FECHAMOS O PROGRAMA COM VOCÊ SENDO O VENCEDOR!!!\n Parabéns e volte sempre')

elif victories_pc == victories_user:
    print('FECHAMOS O PROGRAMA COM EMPATE!!\nACEITAMOS REVANCHE!!')
else:
    print('FECHAMOS O PROGRAMA COM A VITÓRIA DA MÁQUINA!!\n ACEITAMOS REVANCHE!!')
'''''
# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso
from time import sleep
n1 = float(input('\033[1;4;30mNúmero 1: '))
n2 = float(input('Número 2: '))



while True: #Enquanto verdade ocorrerá esse loop
    menu = str(input('\033[1;30;46m=======================================MENU===========================================\n'
                     '[1]SOMAR\n'
                     '[2]MULTIPLICAR\n'
                     '[3]MAIOR\n'
                     '[4]NOVOS NÚMEROS\n'
                     '[5]SAIR DO PROGRAMA\033[m\nQUAL É SUA ESCOLHA?: '))

    # Condições do menu(Funcionalidades do Menu)
    if menu == '1':
        soma = n1 + n2
        print(f'\033[1;4;31m{n1} + {n2} = {soma}\033[m')

    elif menu == '2':
        m = n1 * n2
        print(f'\033[1;4;31m{n1} X {n2} = {m}\033[m')

    elif menu == '3':
        if n1 < n2:
            print(f'{n2} é o MAIOR VALOR!!')
        else:
            print(f'{n1} é o MAIOR VALOR DIGITADO!!')

    elif menu == '4':
        n1 = float(input('\033[1;4;30mNúmero 1: '))
        n2 = float(input('Número 2: '))


    elif menu == '5':
        print('Finalizando...')
        sleep(3)
        print('\033[1;4;30mPROGRAMA FINALIZADO.')
        exit()#Função para sair

    else:
        print('\033[1;4;31mOpção Inválida. Tente Novamente!!')
# Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso de zero até vinte.
# Seu programa deverá ler um número pelo teclado(entre 0 e 20) e mostrá-lo por extenso

# Tupla dos extensos
extenso = ('zero', 'um', 'dois', 'três', 'quatro',
           'cinco', 'seis', 'sete', 'oito',
           'nove', 'dez', 'onze', 'doze',
           'treze', 'quatorze', 'quinze', 'dezesseis',
           'dezessete', 'dezoito', 'dezenove', 'vinte')

# Uma validação para caso o número não estiver entre 0 e 20, o programa, repita o loop
while True:
    num = int(input('Digite um valor [ 0 a 20 ]: '))

    if 0 <= num <= 20:
        num_exten = extenso[num] # Números extensos aqui são definidos pela posição da tupla definida pelo input do usuário.
        continuar = str(input('Quer continuar? [S/N]:')).upper()[0]

        if continuar == 'N':
            print(f'\n\033[1;36;40mVocê digitou o número {num_exten}\033[m')
            break
        elif continuar == "S":
            print(f'\n\033[1;36;40mVocê digitou o número {num_exten}\033[m')
    else:
        print('Ops, você digitou um número inválido. Tente Novamente', end=' ')


print('\033[1;36;40mPrograma finalizado com sucesso\033[m')


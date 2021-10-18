#Escreva um programa em Python que leia um número inteiro qualquer e peça para o
# usuário escolher qual será a
# base de conversão: 1 para binário, 2 para octal e 3 para hexadecimal.


'''Números Binários são a linguagem de máquina, mas por que não usamos-o. Bem, usamos os sistema decimal(base 10), pois
é mais fácil, já que temos 10 dedos(Sim, esse é motivo).
Ex¹:3785(3mil,7tecentos,8tenta,5)

No fim, como falamos antepostamente 3785 é em base 10 e é equivalente a:
3785:

3x1000 = 3x10³
7 x 100= 7x10²
8 x 10 = 8x10¹
5 x 1 = 5x10°

3785 = 3x10³ + 7x10² + 8x10¹ + 5x10°
mcdu(Notação Posicional- Posição de algarismos tem seus valores dentro de um número)

Ex²: 2004 = 2x10³ + 0x10² + 0x10¹ + 4x10° = 2004.
multiplicamos com a base decimal = 10.
Potências de 0 até onde a 'casa' for.(De trás pra frente)

Mas temos outras bases, nas quais estudaremos, como: Sistema Binário
Temos que fazer uma 'relação' entre a máquina e o ser humano, no qual entende Sistema Decimal(10 digitos).

O sistema binário( redes e máquinas são provenientes das redes elétricas que tem apenas os estados: ligado e desligado, por isso
temos apenas 2 valores no SISTEMA BINÁRIO)

Vamos Contar:
0,1,2,3,4,5,6,7,8,9,10 combinações = 10,11,12,13,14,15,16,17,18,19 combinações 20,21,22,23,24,25,26,27,28,29,30.
até chegar em 999. Ou seja, os valores são combinações dos valores majoritários.

Mas ok, entendi, mas e o binário?
Imagine 4 casas = [][][][]
0,1; lembra que são apenas 2?, mas como fazer combinação?

Binários:
0,1,10,11,100,101,110,111,1000,1001,1010,1011,1100,1101,1110,1111,10000,10001,10010,10011


Vamos até completar as casas do 5.
Mas não tem como fazer de forma mais fácil?. Claro que sim, lembra do exemplo de 2004?. Pois é faremos na mesma perspectiva:


[1][0][1][1] = 1 x 2³  0 x 2²   1 x 2¹     1 x 2°
                1x8 + 0x4 + 1x2 + 1x1
                =11 decimal.

Base binária(como o própio nome diz bi = 2)
Potência de trás pra frente( direita para esquerda = 0 a ...)

'[1][0][0][1] = 1x2³ + 0x2² + 0x2¹ + 1x2º''
                1x8 + 0x4 + 0x2 + 1x1
                8+0+0+1 = 9 decimal.


Coversão de decimal para binário:

binário---------decimal = [1][1][0][1] = 1x2³ + 1x2² + 0x2¹  1x2º = 1x8 + 1x4 + 0x2 + 1x1 = 13 decimal.
*macete = [1][0][0][1][1] = apaga os zeros e soma o resto = 18+2+1= 19 decimal
         16 *8  4*  1 = 2x4,2x3,2x2,2x1,2x0*


decimal -------binário =  13\2= 6(quosciente)/2=3(quosciente)/2=1(quosciente)/2 = 0(quosciente) == Os restos são respectivamentes = 1,0,1,1
                            pegar todos os restos de trás pra frente(1101)binário
*macete = [][][][][] = 13decimal
         16 8 4 2 1 = Tente somar uns valores nos outros pra dar 13 = 16 não dá, logo fica 'apagado', mas 8 e 4 formam 12
                      com mais 1 equivalem-se a 13, assim, dizemos que 8,4,1 estão 'acesos'. Os que estão 'acesos' colocamos
                       1 em suas casas decimais e os que estão 'apagados' colocamos 0 . Logo: [0][1][1][0][1].
                                                                                              16  8  4  2  1'''

#Guardando dados
numero_para_converter = int(input('\033[1;4;31;40mDigite um valor inteiro a ser convertido:'))
numero_convertido = numero_para_converter
#Fiz 2 váriaveis com os mesmos valores, pois ao dividir os números por 2, para converterem-se binários, é possível evidenciar que só 1 variável de mesmo
# valor daria um erro ou ficaria NADA legível

print('=*'*20, 'ESCOLHA UMA DAS BASES A CONVERTER', '=*'*20)
opcoes = str(input('\033[1;4;34m'
                   '\n[1]Binário'
                   '\n[2]OCTAL'
                   '\n[3]HEXADECIMAL'
                   '\nR='))


#Condicionais
#Se for converter para binário
if opcoes == '1':
    bi = bin(numero_para_converter)
    print(f'\033[1;4;36m{numero_para_converter}, em binário, equivale-se a {bi}')

elif opcoes == '2':
    octal = oct(numero_para_converter)
    print(f'\033[1;4;36m {numero_para_converter},em octal, equivale-se a {octal}')

elif opcoes == '3':
    hexa = hex(numero_para_converter)
    print(f'\033[1;4;36m{numero_para_converter}, em hexadecimal, equivale-se a {hexa}')

else:
    print('Valor Digitado é inexistente em nossas opções.\nPor favor, TENTE NOVAMENTE')
    exit()

print('Obrigada por usar nossos serviços. Volte Sempre!')


#Programa sem FUNÇÃO bin,hex,octal. PURA LÓGICA

'''numero_converter = int(input('Digite o número que deseja converter: '))
numero_antigo = numero_converter
base = int(input('Escolha qual a base de conversão você quer usar, 1 para binário, 2 para octal e 3 para hexadecimal: '))

if base == 1:
    numero_convertido = str(numero_converter % 2)
    numero_converter = int(numero_converter / 2)
    while numero_converter > 0:
        numero_convertido = str(numero_converter % 2) + numero_convertido
        numero_converter = int(numero_converter / 2)
    print(f'O número {numero_antigo} em binário é {numero_convertido}')
elif base == 2:
    numero_convertido = str(numero_converter % 8)
    numero_converter = int(numero_converter / 8)
    while numero_converter > 0:
        numero_convertido = str(numero_converter % 8) + numero_convertido
        numero_converter = int(numero_converter / 8)
    print(f'O número {numero_antigo} em octal é {numero_convertido}')


elif base == 3:
    numero_convertido = int(numero_converter % 16)
    if numero_convertido > 9:
        a = 1
        if numero_convertido == 10:
            numero_convertido = 'A'
        if numero_convertido == 11:
            numero_convertido = 'B'
        if numero_convertido == 12:
            numero_convertido = 'C'
        if numero_convertido == 13:
            numero_convertido = 'D'
        if numero_convertido == 14:
            numero_convertido = 'E'
        if numero_convertido == 15:
            numero_convertido = 'F'
    else:
        numero_convertido = str(numero_converter % 16)
    numero_converter = int(numero_converter / 16)
    while numero_converter > 0:
        numero_a_ser_adicionado = int(numero_converter % 16)
        if numero_a_ser_adicionado > 9:
            a = 1
            if numero_a_ser_adicionado == 10:
                numero_a_ser_adicionado = 'A'
            if numero_a_ser_adicionado == 11:
                numero_a_ser_adicionado = 'B'
            if numero_a_ser_adicionado == 12:
                numero_a_ser_adicionado = 'C'
            if numero_a_ser_adicionado == 13:
                numero_a_ser_adicionado = 'D'
            if numero_a_ser_adicionado == 14:
                numero_a_ser_adicionado = 'E'
            if numero_a_ser_adicionado == 15:
                numero_a_ser_adicionado = 'F'
        else:
            numero_a_ser_adicionado = str(numero_converter % 16)
        print(numero_a_ser_adicionado)
        numero_convertido = numero_a_ser_adicionado + numero_convertido
        numero_converter = int(numero_converter / 16)
    print(f'O número {numero_antigo} em hexadecimal é {numero_convertido}')
    else:
        print('Opção inválida')'''
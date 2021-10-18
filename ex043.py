# Exercício Python 043: Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# - IMC abaixo de 18,5: Abaixo do Peso
# - Entre 18,5 e 25: Peso Ideal
# - 25 até 30: Sobrepeso
# - 30 até 40: Obesidade
# - Acima de 40: Obesidade Mórbida

# imc = p/ h²


from math import pow
from time import sleep

nome = str(input('\033[1;4;33;44mNome:'))
peso = float(input('\033[1;4;33;41mSEU PESO:'))
h = float(input('Sua Altura: '))
imc = peso / pow(h, 2)

print('\033[1;4;30m SEU ÍNDICE DE MASSA CORPÓREA FOI {:.2f}'.format(imc))
print('\033[1;4;35;40mANALISANDO DADOS...')
sleep(5)

if imc < 18.5:
    print(f'\033[1;4;34m{nome}, você está ABAIXO DO PESO')

elif imc >= 18.5 and imc <=25:
    print(f'{nome}, parabéns: PESO IDEAL')

elif imc > 25 and imc <=30:
    print(f'{nome}, infelizmente, você está COM SOBREPESO')

elif imc > 30 and imc <=40:
    print(f'{nome}, infelizmente, você está COM OBESIDADE I')

elif imc > 40:
    print(f'{nome}, infelizmente, você está COM OBESIDADE MÓRBIDA')

print('\033[1;4;30mOBRIGADA POR USAR NOSSOS SERVIÇOS. VOLTE SEMPRE!')
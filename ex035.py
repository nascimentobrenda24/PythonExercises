#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se
# elas podem ou não formar um triângulo.

#P.S. NOVA FORMA DE ESCREVER .format = print(f'Olá, Mundo {variavel}')

print('\033[1;4;34m=*'*100, 'Criando um Triângulo ', '=*\033[m'*100)

a = float(input('\033[1;4;31mLado 1:CM'))
b = float(input('Lado 2:CM'))
c = float(input('Lado 3:CM\033[m'))

#se, os seus lados obedeceram à seguinte regra: um de seus lados deve ser maior que o valor absoluto
# (módulo) da diferença dos outros dois lados e menor que a soma dos outros dois
if abs(b - c) < a and a < abs(b + c):#abs() para valores absolutos
    print('\033[1;33mESSAS MEDIDAS FORMAM UM TRIÂNGULO')

else:
    print('ESSAS MEDIDAS NÃO FORMAM UM TRIÂNGULO\033[m')

print('\033[1;4;34mObrigada por usar nossos serviços. Volte SEMPRE!\033[m')

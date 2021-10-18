# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.


num = int(input('Digite um valor qualquer:'))

resultado = num % 2 #resultado da divisão

#Todo valor impar dá 1
#Todo valor par dá 0


if resultado == 0:
    print('{} é PAR'.format(num))

else:
    print('{} é Impar'.format(num))
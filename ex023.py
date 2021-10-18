# Separando dígitos de um número
# Faça um programa que leia um número de
# 0 a 9999 e mostre na tela cada
# um dos dígitos separados.

# 1 Maneira

'''num = str(input('Informe um número:'))
print('Analisando o número...')

#unidade,dezena,centena. Usei o fatiamento de strings
u = num[0:1] #De 0 a primeira casa decimal
d = num[1:2] #Da primeira a segunda
c = num[2:3] #Da segunda a terceira
m = num[3:4] #Da terceira a quarta


print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))'''

#2 Maneira(Forma Matemática)

num = int(input('Informe um número:'))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Analisando o número {}...'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))


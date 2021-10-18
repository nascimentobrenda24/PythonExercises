# Faça um programa que leia algo e diga
# seu tipo primitivo e diga todas as informações
# possíveis dele do .is
num = input('Digite algo:')

print('='*40)

print('O tipo primitivo do valor {} é {}'.format(num, type(num)))#vamos mandar o pc mostra o tipo primitivo
print('*'*10)

print('({}) é um número?    {}'.format(num, num.isnumeric()))
print('*'*10)

print('({}) é uma palavra?   {}'.format(num, num.isalpha()))
print('*'*10)

print('({}) está totalmente em maiúsculo? {}'.format(num, num.isupper()))
print('*'*10)

print('({}) está totalmente em minúsculo?  {}'.format(num, num.islower()))



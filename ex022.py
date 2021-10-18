# Analisador de textos
#  Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).

print('=*'*20, 'CADASTRO', '=*'*20)

nome = str(input('Nome Completo:')).strip()#Para ler com letras maiúsculas
print('Analisando seu nome...')

print('Seu nome em minúsculo é   {}'.format(nome.lower()))
print('Seu nome em MAIÚSCULO é   {}'.format(nome.upper()))
print('Seu nome tem ano todo {} letras'.format(len(nome)-nome.count(' ')))#menos o contador de espaços

primeiro_nome = nome.split() #Vai quebrar os caracteres

print('Seu primeiro nome tem {} letras'.format(len(primeiro_nome[0])))



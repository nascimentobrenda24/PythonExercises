#Desenvolva um programa que
# pergunte a distância de uma
# viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de
# até 200Km e R$0,45 parta viagens mais longas.


import time
from emoji import emojize
#Cadastro
print('=*'*20, 'ALUGUEL DE CARROS', '=*'*20)
nome = str(input('Nome Completo:')).split()
km = float(input('Quantos Km tu rodarás?:KM'))


print('Analisando...')
time.sleep(5)

#Condicionais
preco = km * 0.50 if km <= 200 else km * 0.45
print('{} {}, o preço que você vai pagar é de: R${:.2f}'.format(nome[0:1], nome[len(nome)-1], preco))#if simplificado, if in line
# ou operador ternário
print(emojize('\nObrigada por usar nossos serviços. Volte Sempre!:wink:', use_aliases=True))







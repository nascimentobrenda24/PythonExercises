#Faça um programa que leia o nome completo de
# uma pessoa, mostrando em seguida o
# primeiro e o último nome separadamente.

nome = str(input('Nome Completo:')).upper().strip().split()

print('Olá, prazer em conhecer você\nSeu primeiro nome é {} e Seu último nome é {}'.format(nome[:1], nome[len(nome)-1]))
#nome da caixa splitada de 0 a 1 = primeiro nome. Momento de len no nome - 1 'casa', já que começa com 0 a contagem do Py

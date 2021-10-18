# Faça um programa que leia uma
# frase pelo teclado e mostre quantas
# vezes aparece a letra "A", em que posição
# ela aparece a primeira vez e em que posição
# ela aparece a última vez.

frase = str(input('Digite uma frase:')).upper().strip()

print('A letra "A" aparece {} vezes na frase'.format(frase.count('A')))

print('A primeira letra "A" aparece na {} posição'.format(frase.find('A') + 1)) #pois a posição sempre é 0, mas como nós lemos a partir de 1, podemos somar +1 para FACILITAR
print('A última letra "A"apareceu na posição {}'.format(frase.rfind('A') + 1))#Procurará o 'A' para o lado direito. -1, pois a posição termina uma casa a mais, já que começa com 0

#  Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
for c in range(2, 51, 2): #faz apenas 25 repetições(começa em 2) e pula de 2 em 2
    #print('\033[1;4;34;40m.', end=' ')
    print('\033[1;4;30;43m', c, end=' ')
print('\n\n\nFIM')

#Lógica de começar com 2 e não 1 acima no for
'''Imagine que você vai pegar 50 sacos de areia de 2 em 2, igual fizemos acima, porém para não fazer o movimento, e se desgastar,
mesmo não o pegando e só se abaixando e fazendo menção de pegar, podemos ir direto nos 25, assi, fazendo, apenas, 25 'forças' e 
desgastando-se menos.'''

# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

#OBS: Os Números Primos são números naturais maiores do que 1 que possuem somente dois divisores, ou seja,
# são divisíveis por 1 e por ele mesmo. 1!= PRIMO.

#Código da 'Interface Gráfica'
print('\033[1;4;35m', '=*'*10, 'NÚMEROS PRIMOS', '=*'*10)

# Código Fonte
#Variáveis
num = int(input('\033[1;4;30mDigite um Número Inteiro:'))
cont = 0 #acumulador

#Laço de Repetição para definirmos a divisibilidade dele 'num' entre 1 a ele mesmo.
for i in range(1, num+1): #Vai de 1 ao número escolhido
    if num % i == 0: #Valida todos os valores de 'i' que o número é divisível e declara-os em azul
        print('\033[1;4;34m')#cor azul CASO SEJA PRIMO
        cont +=1 #contador de vezes que o 'num' foi dividido pelos valores de 1 a ele mesmo, que nesse caso, é 'i' no for.
    else:
        print('\033[1;4;31m')#Senão for PRIMO, receberá a cor VERMELHA
    print(f'{i}', end=' ')

#Condicionais(Analisando se foi dividido 2x ou + para ser validado como PRIMO ou NÃO PRIMO
if cont == 2:
    print(f'\n\n\033[1;4;30mO {num} foi dividido {cont}X\nPor isso ele É PRIMO')

else:
    print(f'\n\033[1;4;31m{num} foi dividido {cont}X\nPor isso NÃO É PRIMO!!')

print('=*'*200)
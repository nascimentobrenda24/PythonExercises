# Maior e Menor
from time import sleep
print('=*'*100)

n1 = int(input('Valor 1:'))
n2 = int(input('Valor 2:'))
n3 = int(input('Valor 3:'))
numeros = [n1, n2, n3] #mixagem dos valores

print('=*'*100)

print('Analisando dados...')
sleep(5)#Espera de 5segundos

#Simplificação
print('O maior valor digitado foi {}'.format(max(numeros)))
print('O menor numero digitado foi {}'.format(min(numeros)))

if n1 == n2 or n2 == n3 or n1 == n3:
    print('{}, {} e {} SÃO IGUAIS'.format(n1, n2, n3))















#Forma extensa
'''#Quando for os maiores valores
if n1 > n2 and n1 > n3:
    print('{} foi o MAIOR VALOR DIGITADO'.format(n1))

if n2 > n1 and n2 > n3:
    print('{} foi o MAIOR VALOR DIGITADO'.format(n2))

if n3 > n1 and n3 > n2:
    print('{} foi o MAIOR VALOR DIGITADO'.format(n3))


#Quando for os menores valores

if n1 < n2 and n1 < n3:
    print('{} foi o MENOR VALOR DIGITADO'.format(n1))

if n2 < n1 and n2 < n3:
    print('{} foi o MENOR VALOR DIGITADO'.format(n2))

if n3 < n1 and n3 < n2:
    print('{} foi o MAIOR VALOR DIGITADO'.format(n3))
    
#Quando for os mesmos valores

if n1 == n2 or n2 == n3 or n1 == n3:
    print('{}, {} e {} SÃO IGUAIS'.format(n1, n2, n3))

print('\n\nThanks to use our service.')

'''
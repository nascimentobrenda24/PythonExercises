# Refaça o DESAFIO 009,mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
'''# Tabuada

print(10*'=*', 'TABUADA', '=*'*10)

#Definindo valores
num = float(input('Número:'))

#TABUADA
print('A tabuada de {} é:'.format(num))
print('=*'*300)
print('{:.0f} x {} = {:.0f}'.format(num,  1, num*1))
print('{:.0f} x {} = {:.0f}'. format(num, 2, num*2))
print('{:.0f} x {} = {:.0f}'. format(num, 3, num*3))
print('{:.0f} x {} = {:.0f}'. format(num, 4, num*4))
print('{:.0f} x {} = {:.0f}'. format(num, 5, num*5))
print('{:.0f} x {} = {:.0f}'. format(num, 6, num*6))
print('{:.0f} x {} = {:.0f}'. format(num, 7, num*7))
print('{:.0f} x {} = {:.0f}'. format(num, 8, num*8))
print('{:.0f} x {} = {:.0f}'. format(num, 9, num*9))
print('{:.0f} x {} = {:.0f}'. format(num, 10, num*10))
print('=*'*300)
'''

#Começa digitando um valor inteiro
n = int(input('\033[1;4;31;40mDigite um valor:'))
print('\033[1;34m=*'*30)
#De 0 a 10, faremos cálculos na variável m e mostra-los 10X com um print
for c in range(0, 10):
    m = n * c #multiplicação é equivalente ao número multiplicado c, variável de controle, vezes, nesse caso, 11.
    print(f'{n}X{c} = {m} ')
print('\033[1;34m=*'*30)

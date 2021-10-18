# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
# n! = n . (n – 1) . (n – 2) . (n – 3)!
#Usando o While
number = int(input('Número:'))
init = number # When this calculus init, the first number to apper in the multiply is the own number
factorial = 1 # This variable was called, because if we want to multiply every successors of the number,
# in way that evebody will be multiplied, we can use the multiply 's neutral element ( 1 ).

while init > 0:
    print(f'{init}', end='')
    print('x'if init > 1 else '=', end='')
    factorial *= init
    init -= 1

print(factorial, end='')
'''
#Usando o FOR
#Variáveis
num = int(input('Digite um valor qualquer:'))
factorial = 1 #O fatorial começa com 1, pois justificará multiplicar os valores da variável de controle c com 1, elemento nulo na multiplicação.
# ( 1 * c = valores de c acabarão por serem multiplicados entre si = FATORIAL)

print(f'Calculando o fatorial...\n {num}! = ', end='')

#Estrutura de Repetição
for c in range(num, 0, -1): #começa no número digitado e vai até 0, pulando de 1 em 1, ou seja, de trás para frente
    print(f'{c}', 'X' if c != 1 else'=', end=' ')# mostrando os valores de c, e, mostre o símbolo de multiplicação 
    # apenas se for diferente de 1, quando acaba, caso contrário mostrará o símbolo de =.
    factorial *= c #( 1 * c = valores de c acabarão por serem multiplicados entre si = FATORIAL)

print(f'{factorial}', end='')
'''
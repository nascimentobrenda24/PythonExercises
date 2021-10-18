#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
#- EQUILÁTERO: todos os lados iguais
#- ISÓSCELES: dois lados iguais, um diferente
#- ESCALENO: todos os lados diferentes


print('\033[1;4;34m=*'*100, 'Criando um Triângulo ', '=*\033[m'*100)

a = float(input('\033[1;4;31mLado 1:CM'))
b = float(input('Lado 2:CM'))
c = float(input('Lado 3:CM\033[m'))

if abs(b - c) < a and a < abs(b + c):#abs() para valores absolutos
    print('\033[1;33mESSAS MEDIDAS FORMAM UM TRIÂNGULO')
    #Validando os TIPOS DE TRIÂNGULO POR MEDIDA(CM)
    if a == b == c:
        print('\033[1;31;45m\nESSE TRIÂNGULO É EQUILÁTERO')
    elif a == b != c or c == a != b:
        print('\nESSE TRIÂNGULO É ISÓCELES')
    elif a != b != c:
        print('\nESSE TRIÂNGULO É ESCALENO')


else:
    print('ESSAS MEDIDAS NÃO FORMAM UM TRIÂNGULO\033[m')




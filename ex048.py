# Faça um programa que calcule a soma entre todos os números que são múltiplos de três e
# que se encontram no intervalo de 1 até 500.

soma = 0 #Acumulador
cont = 0 #Contador

for c in range(1, 501, 2): # 2, pois pulará de 2 em 2 desde o 1(1,3,5)
    if c % 3 == 0: #Se a divisão por 3 = 0, ou seja, múltiplo de 3, mostre só esses valores(3,9,15...)
        soma += c # soma = soma + c
        cont += 1 #Contador conta 0+1 até todos os VALORES MÚLTIPLOS terminarem

print(f'A soma dos {cont} valores digitados é {soma}')

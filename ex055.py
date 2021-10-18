# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso
# lidos.

maior = 0
menor = 0

for pessoa in range(1, 6):
    peso = float(input(f'\033[1;4;34mPeso da {pessoa}ª pessoa:Kg'))

    if pessoa == 1: #Quando estiver ainda no primeiro laço de repetição
        maior = peso
        menor = peso
        #Ele será o menor e o maior, obviamente, já que ele está sendo o primeiro valor digitado

    else: #Quando passar do primeiro laço
        if peso > maior: #Se o peso for maior que o maior peso do primeiro laço, ele será, agora, o MAIOR.
            maior = peso
        if peso < menor:#Se o peso for menor que o menor peso do primeiro laço, ele será, agora, o MENOR
            menor = peso

print(f'O maior peso lido foi de {maior}Kg')
print(f'O menor peso lido foi de {menor}Kg')


#2ª Maneira
'''
pesos = []

for p in range(1, 5):
    peso = float(input(f'{p}º peso: Kg'))
    pesos.append(peso)
    print(f'O maior peso é {max(pesos)}Kg')
    print(f'O menor peso é {min(pesos)}Kg')
'''
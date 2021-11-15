# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

lista = [[], []]

for c in range(0, 7):
    values = int(input(f"Digite o {c+1}º número: "))

    if values % 2:
        lista[0].append(values)
    else:
        lista[1].append(values)

print('-='*30)
lista[0].sort()
lista[1].sort()
print(f'Os valores pares digitados foram: {lista[0]}'if len(lista[0]) > 1 else f'O valor par digitado foi: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}'if len(lista[1]) > 1 else f'O valor ímpar digitado foi: {lista[1]}')

# Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que
# mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

# Declared a list that contain others lists
num = [[], []]

for c in range(1, 8):
    values = int(input(f'Digite o {c}º valor: '))
    # Adding values in your respectives positions
    if values % 2 == 0:
        num[0].append(values)
    else:
        num[1].append(values)

print('-='*30)
num[0].sort()
num[1].sort()
print(f'Os valores pares digitados foram: {num[0]}')
print(f'Os valores ímpares digitados foram: {num[1]}')
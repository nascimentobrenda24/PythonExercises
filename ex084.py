# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

princ = []
temp = []
light = heavy = 0

while True:
    print('='*30)
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso[Kg]: ')))
    # Finding the heavy and lighter
    # In the first loop, the heavy and lighter user will the first data
    if len(princ) == 0:
        heavy = light = temp[1] # princ[1] = weight
    else:
        if temp[1] > heavy:
            heavy = temp[1]
        elif temp[1] < light:
            light = temp[1]

    # Adding the temporary database "temp" in master list "princ"
    princ.append(temp[:]) # [:] for copy the loop currently list
    temp.clear() # cleaning the "temp" list for clear the data in each loop

    proceed = str(input('Quer continuar?[S/N]: '))
    if proceed in 'Nn':
        break

print('='*40)
print(princ)
print(f'Foram cadastradas {len(princ)} pessoas')
print(f'O maior peso digitado foi {heavy} Kg. Peso de', end=' ')
for p in princ:
    if p[1] == heavy:
        print(p[0], end='')
print(f'\nO menor peso digitado foi {light} Kg. Peso de', end=' ')
for p in princ:
    if p[1] == light:
        print(p[0], end='')

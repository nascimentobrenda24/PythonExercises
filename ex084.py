# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

main = []
temp = []
light = heavy = 0

while True:
    print('='*20)
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso[Kg]: ')))

    # When nothing has yet been added to the "main" variable, the heavy and light weight will be the first value of "temp[1]" list
    if len(main) == 0:
        heavy = light = temp[1] #temp[1] = weight
    else:
        if temp[1] > heavy:
            heavy = temp[1]
        elif temp[1] < light:
            light = temp[1]

    # Saving a copy of "temp" list in the "main" list, because, as the name show us, this is the vital list
    main.append(temp[:])
    temp.clear() # clear each loop for don't mix old values with current, along the loop

    # Validating the user permanence in the software
    proceed = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if proceed in 'Nn':
        break

print('=*'*20)

print(f'Ao todo se cadastram {len(main)} pessoas' if len(main) > 1
      else f'Ao todo se cadastrou {len(main)}')

print(f'O maior peso foi de {heavy} Kg. Peso de ', end='')
for p in main:
    if p[1] == heavy:
        print(f'{p[0]}', end='')
print(f'\nE o menor peso foi de {light} kg. Peso de ', end='')
for p in main:
    if p[1] == light:
        print(f'{p[0]}', end='')
print()
print('=*'*20)











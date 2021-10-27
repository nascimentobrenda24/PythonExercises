# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

persons = []
tot_heavy = 0
tot_lightweight = 0
names_heavies = []
names_lights = []
cont = 0

while True:
    print('='*30)
    names = [str(input('Digite seu nome: '))]
    weight = [float(input('Seu peso [Kg]: '))]
    # Adding in the master list
    persons.append(names)
    persons.append(weight)

    cont += 1
    proceed = str(input('Quer continuar? [S/N]: '))

    if proceed in 'Nn':
        break

    # Heavy and light weight
    # In first time, it is the heavy and light weight
    if cont == 0:
        tot_heavy = tot_lightweight = persons[1]
        #persons.append(tot_heavy)
    else:
        # Heavy
        if persons[1] > tot_heavy:
            tot_heavy = weight
            names_heavies = names
            # Adding in the "person" list
            persons.append(tot_heavy)
            persons.append(names_heavies)
        # Light
        elif persons[1] < tot_lightweight:
            tot_lightweight = weight
            names_lights = names
            # Adding in the "person" list
            persons.append(tot_lightweight)
            persons.append(names_lights)



print(f'Foram cadastradas {cont} pessoas')
print(f'O maior peso foi de {tot_heavy} Kg\nO menor peso foi de {tot_lightweight} Kg')



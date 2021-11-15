# Faça um programa que leia 5 valores númericos e guarde-os e uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

# Empty variables to control the loopings
list_num = []
max = 0
min = 0

# First looping to validate the values in "list_num" list
for c in range(0, 5):
    # The "append" method will be useful to add inputs of the users in the composite variable
    list_num.append(int(input(f'Digite um valor para a posição {c}:')))
    # Lowest and highest numbers validations
    if c == 0:
        # In the first looping the max and minor number will be the first value provided
        max = min = list_num[c]
    # In the second looping
    else:
        if list_num[c] > max:
            max = list_num[c]
        if list_num[c] < min:
            min = list_num[c]

# Showing the databases to users
print('='*30)
print(f'Você digitou os valores {list_num}')

print(f'O maior valor digitado foi {max} nas posições ', end='')
# Looping to recognize the positions of the max and min values identifies
for position, value in enumerate(list_num):
    if value == max:
        print(f'{position}...', end='')
print(f'\nE o menor valor digitado foi o {min} nas posições ', end='')
print()
for position, value in enumerate(list_num):
    if value == min:
        print(f'{position}...', end='')
print()

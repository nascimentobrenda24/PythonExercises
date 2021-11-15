# Faça um programa que leia 5 valores númericos e guarde-os e uma lista.
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista

list_num = []
mx = mn = 0

for c in range(0, 5):
    list_num.append(int(input(f'Digite um valor para a posição {c+1}: ')))

    if c == 0:
        mx = mn = list_num[c]
    else:
        if list_num[c] > mx:
            mx = list_num[c]
        if list_num[c] < mn:
            mn = list_num[c]

print('='*50)
print(f'O maior valor digitado foi {mx} na posição ', end='')
for p, v in enumerate(list_num):
    if v == mx:
        print(f'{p}...', end='')
print()

print(f'\nE o menor valor digitado foi {mn} na posição ', end='')
for p, v in enumerate(list_num):
    if v == mn:
        print(f'{p}...', end='')
print()

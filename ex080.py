# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela

list = []

for c in range(0, 5):
    num = int(input(f'\033[1;30;46mDigite um valor para a posição {c+1}:\033[m'))

    if num in list:
        print('\033[1;31mValor duplicado. Não vou adicionar!\033[m')

    elif num not in list:
        if c == 0 or num > list[-1]:
            list.append(num)
            print('\033[1;32mValor adicionado na última posição\033[m')
        else:
            pos = 0
            while pos < len(list):
                if num <= list[pos]:
                    list.insert(pos, num)
                    print(f'\033[1;32mValor adicionado com sucesso na {pos}ª posição')
                    break
                pos += 1

print(f'Sua lista é {list}')

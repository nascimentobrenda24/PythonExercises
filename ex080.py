# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela

list = []

for c in range(0, 5):
    num = int(input('Digite um valor:'))
    if num in list:
        print('Valor duplicado! Não adicionarei')

    elif num not in list:
        if c == 0 or num > list[-1]:
            list.append(num)
            print('Adicionado na última posição com sucesso!')
        else:
            pos = 0
            while pos < len(list):
                if num <= list[pos]:
                    list.insert(pos, num)
                    print(f'Adicionado com sucesso na {pos}ª posição')
                    break
                pos += 1

print(list)
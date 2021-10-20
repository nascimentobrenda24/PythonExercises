# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista, já na posição
# correta de inserção (sem usar o sort()).
# No final, mostre a lista ordenada na tela

values = []
ma = 0
mi = 0


for v in range(0, 5):
    num = int(input('Digite um valor: '))
    # First situation: Duplicate value
    if num not in values:
        values.append(num)
        print('Valor adicionado com sucesso!')
        # In the first looping: minors and max values
        # The logic of this validation is authenticate the "num" variable in list looking to minor and major values
        # in list and rearranging in ascending order them again in list
        if v == 0:
            num = ma = mi

        # When skip to next loop
        else:
            if num > ma:
                ma = num
                #list.insert()
            elif num < mi:
                mi = num
                list.insert(0, num)

    else:
        print('Valor duplicado!. Não vou adicionar...')

print(f'Sua lista é: {list} ', end=' ')
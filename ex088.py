#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
#  conterão apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
#  listas geradas.

list = []
odd = []
pair = []

while True:
    num = int(input('Digite um número: '))
    cont = str(input('Deseja continuar [S/N]: '))
    if num in list:
        print('Valor duplicado! Não vou adicionar...')

    else:
        list.append(num)
        print('Valor adicionado com sucesso!!')
        # Principal situation: Pair or odd
        if num % 2 == 0:
            pair.append(num)
        else:
            odd.append(num)


    if cont in 'Nn':
        break


print(f'Sua lista é {list}')
print(f'Os valores pares são: {pair}'if pair.count(num % 2 == 0) > 1 else f'O valor par é {pair}')
print(f'E os valore ímpares são:{odd}'if odd.count(num % 2 != 0) > 1 else f'O valor ímpar é {odd} ')


#  Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que
#  conterão apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três
#  listas geradas.

list = []
odd = []
pair = []

while True:
    num = int(input('Digite um número: '))

    if num in list:
        print('Valor duplicado! Não vou adicionar...')

    else:
        list.append(num)
        print('Valor adicionado com sucesso!!')
        # Principal situation: Pair or odd


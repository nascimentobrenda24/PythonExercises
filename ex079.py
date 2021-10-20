# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
#já exista lá dentro, ele não será adicionado novamente. No final, serão exibidos todos os valores únicos digitados, em
# ordem crescente.

list = []

while True:
    num = int(input('Digite um valor:'))
    if num not in list:
        list.append(num)
        print('Adicionado com sucesso!')
    else:
        print('Valor duplicado! Não vou adicionar...')
    continuar = str(input('Quer continuar [S/N]: '))
    if continuar in 'Nn':
        break
print(f'Sua lista está completa: {sorted(list)}')

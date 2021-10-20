# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número
#já exista lá dentro, ele não será adicionado novamente. No final, serão exibidos todos os valores únicos digitados, em
# ordem crescente.

list = []

while True:
    # Receiving the inputs of users
    n = int(input('Digite um número: '))
    # First Case: If the value showed from user was in empty list, it will add in this list
    if n not in list:
        list.append(n)
        print('Valor adicionado com sucesso...')

    else:
        print('Valor duplicado...Não vou adicionar!')

    continuar = str(input('Quer continuar? [S/N]: ')).upper()

    if continuar in 'Nn':
        break

print(list)
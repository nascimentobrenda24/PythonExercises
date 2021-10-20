# Crie um programa que vai ler vários números e colocar em uma lista.
# Depois disso, mostre: Quantos números foram digitados; A lista de valores, ordenada de forma decrescente; Se o valor 5
# foi digitado e está ou não na lista.

l = list()
cont = 0

while True:
    num = int(input('Digite um valor: '))
    cont += 1 # Calculating how many values we have
    continuar = str(input('Quer continuar [S/N]: ')).upper()

    if cont == 0 or num not in l:
        l.append(num)
        print('Valor adicionado com sucesso!!')
    else:
        print('Valor duplicado! Não vou adicionar...')

    if continuar == 'N':
        break

print('*='*30)
print(f'Foram digitados {cont} elementos')
l.sort(reverse=True)
print(f'A ordem inversa de sua lista é: {l}') # Inverting the list
print(f'O número 5 faz parte da lista na {l.count(5)}ª posição'if l.count(5) > 1 else 'O número 5 não foi digitado')

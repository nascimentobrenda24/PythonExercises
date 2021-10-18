#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#- O primeiro valor é maior

n1 = int(input('\033[1;4;31;40mDigite um número:'))
n2 = int(input('\033[1;4;35;40mDigite outro valor:'))


if n1 > n2 and n2 < n1:
    print(f'O primeiro valor é MAIOR. {n1} > {n2}')

elif n2 > n1 and n1 < n2:
    print(f'O segundo valor é MAIOR. {n2} < {n1}')

print('\n\nObrigada por usar nossos serviços. Volte Sempre!')
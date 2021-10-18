#  Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor
# digitado for ímpar, desconsidere-o.

soma = 0  #ACUMULADOR
cont = 0 #CONTADOR

for c in range(1, 7):
    n = int(input('\033[1;4;34;40mDigite um Valor:'))

    if n % 2 == 0: #Se número for PAR
        soma += n #Na váriavel SOMA, somamos a váriavel, na qual é igual a 0, 'soma' com a variável n(numero) 6X.
        cont += 1

print(f'A soma do(s) {cont} valores pares é {soma}')

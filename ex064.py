# Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário
# digitar o valor 999, que é a condição de parada. No final, mostre quantos números foram digitados e
# qual foi a soma entre eles (desconsiderando o flag).
print('=*'*20, 'DIGITE 999, CASO QUEIRA PARAR O PROGRAMA', '=*'*20)
numero = total = soma = 0

while numero != 999:
    numero = float(input('Digite um número qualquer:'))

    if numero != 999:
        soma += numero
        total += 1
print(f'O programa finalizou. Foram validados {total} valores numéricos. A soma deles foi de aproximadamente {soma:.1f}')

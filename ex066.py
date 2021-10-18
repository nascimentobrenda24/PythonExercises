# Crie um programa que leia números inteiros pelo teclado. O programa só vai parar
# quando o usuário digitar o valor 999, que é a condição de parada. No final, mostre quantos números
# foram digitados e qual foi a soma entre elas (desconsiderando o flag).

n = total = soma = 0

while True:
    n = float(input('Digite um valor qualquer:'))
    # Se equivaler-se ao FLAG, o programa para e mostra a soma dos outros valores.
    if n == 999:
        break

    soma += n
    total += 1
print('~'*200)
print(f'Porgrama finalizado com sucesso!\nForam digitados {total} números\nA soma geral desses valores é {soma}')
print('~'*200)

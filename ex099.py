# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
# Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
from time import sleep


def maior(*num):
    cont = bigger = 0

    print('=-' * 30)
    print('Analisando os valores passados...')

    for value in num:
        print(value, end=' ')
        sleep(0.3)

        if cont == 0:
            bigger = value
        else:
            if value > bigger:
                bigger = value

    print(f'\nForam informados {cont} valores no total')
    print(f'E o maior deles digitado foi {bigger}')


# Principal Program
maior(2, 3, 6, 4, 5)
maior(10, 1, 0)
maior(1, 5)
maior(8)
maior()

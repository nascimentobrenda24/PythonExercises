# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

from time import sleep

def contador(i, f, p):
    # First Validation: Focus in the minority and majority
    # When the "p" variable is negative, we'll change it token, because the compiler understand just positive values
    if p < 0:
        p *= -1
    # The same will occur if the "p" is zero, 'cause, for us, zero mean that the user want jump none value, so it's 1
    if p == 0:
        p = 1

    # Showing the score
    print('-='*20)
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)

    # Second Validation: Focus in the accountant
    if i < f:
        cont = i
        while cont <= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont += p # We sum the "i", whose save the start numbers, with "p", because the "p" variable will validate
            # the jump quantitative

    else:
        cont = i
        while cont >= f:
            print(f'{cont}', end=' ')
            sleep(0.5)
            cont -= p
        print('FIM!')


# Principal Program
contador(1, 10, 1)
contador(10, 0, 2)

print('-=' * 20)
print('Agora é sua vez de personalizar essa contagem!')

start = int(input('Inicio:   '))
end = int(input('Fim:   '))
jump = int(input('Passo:  '))

contador(start, end, jump)
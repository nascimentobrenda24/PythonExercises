# Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
# Seu programa tem que realizar três contagens através da função criada:

def accountant(start, end, jump):
    for s in range(start, end, jump):
        print(start, end, jump)



start = int(input('Inicio: '))
end = int(input('Fim: '))
jump = int(input('Passo: '))

print(accountant(start, end, jump))
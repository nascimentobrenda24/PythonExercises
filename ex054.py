#Crie um programa que leia o ano de nascimento de sete pessoas.
# final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
contotal = 0
maiores = 0
menores = 0

from datetime import date
ano = date.today().year

for c in range(1, 8):
    nascimento = int(input(f'Em que ano a {c}ª pessoa nasceu?: '))
    contotal += 1
    idade = ano - nascimento

    if idade >= 18:
        maiores += 1

    else:
        menores += 1

print(f'Ao todo tivemos pessoas {maiores} MAIORES DE IDADE e {menores} MENORES DE IDADE')
# Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário
# e todos os dicionários em uma lista. No final, mostre:

# A) Quantas pessoas foram cadastradas
# B) A média de idade
# C) Uma lista com as mulheres
# D) Uma lista de pessoas com idade acima da média

guys = list()
person = dict()

sum_year = average = cont = 0

while True:
    person.clear()
    person["nome"] = str(input('Nome: '))

    while True:
        person["sexo"] = str(input('Sexo [M/F]: ')).upper()[0]
        if person["sexo"] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    person["idade"] = int(input('Idade: '))
    sum_year += person["idade"]

    guys.append(person.copy())

    while True:
        proceed = str(input('Quer continuar [S/N]: ').upper())[0]
        if proceed in 'SN':
            break
    if proceed == 'N':
        break

print('-='*30)
# A
print(f'A) Ao todo temos {len(guys)} pessoa(s) cadastrada(s)')
# B
average = sum_year / len(guys)
print(f'B) A médida de idade é de {average:.2f} anos')
# C
print('C) Lista da(s) mulher(es) cadastrada(s): ', end='')
for p in guys:
    if p["sexo"] in 'Ff':
        cont += 1
        print(f'{p["nome"]}', end=',')
# D
print(f'\nD) Lista da(s) pessoa(s) que estão acima da média: ', end='')
for p in guys:
    if p["idade"] >= average:
        print('       ', end='')
        for k, v in p.items():
            print(f'\n    - {k} = {v}', end='')
        print()
print('\n<<<ENCERRADO>>>')
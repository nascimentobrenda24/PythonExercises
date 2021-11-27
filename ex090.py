# Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário. No final, mostre
# o conteúdo da estrutura na tela.

name = str(input('Nome do Aluno(a): '))
average = float(input('Média: '))

# Adding in dictionary
total = {"Nome": name, "Média": average}

# Calculating and comparing the average
acceptance_criteria = average >= 7.5
print('=*'*30)
for n, a in total.items():
    print(f'{n} é igual {a}')

if average != acceptance_criteria:
    print('Situação é igual Reprovado(a) ')
else:
    print('Situação é igual Aprovado(a)')
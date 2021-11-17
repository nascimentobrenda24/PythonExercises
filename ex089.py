#  Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final,
#  mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno
#  individualmente.

record = []

while True:
    print('=' * 15)
    name = str(input('Nome: '))

    grade1 = float(input('Nota1: '))
    grade2 = float(input('Nota2: '))

    average = (grade1 + grade2) / 2

    record.append([name, [grade1, grade2], average])

    answer = str(input('Quer continuar? [S/N]: ')).upper()[0]
    if answer in 'Nn':
        break

print('-='*30)
print(f'{"Nº.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-'*26)
while True:
    opc = int(input('Mostrar notas de qual aluno? (Pressione 999 para sair): '))
    if opc == 999:
        break
    if opc <= len(record) - 1:
        print(f'As notas de {record[opc][0]} foram: {record[opc][1]}')
print('<<<VOLTE SEMPRE>>>')
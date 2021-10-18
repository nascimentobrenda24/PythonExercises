# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 8.0: REPROVADO

print('=*'*300)
aluno = str(input('\033[1;4;36;40mNome: '))
print('=*'*300)
n1 = float(input('\033[1;4;31;40mNota da 1ª avaliação:'))
print('=*'*300)
n2 = float(input('Nota da 2ª avaliação:'))
print('=*'*300)

m = (n1 + n2) / 2


if m >= 8.0:
    print(f'\033[1;4;35mParabéns, {aluno},você tirou {n1} na 1ª av. e {n2} na 2ª av. \n'
          f'SUA MÉDIA FOI {m}\nVOCÊ FOI APROVADO(A)')

elif m < 8.0:
    print(f'\033[1;4;31mInfelizmente, {aluno}, tirastes {n1} na 1ª av. e {n2} na 2ª av.'
          f'\nSua Média foi {m}\nREPROVADO(A)')


else:
    print(f' {n1} {n2} são NOTAS INVÁLIDA')

print('\033[1;4;33;40mOBRIGADA POR CONSUMIR NOSSOS SERVIÇOS. VOLTE SEMPRE!')
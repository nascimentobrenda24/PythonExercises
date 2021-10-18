# Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
# o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

from time import sleep
maioridade = 0
mulheres_menor = 0
homens = 0
while True:
    print('=*'*200)
    idade = int(input('Idade:'))
    sexo = str(input('M/F:')).upper()[0]
    print('Loading...')
    sleep(5)
    continuar = str(input('APERTE C para continuar\nCaso Contrário aperte S para sair')).upper().strip()

    if idade > 18:
        maioridade += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_menor += 1
    if continuar == 'S':
        break

print(f'\n\nHá {maioridade} pessoas maiores de idade 'if maioridade > 1
      else f'Há {maioridade} pessoa maior de idade',
      f'e um total de {mulheres_menor} mulheres menores de idade\nSendo {homens} homens' if mulheres_menor > 1
      else f'e um total de {mulheres_menor} mulher menor de idade')

print('Finalizado com sucesso')

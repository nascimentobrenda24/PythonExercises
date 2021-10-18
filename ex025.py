#Procurando uma string dentro da outra
#Crie um programa que leia o nome de uma pessoa
# e diga se ela tem "SILVA" no nome.


# Tem SILVA em qualquer ala do caracter?
nome = str(input('Qual seu nome completo?: ')).upper().strip()

s = 'SILVA' in nome

print(s)
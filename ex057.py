#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
from time import sleep
print('\033[1;4;36m=*'*20, 'CADASTRANDO', '=*'*20)


sexo = str(input('\033[1;4;30mSexo[M/F]:')).upper().strip()[0]#Ignora espaços, deixa em maiúsculo e lÊ somente a 1ª letra(MASCULINO=M)

print('\033[1;4;30mANALISANDO...')
sleep(5)

#Estrutura de Repetição com teste Lógico(while)
while sexo not in 'FM': #Enquanto sexo diferir de MASCULINO e do sexo FEMININO, o loop será veracito
        print(F'\033[1;4;31mInválido.Não EXISTE O SEXO {sexo}\n')
        sexo = str(input('\033[1;4;30mDigite Novamente Seu Sexo[M/F]:')).upper().strip()[0]
        print('\033[1;4;30mANALISANDO...')
        sleep(5)


print('\033[1;4;34mValidado')
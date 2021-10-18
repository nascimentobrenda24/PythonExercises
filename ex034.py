#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.


from time import sleep
from datetime import date

ano_atual = date.today().year
print('=*'*20, f'AUMENTO SALARIAL {ano_atual}', '=*'*20)

salario = float(input('Seu atual salário: R$'))

print('ANALISANDO DADOS...')
sleep(5)

if salario > 1250.00:
    aumento = (salario * 10/100) + salario
    print('Seu aumento salarial foi de 10%.\nTOTAL A SACAR: R${:.2f}'.format(aumento))
else:
    aumento = (salario * 15/100) + salario
    print('Seu aumento salarial foi de 15%. \nTOTAL A SACAR: R${:.2f}'.format(aumento))
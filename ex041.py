# : A Confederação Nacional de Natação precisa de um programa que
# leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM

from datetime import date

#Armazenamento Dados
ano_atual = date.today().year
nascimento = int(input('\033[1;4;34;43mSeu Ano de Nascimento:'))
i_a = ano_atual - nascimento


#Condicionais
if i_a <= 9:
    print(f'\033[1;31;45m O atleta tem {i_a} anos.\nCLASSIFICAÇÃO: MIRIM ')# len(atleta)-1 = comprimento da
    # string 'atleta' -1, para contar o 1º e o último nome

elif i_a > 9 and i_a <= 14:
    print(f'O atleta tem {i_a} anos.\nCLASSIFICAÇÃO: INFANTIL')

elif i_a > 14 and i_a <= 19:
    print(f'O atleta tem {i_a} anos.\nCLASSIFICAÇÃO: JÚNIOR')

elif i_a > 19 and i_a <= 25:
    print(f'O atleta tem {i_a} anos.\nCLASSIFICAÇÃO: SÊNIOR')

elif i_a > 25:
    print(f'O atleta tem {i_a}.\nCLASSIFICAÇÃO: MASTER')

print('OBRIGADA POR USAR OS NOSSOS SERVIÇOS!!!!!!')
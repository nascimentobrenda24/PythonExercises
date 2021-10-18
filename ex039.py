#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

# Armazendando Dados
nascimento = int(input('Seu Ano de Nascimento:'))
ano_atual = date.today().year
idade_usuario = ano_atual - nascimento

#Condicionando e Validando Dados
if idade_usuario == 18:
    print('\033[1;4;32mEstá NA HORA DE SE ALISTAR\nPara alistar-se entrar no link: http://www.eb.mil.br/')

elif idade_usuario < 18:
    t_alistar = 18 - idade_usuario
    print(f'\033[1;4;31mALISTAMENTO INVÁLIDO. FALTA {t_alistar} anos para VOCÊ ALISTAR-SE!')


elif idade_usuario > 18:
    t_alistar = idade_usuario - 18
    print(f'\033[1;4;31mJÁ PASSOU {t_alistar} anos DA HORA DE ALISTAR-SE.\nPOR FAVOR, COMPARECER EM UM BATALÃO URGENTEMENTE\nPARA MAIS: '
          'http://www.eb.mil.br/ ')




# Empréstimo Bancário
import emoji
from time import sleep
from playsound import playsound

print(emoji.emojize('\033[1;4;7;30m                                         EMPRÉSTIMO BANCÁRIO:money_with_wings:', use_aliases=True))



#Armazenamento de Dados do Comprador
imovel = float(input(emoji.emojize('\033[1;4;30mValor do Imóvel?:credit_card:: R$ ', use_aliases=True)))
salario = float(input(emoji.emojize('Seu Sálário Mensal:dollar:: R$', use_aliases=True)))
anos = float(input(emoji.emojize('Em quantos financiará a casa?::clock1: ', use_aliases=True)))


print('Analisando dados...')#Animações
sleep(5)


#Condicionais
#Se o ano digitado estiver entre 50 anos
if anos <= 50:
    parcelas_mensais = imovel / (anos*12)
    print('\033[1;4;35;40mVocê pagará R${:.2f} mensais por {} anos.'.format(parcelas_mensais, anos))

    #Se as parcelas mensais excederem 30% do salário do comprador ELE NÃO VAI FINANCIAR O IMÓVEL
    if parcelas_mensais > (salario*30/100):
        print('\033[1;4;31mInfelizmente, você NÃO PODERÁ FINANCIAR O IMÓVEL, pois RETIRARÁ MAIS DE 30% DE SEU SALÁRIO '
                  'DE R${:.2f}'.format(salario))

    #Senão, ele PODE FINANCIAR
    elif parcelas_mensais < (salario*30/100):
        print(emoji.emojize('\033[1;4;35;40mFINANCIAMENTO DO IMÓVEL APROVADO COM SUCESSO:city_sunrise:',
                                use_aliases=True))



#Se for MAIOR que 50 anos(juros de 15%)
elif anos >= 50:
    parcelas_mensais = imovel / (anos*12) #preco mensal
    juros = (parcelas_mensais * 15/100) + parcelas_mensais#juros a pagar pelo ano

    print('\033[1;4;35;40mVocê pagará R$ {:.2f} mensais por {} anos'.format(parcelas_mensais, anos))

    #Se passar do ano e o juros correr, mas o comprador EXCEDA 30% DE SEU SALÁRIO ELE NÃO PODERÁ FINANCIAR ESSA RESIDÊNCIA
    if parcelas_mensais > (salario*30/100) and juros > (salario*30/100):
        print('\033[1;4;31mInfelizmente, você NÃO PODERÁ FINANCIAR O IMÓVEL, pois RETIRARÁ MAIS DE 30% DE SEU SALÁRIO '
                  'DE R${:.2f}'.format(salario))

    #Se ele PODER PAGAR O JUROS
    elif parcelas_mensais < (salario*30/100) and juros < (salario*30/100):
        print(emoji.emojize('\033[1;4;35;40mFINANCIAMENTO DO IMÓVEL APROVADO COM SUCESSO:city_sunrise:', use_aliases=True))








    print('\033[1;4;30;43mObrigada por acessar nosso serviços!')

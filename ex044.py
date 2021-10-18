# Exercício Python 044: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# - à vista dinheiro/cheque: 10% de desconto
# - à vista no cartão: 5% de desconto
# - em até 2x no cartão: preço formal
# - 3x ou mais no cartão: 20% de juros

import emoji

print('\033[1;4;33;44m =*'*15, 'XDEVELOPERS STORE', '=*'*15)

produto = float(input('\033[1;4;30m\n\nPREÇOS DAS COMPRAS: R$'))
formas_pagamento = str(input(emoji.emojize('[1] A VISTA DINHEIRO:money_with_wings:\CHEQUE:envelope: \n'
                                           '[2]A VISTA NO CARTÃO:credit_card: \n'
                                           '[3] 2X NO CARTÃO :credit_card:    \n'   
                                           '[4] 3X NO CARTÃO :credit_card:    \n'
                                           '\nQUAL É SUA OPÇÃO? :')))
#Condicionais
if formas_pagamento == '1':
    desconto = produto - (produto * 10/100 )
    print('SUA COMPRA DE R${:.2f} custará R${:.2f} com 10% DE DESCONTOS'.format(produto, desconto))

elif formas_pagamento == '2':
    desconto = produto - (produto * 5/100)
    print('SUA COMPRA DE R${:.2f} custará R${:.2f} com 5% DE DESCONTOS'.format(produto, desconto))

elif formas_pagamento == '3':
    parcelas = produto / 2
    print('SUA COMPRA DE R${:.2f} custará R${:.2f} de 2X DE R${:.2f}'.format(produto, produto, parcelas))

elif formas_pagamento == '4':
    parcelas = int(input('Quantas parcelas?:'))
    parcelas_tot = produto/ parcelas
    juros = parcelas_tot + (parcelas_tot * 20/100)
    produto_final = produto + juros
    print('SUA COMPRA DE R${:.2f} será parcela em {}X de R${:.2f}\nCOM JUROS, SUA COMPRA FICARÁ R${:.2f}'.format(produto, parcelas, parcelas_tot, produto_final))


print('\033[1;4;30mOBRIGADA POR USAR NOSSOS SERVIÇOS. VOLTE SEMPRE!!')

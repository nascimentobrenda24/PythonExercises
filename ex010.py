# Conversor de Moedas( $ ------ R$)


money_real = float(input('How many money do you have in your wallet ?: R$'))

dollar = money_real / 5.62#cotação atual do dolar(2020)

print('You can buy ${:.2f} with your R${:.2f}'.format(dollar, money_real))

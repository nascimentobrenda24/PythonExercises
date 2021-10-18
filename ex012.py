# Calculando Descontos(Porcentagem)

print(10*'=*', 'LIQUIDAÇÃO(5% DE DESCONTO)', '=*'*10)
preco = float(input('Qual o preço do produto:R$'))

desconto = preco - (preco * 5/100) #calculo porcentagem e subtraio o valor atual com o antigo


print('O produto custa R${:.2f}'.format(desconto))
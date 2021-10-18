#Dobro, Triplo, Raiz Quadrada

valor = float(input('Digite um valor:'))

d = valor*2
t = valor*3
raiz_quadrada = valor **(1/2)
print('O valor {}, tem os seguintes valores:'
      '\nRaiz Quadrada: {:.1f}'#:.1f para mostrar apenas a primeira casa decimal, caso houver
      '\nDobro: {:.0f}'
      '\nTriplo: {:.0f}'.format(valor, raiz_quadrada, d, t))

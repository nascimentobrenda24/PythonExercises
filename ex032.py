# Ano Bissexto
'''Divisível por 4. Sendo assim, a divisão é exata com o resto igual a zero;
Não pode ser divisível por 100. Com isso, a divisão não é exata, ou seja, deixa resto diferente de zero;
Pode ser que seja divisível por 400. Caso seja divisível por 400, a divisão deve ser exata,
deixando o resto igual a zero.
'''

from datetime import date
from emoji import emojize


ano = int(input('Que ano quer analisar?. Digite 0 para o ano que você se encontra:'))

if ano == 0:
    ano = date.today().year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(emojize('{} é BISSEXTO:globe_with_meridians:'.format(ano)))

else:
    print(('{} definitivamente NÃO É BISSEXTO '.format(ano)))

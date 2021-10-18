# Teorema de Pitagoras

from math import hypot

c_o = float(input('C.O:'))
c_a = float(input('C.A:'))
h = hypot(c_a, c_o)

print('Enfim, a hipotenusa {:.2f}'.format(h))
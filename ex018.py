# Seno, Cosseno, tangente

from math import radians, sin, cos, tan

angulo = float(input('Ângulo:'))

sen = sin(radians(angulo))
cos = cos(radians(angulo))
tang = tan(radians(angulo))

print('O Ângulo {} tem as seguintes medidas :\nSen: {:.2f}\nCos: {:.2f}\nTang: {:.2f}'
      .format(angulo, sen, cos, tang))


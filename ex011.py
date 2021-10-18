# Pintando uma parede

b = float(input('Largura da Parede:'))
h = float(input('Altura da Parede: '))

area = b * h
tinta = area/2 # A cada 2m² de parede precisa de 1l de tinta

print('Sua parede tem as dimensões {}X{} e sua área é {}m²\n'
      'Para pinta-la essa parede, precisaremos de {:.2f}l de tinta'.format(b, h, area, tinta))


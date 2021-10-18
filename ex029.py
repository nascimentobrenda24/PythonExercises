#Radar Eletrônico
#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem
# dizendo que ele foi multado.
# A multa vai custar R$7,00 por cada Km acima do limite.



from time import sleep



v = float(input('Velocidade do Carro: KM'))

if v > 80:
    multa = (v - 80) * 7

    print('MULTADO!!.EXCEDEU O LIMITE DE KM\nTOTAL A PAGAR: R${:.2f}\n '.format(multa))


else:
    print('Tenha um Bom Dia. Continue dirigindo com cautela e segurança!!.')


# Crie um mp3

import playsound

music = str(input('\033[1;4;33mEscolha uma Música:')).upper().strip()

if music == 'BABY CAN I HOLD YOU':
    playsound.playsound('baby_can_i_hold_you.mp3')


else:
    print('\033[1;31mDesculpe, ainda não temos essa faixa em nosso programa. Tente Novamente!!')
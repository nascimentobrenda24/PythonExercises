#Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
# indo de 10 até 0, com uma pausa de 1 segundo entre eles.

#Importações para: Tocar música,mostrar emoji, pausar, cores.
from playsound import playsound
from emoji import emojize
from time import sleep
from colorama import Fore, Style


#Código Gráfico
print(f'{Fore.BLUE}=*' * 200)
print(Fore.YELLOW)

print(emojize('CONTAGEM REGRESSIVA PARA 2021 :date: :fire: #SAICARNIÇA2020 #XÔCOVID ', use_aliases=True))

print(f'{Fore.BLUE}=*' * 200) #{Style.RESET_ALL} == FINALIZA A COR NESSE CARACTER 'GRÁFICO'



#Código Fonte


for fogos in range(10, 0, -1): #-1 para ser uma contagem de 10 a 0 DECRESCENTE
    sleep(0.5)
    print(f'{Fore.BLACK}', fogos)
    sleep(0.5)


print(emojize('FELIZ ANO NOVO!! :boom:', use_aliases=True))
playsound('fogos.mp3.mp3')

#Verificicando as primeiras letras de um texto
# Exercício Python 024:
# Crie um programa que leia o nome de
# uma cidade diga se ela começa
# ou não com o nome "SANTO".


#'Santo' no inicio
cidade = str(input('Em que cidade você nasceu?: ')).upper().strip()

s = cidade[:5] == 'SANTO' #SANTO(5 PALAVRAS)
print(s)

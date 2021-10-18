# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo,
# desconsiderando os espaços.

frase = input("Qual a frase? ").upper().replace(" ", "") #replace transforma os espaços:' ' em 'unidos' com o outro caracter ''.
if frase == frase[::-1]: #se a frase equivaler a mesma, só que de trás para frente É PALÍNDROMO
   print("A frase é um palíndromo")
else:
    print("A frase não é um palíndromo")
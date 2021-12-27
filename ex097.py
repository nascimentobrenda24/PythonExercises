# Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma
# mensagem com tamanho adaptável.

# The solution consist in show the message and adapt the decoration in the word size
# To do this we call the len() method and multiply the str with a variable, whose save the "txt" paramether, to expand
# the style lines according with the text size
def escreva(txt):
    size = len(txt)
    print('~'*size)
    print(txt)
    print('~'*size)


escreva('Olá Mundo')


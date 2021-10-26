#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
#  se a expressão passada está com os parênteses abertos e fechados na ordem correta.

while True:
    entrada = str(input('Digite a expressão: '))

    para_esquerda = entrada.count('(')
    para_direita = entrada.count(')')

    if para_esquerda == para_direita:
        print(f'Essa expressão {entrada} é válida.')
    else:
        print(f'Essa expressão {entrada} é inválida.')
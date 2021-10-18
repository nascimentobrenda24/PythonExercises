# Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado
# pelo usuário. O programa será interrompido quando o número solicitado for negativo.
print('\033[1;30;46m=*'*20, 'CÁLCULO DE TABUADA (INFINITO)', '=*'*20)
print('\nREGRA Nº1: VALORES NEGATIVOS FINALIZAM O PROGRAMA!                                                               \033[m')

while True:
    print('\033[1;33m~'*200)

    # Lendo valores do user, enquanto verdade(loop infinito)
    n = float(input('Digite um valor:'))

    print('~'*200)

    #Se número equivaler a valores negativos, o programa para e mostra o produto de outros valores
    if n < 0:
        break

    #Achando o produto
    for c in range(0, 11):
        m = n * c  # Multiplicação é igual ao contador e ao numero digitado pelo usuário
        print(f'\033[1;4;34m{n:.0f} X {c:.0f} = {m:.0f} \033[m')#Mostrando, de forma organizada, a multiplicação acima.

print('\033[1;30mFIM DO PROGRAMA TABUADA. VOLTE SEMPRE!')
# Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerrará quando ele disser que quer mostrar 0 termos.
print('\033[1;4;30m=====================GERADOR DE UMA PA===============================')
#Variáveis armazenadoras de dados do usuário
p1 = int(input('\033[1;4;30;46mPrimeiro Termo:'))
razao = int(input('Razão:'))

# Variáveis de controle de loop ou manipulação de dados predefinidos
termo = p1 #A sequência começa com o Primeiro Termo
cont = 1 # Responsável por começar o LOOP SECUNDÁRIO
total = 0 #Total de termos reenvindicados pelo usuário começa, obviamente, com 0.
novos_termos = 10 # Responsável por começar o LOOP PRINCIPAL

#Loop Principal
while novos_termos != 0: #Quando for 0 o programa finaliza
    total += novos_termos # total começa a valer 10( total = 0 + 10, porém depois como o usuário modificará a variável novos_termos
    # ele modificará de acordo com a progressão do loop

    #Loop dos primeiros 10 termos da P.A
    while cont <= total: #Enquanto contador for menor ou igual ao total
        print(termo, end='>')
        termo += razao #Calculo da P.A
        cont += 1 # Finaliza o loop, pois a cada ciclo +1 é dado a essa variável, portanto sendo um loop finito
    print('PAUSA', end='')

    # Usuário manipulando termos a mais.
    novos_termos = int(input('\n\nQuantos termos a mais desejas?\nR='))

print(f'FIM DA CONTAGEM DE PROGRESSÃO ARITMÉTICA.\nTIVEMOS {total} TERMOS MOSTRADOS')

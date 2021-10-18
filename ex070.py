# Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
# se o usuário vai continuar ou não. No final, mostre:

# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
print('\033[1;32;46m=*'*20, 'XDEVELOPERS STORE', '=*'*20)

#Variáveis de Controle do Laço com Teste Lógico ou de suas condições
continuar = gasto_final = produtos_mais_1000 = preco_barato = produtos_caro_nome = caro = produtos_barato_nome = cont = 0

while True:
    cont += 1 # A cada compra contamos +1
    print('\033[m\033[1;30m~'*45, f'{cont}ª COMPRA', '~'*300)
    # Código Fonte
    nome = str(input('\033[1;34mNome do Produto:')).upper()
    preco = float(input('\033[1;33mPreço: R$'))
    continuar = str(input('\033[1;36mQuer continuar?[S/N]\nR=')).upper()[0]

    #Se continuar for 'S' ou 'N', rodaremos os seguintes scripts:
    if continuar == 'S' or 'N':
        #Preço Final das Compras: A soma de todos os preços inputados.
        gasto_final += preco # Somar todos os valores por 0, no qual é o valor da variável gasto_final, resulta em soma entre eles(1+0+9 = 1+9 = 10)

        # Produto +deR$1000
        if preco > 1000:
            produtos_mais_1000 += 1 # Cada vez que houver um preço maior que 1000, ele será contado e posto nessa variável
            # Na primeira Compra, o produto será o maior preço existente, já que nenhum outro valor fora inputado.
            if cont == 1:
                produtos_caro_nome = nome #Na primeira compra, ele será o maior valor digitado
                caro = preco #Logo é o mais caro, até então

            else: #Ao passar da primeira compra, ele é atribuido ao nome de cada compra que for
                # maior que 1000 reais.
                #Se o novo preço for maior que o preço, anteriormente atribuido a caro, ele agora passa a ser o mais caro
                if preco > caro:
                    produtos_caro_nome = nome
                    caro = preco


        # Produtos equivalentes ou menores a 1000 reais
        if preco <= 1000:
            if cont == 1:
                # Barato
                preco_barato = preco
                produtos_barato_nome = nome
                # CARO
                produtos_caro_nome = nome
                caro = preco

            else:
                # Se o preço for menor ao caro, ele será o +barato
                if preco < caro:
                    produtos_barato_nome = nome
                    preco_barato = preco

                # Se o preço for maior ao barato, ele será o +caro
                if preco > preco_barato:
                    produtos_caro_nome = nome
                    caro = preco


        # Mesmo rodando os seguintes scripts acima, quando for 'N' o loop para.
        if continuar == 'N':
            break

# Fim da Compra
print('\033[1;30m~'*40, 'COMPRA FINALIZADA COM SUCESSO', '~'*40)
print(f'                    O VALOR TOTAL da compra foi: R${gasto_final:.2f}')
print(f'                    Tivemos {produtos_mais_1000} produtos acima de R$1000,00, porém o +CARO foi: {produtos_caro_nome}')
print(f'                    O PRODUTO MAIS BARATO FOI: {produtos_barato_nome} ')
print('~'*200)
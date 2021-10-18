#Crie um programa que simule o funcionamento de um caixa eletrônico.
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)  e o programa vai
# informar quantas cédulas de cada valor serão entregues. OBS: considere que o caixa possui cédulas
# de R$50, R$20, R$10 e R$1.
#Banco BN: Ficticío e Própio: Terá notas de R$200,100,50,20,10, 1



#Interface de ambas forças do programa
print('\033[1;30m~'*200)

print(f'                                                     BANCO BN                                        ')
print('\033[1;30m~'*200)

'''#Usando o for

#Variáves
valor = int(input('\033[1;4;34mSaque: R$\033[1;4;31m'))
ced_disp = [200, 100, 50, 20, 10, 1] #cédulas disponíveis em nosso Banco(BBN)

#Estrutura de Repetição com Variável de Controle
#O saque será feito no intervalo de tempo do comprimento de nossa lista(ced_disp)
for s in range(len(ced_disp)):
    # As notas serão dadas de acordo com a divisão do valor inputado com as ced_disp(uma a uma, nesse intervalo)
    notas = valor // ced_disp[s]
    # Se notas forem maiores que 0 mostramos a quantidade de notas necessárias a pagar o user
    if notas > 0:
        # Ajustando possível erro gramatical(Plural X Singular)
        print(notas, f"nota de R${ced_disp[s]}" if notas == 1 else f'notas de R${ced_disp[s]}')
        #Para fragmentar e finalizar o valor com as notas no loopinh, há carecimento de subtrai-lo pelos valores dados ao usuário
        valor = valor - (notas * ced_disp[s])
'''
#Usando o while

#Variáveis
ced_disp = [200, 100, 50, 20, 10, 1]
valor = int(input('\033[1;36;40mSAQUE: R$ '))
cont = 0 #Responsável por pegar cada item de nossa lista(ced_disp)


while True:
    #Retiramos do valor inputado, até quando possível, ou seja, ao chegar a 0, de nossas cédulas disponíveis
    if valor >= ced_disp[cont]:
        #Quantidade de notas
        nota = valor // ced_disp[cont]
        # Ajustando possível erro gramatical(PLURAL VS Singular)
        print(f'\033[1;30;46m{nota} nota de R$ {ced_disp[cont]}\033[m' if nota == 1 else f'\033[1;30;46m{nota}{nota} notas de R${ced_disp[cont]}' )
        # Fragmentando o valor por sua nota até zerá-lo por completo
        valor = valor % ced_disp[cont]
    cont += 1
    if valor == 0:
        break
print('\n\033[1;30mPrograma Finalizado com sucesso. Volte Sempre!!\033[m')
print('~'*200)
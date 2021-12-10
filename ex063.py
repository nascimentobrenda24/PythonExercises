# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros
# elementos de uma Sequência de Fibonacci.
# Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

# A lógica do programa baseia-se no fato de haver a predefinição de valores na seq.fibonacci(0,1). Entretanto,
# o que ocorre é a soma infinita ou finita, isso o user que determina, desses valores com o resultado. Assim, criamos 3
# variáveis(t1 = começa valer 0; t2 = começa valer 1; t3 = define o valor volátil,dado pela soma de t1+t2). Assim,
# nota-se que devemos considerar que quando o contador, no qual é o 'cont' e começa com 1 e somarar-se a cada loop,
# for menor que a quantidade de termos,definida pelo usuário, o loop rodará com os seguintes algoritimos: quando o cont==1,
# ele estará na 1º linha, digamos assim, portanto escrevemos na tela o valor 0, predefinido na sequência, assim também
# vale ao cont==2, segunda linha, na qual será equivalente a 1, posteriormente, ao passar dessas duas verificações,
# criamos a variável t3 que receberá a soma de t1+t2, com os seguintes pré-requisitos: a cada soma ocorrerá esse fenômeno
# (t1=t2 ; t2= t3), dessa maneira, t1 a cada loop passa ser t2 e o mesmo ocorre finitamente/infinitamente com t2 e t1.
#Ex:  0-1-1-2-3-5-8...
#t =  1+ 2+ 3+ 1+ 2+ 3+ 1+ 2+ 3...

# Código Fonte
print('\033[1;30;44m=*'*20, 'SEQUÊNCIA FIBONACCI', '=*'*20, '\033[m')
termos = int(input('Quantos TERMOS DESSA SEQUÊNCIA desejas?\nR='))
# Padrões da Sequência Fibonacci
t1 = 0
t2 = 1

#Responsável por dar início ao loop
cont = 1
print('\033[1;33m='*300)
#Enquanto o contador for menor que a quantidade de termos
while cont <= termos:
    # Se o contador valer 1
    if cont == 1:
        print(0, '>', end='')
    #Se o contador valer 2
    elif cont == 2:
        print(1, '>', end='')
    # Quando a primeira parte da estrutura fibonática passar (0, 0+1, 1, 1+1, 2 ...)
    else:
        t3 = t1 + t2 #Sequência Fibonacci

        # O termos permutarão entre si, ao longo do programa
        t1 = t2
        t2 = t3

        print(t3, end=' ')

        print('>'if cont != termos else '.', end='')

    cont += 1 # Encerrando o looping

print('\n')
print('\033[1;33m='*300)
print('FIM.')















cont = 1 #Responsável por iniciar o loop


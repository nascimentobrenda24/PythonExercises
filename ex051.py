#Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os
# 10 primeiros termos dessa progressão.

''' P.A = Sequência numérica que utiliza onde cada número é obtido a partr da soma de um mesmo valor, chamado
RAZÃO.
Ex¹: (2,5,8,11...) 2+3 = 5; 5+3= 8 e etc...
    Estamos somando 3X cada valor para obter o valor sucessor/posterior. R= 3.

Ex²: (10,7,4...)
    R = x-y : R= 7-10 == R=-3.

Ex³: (8,8,8,...)
    R= 8-8: R=0.

Classificando PROGRESSÕES:
Se R=0 :
    PROGRESSÃO CONSTANTE
Se R<0:
    PROGRESSÃO DECRESCENTE

Se R>0:
    PROGRESSÃO CRESCENTE

    TERMO GERAL DE UMA P.A:
        Facilita a eu não ficar R = posterior - antecessor, até por que, em uns casos, não dará a resolver esse método.
        Vamos pela fórmula:
        enésimo_termo_PA = primeiro_termo + (numero_de_termos - 1) * razao
        '''

print('=*'*20, 'TERMOS DE UMA P.A', '=*'*20)

primeiro_termo = int(input('PRIMEIRO TERMO DA P.A:'))
razao = int(input('RAZÃO:'))
enesimo_termo = primeiro_termo + (10-1) * razao

for PA in range(primeiro_termo, enesimo_termo, razao):
    #Do primeiro termo, até o 'enésimo termo', 'pulando' de 'razão' em razão'.
    print(PA, end='---')

print('ACABOU!!')
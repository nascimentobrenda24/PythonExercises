# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os
# 10 primeiros termos da progressão usando a estrutura while.

print('\033[1;36;40m=*'*20, 'CALCULANDO OS 10 PRIMEIROS TERMOS DE UMA P.A(WHILE)', '=*'*20)

#Código Fonte

p1 = int(input('Primeiro Termo:'))
razao = int(input('Razão:'))

termo = p1 #10 primeiros termos de uma P.A. Começa com o p1
cont = 1 #Contador inicia com 1, para dá inicio ao loop

while cont <= 10: #Enquanto o contador for inferior ou equivalente a 10, iniciará o loop.
    print(termo, end='>') #Começa mostrando o valor inicial da PA(P1)
    termo += razao # primeiro termo + razao = sequencia posterior
    cont += 1 #Isso possibilitará o fim do loop, já que a cada loop ele contará + 1 e quando diferir da minoridade do
    # contador com 10, pois o novo contador será 11(1+10), o 'while' para.


#Usando o For
print('\033[1;31m\nUSANDO O FOR', '=*'*20)
p1 = int(input('\n\nPrimeiro Termo:'))
razao = int(input('Razão:'))
enesimo_termo = p1 + (10-1)*razao

for c in range(p1, enesimo_termo+1, razao):
    print(c)
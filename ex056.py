# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# a média de idade do grupo,
# qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.

#Variáveis de Controle
somatorio = 0
cont = 0
cont_homem = 0
maioridade_homem = 0
nome_velho = ''
mulher_menos_20 = 0

#Laço de Repetição
for p in range(1, 5):
    #Cadastrando Variáveis
    print('\033[1;30m=*'*5, f'{p}ª PESSOA', '=*'*5)
    nome = str(input('Nome:')).upper().strip()
    idade = int(input('Idade:'))
    #cont += 1
    sexo = str(input('Sexo[F/M]:')).upper().strip()
    cont += 1
    somatorio += idade

    #Condicionais
    #Se estiver no primeiro laço e o sexo for MASCULINO, ele será, a idade, a maioridade digitada e, obviamente, a menoridade digitada.
    if p == 1 and sexo == 'M':
        cont_homem += 1
        maioridade_homem = idade
        nome_velho = nome

    #Senão ao passar do primeiro laço e o sexo for MASCULINO, ele será o 'novo' maior, caso ultrapasse a maioridade e assim cabe a menoridade.
    elif p != 1:
        cont_homem += 1
        if sexo == 'M' and idade > maioridade_homem: #Se idade for maior que a maioridade, acima definida, ela será, agora, a MAIORIDADE.
            maioridade_homem = idade
            nome_velho = nome

        if cont_homem == 0: #Quando não houver homens na contagem, mostraremos a idade = 0 e nome_velho =
            nome_velho = '\033[1;31m<NÃO VALIDADO>\033[m'
            maioridade_homem = '\033[1;31m<NÃO VALIDADO>\033[m'

    if sexo == 'F' and idade < 20:
        mulher_menos_20 += 1

media = somatorio / cont
print(f'A média geral das idades foi {media}')
print(f'O homem mais velho tem {maioridade_homem} \033[1;30manos e se chama {nome_velho}')
print(f'\033[1;4;30mHá {mulher_menos_20} menina que tem menos de 20 anos' if mulher_menos_20 <= 1
      else f'\033[1;4;30mHá {mulher_menos_20} meninas que tem menos de 20 anos')


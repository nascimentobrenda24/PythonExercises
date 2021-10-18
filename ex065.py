# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média
# entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário
# se ele quer ou não continuar a digitar valores.

print('\033[1;4;36;40m=*'*15, 'CALCULADORA DE MÉDIA ARITMÉTICA E MAIORIDADE VS MENORIDADE', '=*'*20)

# Variável gatilho ao inicio do loop
options = 'S'
#Variáveis de controle
media = soma_numbers = cont = maior = menor = 0

# Validação com Estrutura de Repetição Com Teste Lógico
while options in 'Ss':
    n = float(input('Digite um valor numérico qualquer:'))
    cont += 1 # Contador(quantidade de números)
    options = str(input('Quer continuar?[S/N]:\nR=')).upper()[0]

    # Média Aritmética
    soma_numbers += n  # (0+n1+n2+n3... = n1 + n2 + n3 ... )

    #Maior & Menor
    if cont == 1: # Quando estiver no primeiro loop; O maior e o menor equivalem-se, pois, até então, só um valor digitado
        maior = menor = n

    else: # Senão. Ao passar do primeiro loop
        if n > maior: # Se numero for maior que a variável MAIOR, agora ele é o NOVO_MAIOR
            maior = n
        elif n < menor:#Se numero for menor que a variável MENOR, agora ele é o NOVO_MENOR
            menor = n
# Média Aritmética
media = (soma_numbers) / cont  # (1+2+3+4) / 4

# Mostrando valores
print('~'*200)
print(f'\nPrograma finalizado com sucesso. Você digitou {cont} valores.')
print(f'A Média Aritmética Geral desses valores fora de {media:.1f} ')
print(f'O MAIOR valor digitado foi: {maior:.0f}\n O menor valor digitado foi: {menor:.0f}')
print('~'*200)

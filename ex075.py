# Desenvolva um programa que leia quatro valores e guarde-os em uma tupla. No final, mostre:
# Quantas vezes apareceu o valor 9
# Em que posição foi digitado o primeiro valor 3
# Quais foram os números pares

from random import sample

value = (int(input('Digite um número: ')),
         int(input('Digite outro número: ')),
         int(input('Digite mais um número:')),
         int(input('Digite só mais esse número: ')))

print(f'\nO valor 9 apareceu {value.count(9)}', end=' ')
print('vezes'if value.count(9) > 1 else 'vez')

# If ever 3 apper in this tuple the interpreter will recognize as True, otherwise will be False
print(f'O número 3 foi digitado na {value.index(3)+1}ª posição' if value.count(3) == True
      else 'O número 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram: ', end=' ')

# Searching pair numbers in the variable "value" length, if ever these numbers was pairs, otherwise will not appear in
# result
for n in value:
    if n % 2 == 0:
        print(n, end='>')

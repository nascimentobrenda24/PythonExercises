#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
#  se a expressão passada está com os parênteses abertos e fechados na ordem correta.

exp = str(input('Digite uma expressão matemática:'))
battery = []

for symbol in exp:
    if symbol == "(":
        battery.append(symbol)

    elif symbol == ")":
        if len(battery) > 0:
            battery.pop()
        else:
            battery.append(symbol)
            break

if len(battery) == 0:
    print('Sua expressão está válida')
else:
    print('Sua expressão não é válida')

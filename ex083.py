#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
#  se a expressão passada está com os parênteses abertos e fechados na ordem correta.

l = ["(", ")"]
e = input('Input a value:')

#Validating the existence of parentheses
#First Probabily: Have parentheses
if l.index("(") > 1 or l.index(")"):
    print("Your equation have parentheses!!")

elif l.index("(") > 1 and l.index(")") == 0:
    print('')




else:
    print("Your equation haven't paretheses!!")
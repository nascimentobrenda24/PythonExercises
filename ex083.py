#  Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar
#  se a expressão passada está com os parênteses abertos e fechados na ordem correta.

l = ["(", ")"]
e = input('Digite um valor:')

#Validating the existence of parentheses

# After validate the fact with have parenthesis, we may analyze if the combination of both it is correctly
if e.count("(") > 0 or e.count(")"):
    print("Sua equação tem parênteses!!")

# When the user digit in equation a parentheses and don't completed with other
elif e.count("(") > 0 and e.count(")") == 1 or e.count(")") > 0 and e.count("(") == 1:
    print('Só um parênteses detectado\nSua expressão está incompleta, logo inválida!')




else:
    print("Sua equação não tem parênteses!!")
    print('Sua equação está válida!')
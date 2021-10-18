#Reajuste Salarial( Calculo de Porcentagem) 15%


funcionario = str(input('Nome do Funcionário(a):'))
salario = float(input('Qual é o salário de {}?: R$ '))

aumento = salario + (salario * 15/100)

print('{} agora recebe R${}'.format(funcionario, aumento))
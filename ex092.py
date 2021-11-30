# Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
# Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e
# acrescente, além da idade, com quantos anos a pessoa vai se aposentar.

from datetime import datetime

data = dict()

data["Nome"] = str(input('Nome: '))
year_born = int(input('Ano de Nascimento: '))
data["Idade"] = datetime.now().year - year_born
data["Ctps"] = int(input('Nº da CTPS ( Digite 0 se não tiver ): '))

if data["Ctps"] != 0:
    data["Contratação"] = int(input('Ano de Contratação: '))
    data["Salário"] = float(input('Salário: '))
    data["Aposentadoria"] = data["Idade"] + ((data["Contratação"] + 35) - datetime.now().year)
print('-='*30)
for k, v in data.items():
    print(f'  - {k} tem o valor {v}')
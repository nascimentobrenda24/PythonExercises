# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços na sequência
# No final, mostre uma listagem de preços, organizando os dados em forma tabular .

# REFAZER no dia 14.10
print("BRENDA'S PAPE")
products = ('Estojo', 10,
            'Lápis', 1,
            'Caneta', 1.50,
            'Lapiseira', 2,
            'Apontador', 0.5,
            'Lápis de Cor', 12,
            'Mochila', 60,
            'Tinta Guache', 15,
            'Papel A4', 20,
            'Régua 30 cm', 8,
            'Marcador', 2,
            'Compasso', 20)
print('-'*20)
print(f'{"TABELA DE PREÇOS"}')
print('-'*20)
# Name Table
for p in range(0, len(products)):
    if p % 2 == 0:
        print(f'{products[p]:.<30}', end=' ')
    else:
        print(f'R$ {products[p]:<7.2f}')
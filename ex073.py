# Crie uma tupla preenchida com os 20 primeiros colocados da tabela do Campeonato Brasileiro de Futebol, na ordem de
# colocação. Depois mostre:

# Apenas os 5 primeiros colocados
# Os últimos 4 colocados da tabela
# Uma lista com os times em ordem alfabética
# Em que posição na tabela está o time da Chapecoense


colocacao = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza',
             'Corinthians', 'Red Bull Bragantino', 'Athletico PR',
             'Internacional', 'Fluminense', 'América-MG', 'Atlético-GO',
             'Cuiabá-MT', 'Ceará', 'São Paulo', 'Juventude', 'Santos',
             'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
cont = 0

# Adptei somente para o TOP4 da tabela
print('\033[1;33;4;40m                                          TABELA DO BRASILEIRÃO (ATUALIZADA)                                    ')
for c in colocacao:
    cont += 1
    print(f'\033[1;36m{cont}º colocado é {c}')

print(f'\n\033[m\033[1;34;40mOs times do G4 são:\033[m\n\033[1;34;40m{colocacao[0:4]}\033[m')
print(f'\n\033[1;33;40mOs times da ZONA DE REBAIXAMENTO são:\033[m\n\033[1;33;40m{colocacao[-4:]}\033[m')
print(f'\n\033[1;35;40mA ordem alfabética da TABELA é:\n{sorted(colocacao)}\033[m')
print(f'\n\033[1;31;40mO time da Chapecoense se encontra na {colocacao.index("Chapecoense")+1}º posição\033[m')

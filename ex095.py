# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

players = []
player = {}
each_matches = []



while True:
    player.clear()
    each_matches.clear()

    tot = 0
    player["Nome"] = str(input('Nome do Jogador: '))
    player["Partidas"] = int(input(f'Quantas Partidas {player["Nome"]} jogou?: '))

    if player["Partidas"] != 0:
        for p in range(player["Partidas"]):
            goals_per_matches = int(input(f'   - Gols na partida {p+1}: '))

            each_matches.append(goals_per_matches)
            tot += goals_per_matches

            player["Gols por Partidas"] = each_matches[:]
            player["Total de Gols"] = tot
    else:
        print('Esse jogador(a) não participou de nenhum partida.')

    # Adding the dict datas in the majority database: "players" list
    players.append(player.copy())

    while True:
        proceed = str(input('Quer Continuar? [S/N]: ')).upper()[0]
        if proceed in 'SN':
            break

        print('Ops! Dado inacessível por dígito errado. Tente Novamente!')

    if proceed == 'N':
        break

print('-='*30)

# Scoreboard Style
print('cod', end='')
for e in player.keys():
    print(f'{e:>20}', end='')
print()
# Scoreboard Results
print('-'*80)
for k, v in enumerate(players):
    print(f'{k:>4}', end='')
    for d in v.values():
        print(f'{str(d):<20}', end='')
    print()
print('-'*80)
while True:
    search = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if search == 999:
        break
    if search >= len(players):
        print(f'ERRO! Não existe jogador com código {search}!')
    else:
        print(f'-----LEVANTAMENTO DO JOGADOR {players[search]["Nome"]}')
        for i, g in enumerate(players[search]["Gols por Partidas"]):
            print(f'   No jogo {i+1} fez {g} gols.')
    print('-'*40)
print('<<VOLTE SEMPRE>>')
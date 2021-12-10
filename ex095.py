# Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes
# do aproveitamento de cada jogador.

players = []
player = {}
each_matches = []

tot = 0

while True:
    player.clear()
    each_matches.clear()

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


print('-='*50)
print(f'{str("cod."):>3}', end='')
for c in player.keys():
    print(f'{c:^16}', end='  // ')
print()
print('-='*50)
for i, datas in enumerate(players):
    print(f'{i:>3} {datas["Nome"]:>10} {str(datas["Gols por Partidas"]):>15} {datas["Total de Gols"]:>10}')

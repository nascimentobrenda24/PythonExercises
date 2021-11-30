# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

# ** I DID ALONE THIS EXERCISE
game = {}
each_matches = []
tot = 0

game["Nome"] = str(input("Nome do Jogador: "))
game["Partidas"] = int(input(f'Quantas Partidas {game["Nome"]} jogou?: '))

if game["Partidas"] != 0:
    # Calculating the goals in the respective games in time of matches, whose this player played
    for p in range(game["Partidas"]):
        goals_per_matches = int(input(f'  - Gols na partida {p+1}: '))
        each_matches.append(goals_per_matches)

        tot += goals_per_matches
        game["Gols por Partida"] = each_matches
        game["Total de Gols"] = tot
else:
    print('Esse jogador(a) não participou de nenhuma partida.')

print('-='*30)
# Iº demonstration
print(game)
# IIº demonstration
print('-='*30)
for k, v in game.items():
    print(f'O campo {k} está preenchido com {v}')
# IIIº demonstration
print('-='*30)
print(f'O jogador(a) {game["Nome"]} jogou {game["Partidas"]} partidas')
for p in range(game["Partidas"]):
    print(f'Na partida {p+1}, fez {game["Gols por Partida"][p]} gols')


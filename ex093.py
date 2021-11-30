# Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador
# e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será
# guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

game = {}
tot = 0
list_goals = []

game["Nome"] = str(input("Nome do Jogador: "))
game["Partidas"] = int(input(f'Quantas Partidas {game["Nome"]} jogou?: '))

if game["Partidas"] != 0:
    # Calculating the goals in the respective games in time of matches, whose this player played
    for p in range(game["Partidas"]):
        goals_per_matches = [int(input(f'  - Gols na partida {p+1}: '))]
        #list_goals = goals_per_matches

        for t, p in enumerate(goals_per_matches):
            tot += goals_per_matches[p]
            game["Gols por Partida"] = goals_per_matches
        game["Total de Gols"] = tot


print(game)

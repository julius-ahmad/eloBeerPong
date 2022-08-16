import GraphDrawer
import DataHandler
import math
DEFAULT_ELO = 1000
K_VALUE = 32


def compile_elos(games):
    """
    takes the games played and computes ranks over time
    @param games: a list of tuples of players who played in a game and who won (number represents if 2 left players won)
    @return: a list of dictionaries of player to elo rank for after each game played
    """
    player_elos = {}
    timeline = []
    for game in games:
        for player in game[0]:
            if player not in player_elos:
                player_elos[player] = DEFAULT_ELO
    timeline.append(player_elos.copy())

    for game in games:
        if game[1] == '1':
            new_elo(game[0], player_elos, True)
            timeline.append(player_elos.copy())
        else:
            new_elo(game[0], player_elos, False)
            timeline.append(player_elos.copy())

    return timeline


def new_elo(players, player_elos, won):
    """
    Updates the new ranks of each player after each game
    @param players: list of players in a game
    @param player_elos: a dictionary of the current ranks of each player
    @param won: a boolean representing if the left two players won
    """
    p1 = players[0]
    p2 = players[1]
    p3 = players[2]
    p4 = players[3]

    #Calculating the opponent players rank by considering teammates rank to prevent carrying/sandbagging
    p1_opponent_rank = player_elos[p3] + player_elos[p4] - player_elos[p2]
    p2_opponent_rank = player_elos[p3] + player_elos[p4] - player_elos[p1]
    p3_opponent_rank = player_elos[p1] + player_elos[p2] - player_elos[p4]
    p4_opponent_rank = player_elos[p1] + player_elos[p2] - player_elos[p3]

    #Calculating expected game outcome for each player
    E1 = expected_score(player_elos[p1], p1_opponent_rank)
    E2 = expected_score(player_elos[p2], p2_opponent_rank)
    E3 = expected_score(player_elos[p3], p3_opponent_rank)
    E4 = expected_score(player_elos[p4], p4_opponent_rank)

    if won:
        player_elos[p1] = player_elos[p1] + K_VALUE * (1 - E1)
        player_elos[p2] = player_elos[p2] + K_VALUE * (1 - E2)
        player_elos[p3] = player_elos[p3] + K_VALUE * (0 - E3)
        player_elos[p4] = player_elos[p4] + K_VALUE * (0 - E4)
    else:
        player_elos[p1] = player_elos[p1] + K_VALUE * (0 - E1)
        player_elos[p2] = player_elos[p2] + K_VALUE * (0 - E2)
        player_elos[p3] = player_elos[p3] + K_VALUE * (1 - E3)
        player_elos[p4] = player_elos[p4] + K_VALUE * (1 - E4)


def expected_score(Ra, Rb):
    return 1 / (1 + math.pow(10, (Rb - Ra) / 400))


if __name__ == '__main__':
    games = DataHandler.read_data()
    timeline = compile_elos(games)
    players = list(timeline[0].keys())
    data = []

    for player in players:
        for i in range(len(timeline)):
            data.append((i, timeline[i][player]))
        GraphDrawer.draw_graph(data, player)
        data.clear()

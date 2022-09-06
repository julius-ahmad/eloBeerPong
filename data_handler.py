def read_data():
    """
    reads data from the games.txt file keeps players in order as we have 2v2 matches
    @return: a list of tuples of players who played in a game and who won (number represents if 2 left players won)
    """
    with open('games.txt') as f:
        games = [game.split() for game in (line.strip() for line in f.readlines())]
    f.close()

    games = [(game[:4], game[4]) for game in games]

    return games

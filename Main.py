import GraphDrawer


def read_data():
    """
    reads data from the games.txt file
    @return: a dictionary of some sort -> not sure how to store the data atm
    """
    with open('games.txt') as f:
        games = [game.split() for game in (line.strip() for line in f.readlines())]
    f.close()

    return


if __name__ == '__main__':
    read_data()
    # data = []
    #
    # GraphDrawer.draw_graph(data)

# dominio.py é basicamente o cidades.py

from tree_search import SearchProblem, SearchTree, SearchDomain
from commonMAIS import Map, Coordinates


class Dominio():  # adicionar depois o SearchDomain entre os ()
    def __init__(self, mapa: Map):
        self.initial_map = mapa

    def actions(self, mapa):  # -> set[tuple[str,str]]:
        carros = set()

        for x, y, piece in mapa.coordinates:

            if piece != 'x':

                for i in mapa.car_actions(piece):
                    carros.add(i)

        return carros

    def result_two(self, mapa, action):
        ''' Returns the state (Map) that results from executing the given action '''

        piece = action[0]
        act = action[1]

        if act == 'a':
            vector_coordinates = Coordinates(-1, 0)
        elif act == 'd':
            vector_coordinates = Coordinates(1, 0)
        elif act == 's':
            vector_coordinates = Coordinates(0, 1)
        elif act == 'w':
            vector_coordinates = Coordinates(0, -1)

        return mapa.move_two(piece, vector_coordinates)


    def heuristic(self, mapa):
        list_coordinates = mapa.piece_coordinates("A")
        return mapa.grid_size - list_coordinates[-1].x

    def satisfies(self, mapa):
        return mapa.test_win()

# # Atalho para obter caminho de c1 para c2 usando strategy:


def search_path(strategy, grid):
    mapa = Map(grid)
    dom = Dominio(mapa)
    my_prob = SearchProblem(dom)
    my_tree = SearchTree(my_prob, strategy)
    return my_tree.search()

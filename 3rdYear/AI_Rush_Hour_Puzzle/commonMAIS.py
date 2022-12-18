"""Common data structures. Can be used by any module."""
from __future__ import annotations
import math
from dataclasses import dataclass


@dataclass
class Coordinates:
    """Coordinates data class."""

    x: int
    y: int


class MapException(Exception):
    """Exception Moving Pieces."""


class Map:
    """Representation of a map."""

    empty_tile = "o"
    wall_tile = "x"
    player_car = "A"

    def __init__(self, txt: str):
        """Initialize Map from string."""
        pieces, grid, movements = txt.split(" ")
        self.pieces = int(pieces)  # quantidade de peças
        self.movements = int(movements)  # pontos
        self.grid_size = int(math.sqrt(len(grid)))
        self.grid_string = grid
        self.grid = []

        line = []
        for i, pos in enumerate(grid):
            line.append(pos)  # pos = cada peça da grid
            if (i + 1) % self.grid_size == 0:
                self.grid.append(line)  # line = cada linha horizontal da grid
                line = []

    def __repr__(self):
        """Revert map object to string."""

        mapToString = []
        for i in self.grid:
            mapToString += i
        raw = "".join(mapToString)

        return f"{self.pieces} {raw} {self.movements}"

    @property
    def coordinates(self):
        """Representation of ocupied map positions through tuples x,y,value."""

        return [(x, y, column) for y, line in enumerate(self.grid) for x, column in enumerate(line) if column != self.empty_tile]

    def get(self, cursor: Coordinates):
        """Return piece at cursor position."""
        if 0 <= cursor.x < self.grid_size and 0 <= cursor.y < self.grid_size:
            return self.grid[int(cursor.y)][int(cursor.x)]
        raise MapException("Out of the grid")

    def piece_coordinates(self, piece: str):
        """List coordinates holding a piece."""
        return [Coordinates(x, y) for y, line in enumerate(self.grid) for x, column in enumerate(line) if column == piece]

    def move(self, piece: str, direction: Coordinates):
        """Move piece in direction fiven by a vector."""
        if piece == self.wall_tile:
            raise MapException("Blocked piece")

        piece_coord = self.piece_coordinates(piece)
        # Don't move vertical pieces sideways
        if direction.x != 0 and any([line.count(piece) == 1 for line in self.grid]):
            raise MapException("Can't move sideways")
        # Don't move horizontal pieces up-down
        if direction.y != 0 and any([line.count(piece) > 1 for line in self.grid]):
            raise MapException("Can't move up-down")

        def sum(a: Coordinates, b: Coordinates):
            return Coordinates(a.x + b.x, a.y + b.y)

        for pos in piece_coord:
            if not self.get(sum(pos, direction)) in [piece, self.empty_tile]:
                raise MapException("Blocked piece")

        for pos in piece_coord:
            self.grid[pos.y][pos.x] = self.empty_tile

        for pos in piece_coord:
            new_pos = sum(pos, direction)
            self.grid[new_pos.y][new_pos.x] = piece

    def test_win(self):
        """Test if player_car has crossed the left most column."""
        return any([c.x == self.grid_size - 1 for c in self.piece_coordinates(self.player_car)])

###############Editado por nós###########################################

    def car_actions(self, piece: str) -> list[tuple[str, str]]:
        orientation = self.get_car_orientation(piece)
        action_list = []

        if orientation == 'h':
            extremo_esquerda = self.grid_string.find(piece)
            extremo_direita = self.grid_string.rfind(piece)
            if extremo_esquerda % self.grid_size != 0:
                a_esquerda = extremo_esquerda - 1
                if self.grid_string[a_esquerda] == 'o':
                    action_list.append((piece, 'a'))

            if (extremo_direita+1) % (self.grid_size) != 0:
                a_direita = extremo_direita + 1
                if self.grid_string[a_direita] == 'o':
                    action_list.append((piece, 'd'))

        else:
            extremo_cima = self.grid_string.find(piece)
            extremo_baixo = self.grid_string.rfind(piece)
            if extremo_cima >= self.grid_size:
                a_cima = extremo_cima - self.grid_size
                if self.grid_string[a_cima] == 'o':
                    action_list.append((piece, 'w'))

            if extremo_baixo < self.grid_size**2 - self.grid_size:
                a_baixo = extremo_baixo + self.grid_size
                if self.grid_string[a_baixo] == 'o':
                    action_list.append((piece, 's'))

        return action_list

    def get_car_orientation(self, piece: str) -> str:
        first: int = self.grid_string.find(piece)
        if self.grid_string[first + 1] != piece:
            return "v"
        return "h"

    def move_two(self, piece: str, direction: Coordinates):
        """Move piece in direction fiven by a vector."""
        if piece == self.wall_tile:
            raise MapException("Blocked piece")
       
        piece_coord = self.piece_coordinates(piece)
        # Don't move vertical pieces sideways
        if direction.x != 0 and any([line.count(piece) == 1 for line in self.grid]):
            raise MapException("Can't move sideways")
        
        # Don't move horizontal pieces up-down
        if direction.y != 0 and any([line.count(piece) > 1 for line in self.grid]):
            raise MapException("Can't move up-down")


        self.new_grid_string = self.grid_string

        def sum(a: Coordinates, b: Coordinates):
            return Coordinates(a.x + b.x, a.y + b.y)
        
        for pos in piece_coord:
            if not self.get(sum(pos, direction)) in [piece, self.empty_tile]:
                raise MapException("Blocked piece")
                
        for pos in piece_coord:
            self.new_grid_string = self.new_grid_string[:(
                self.grid_size*pos.y+pos.x)] + self.empty_tile + self.new_grid_string[(self.grid_size*pos.y+pos.x) + 1:]

        for pos in piece_coord:
            new_pos = sum(pos, direction)
            self.new_grid_string = self.new_grid_string[:(
                self.grid_size*new_pos.y+new_pos.x)] + piece + self.new_grid_string[(self.grid_size*new_pos.y+new_pos.x) + 1:]

        return self.new_grid_string

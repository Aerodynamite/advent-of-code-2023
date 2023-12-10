from dataclasses import dataclass

filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()


@dataclass
class XY:
    x: int
    y: int


NORTH = XY(-1, 0)
EAST = XY(0, 1)
SOUTH = XY(1, 0)
WEST = XY(0, -1)


class Tile:
    def __init__(self, shape, x_coord: int, y_coord: int):
        self.shape = shape
        self.x = x_coord
        self.y = y_coord
        self.is_pipe = True

        if shape == "|":
            self.possible_neighbours = [NORTH, SOUTH]
        elif shape == "-":
            self.possible_neighbours = [EAST, WEST]
        elif shape == "L":
            self.possible_neighbours = [NORTH, EAST]
        elif shape == "J":
            self.possible_neighbours = [NORTH, WEST]
        elif shape == "7":
            self.possible_neighbours = [SOUTH, WEST]
        elif shape == "F":
            self.possible_neighbours = [SOUTH, EAST]
        elif shape == "S":
            self.possible_neighbours = [NORTH, EAST, SOUTH, WEST]
        else:
            self.is_pipe = False
            self.possible_neighbours = []

    def __str__(self):
        return f"{self.shape} ({self.x}, {self.y})"


# find starting position
# from there, get possible neighbours
# follow one path
# repeat until back at starting position
tiles = []
starting_tile = None
for x in range(len(content)):
    tiles.append([])
    for y in range(len(content[x])):
        tiles[x].append(Tile(content[x][y], x, y))
        if content[x][y] == "S":
            starting_tile = XY(x, y)


def get_new_coords(current: XY, diff: XY):
    return XY(current.x + diff.x, current.y + diff.y)


current_tile = tiles[starting_tile.x][starting_tile.y]
previous_tile = None
back_at_start = False
path_length = 0
while not back_at_start:
    print(current_tile)
    neighbour_coords = [get_new_coords(current_tile, diff)
                        for diff
                        in tiles[current_tile.x][current_tile.y].possible_neighbours]
    for neighbour_coord in neighbour_coords:
        neighbour_tile = tiles[neighbour_coord.x][neighbour_coord.y]
        if not neighbour_tile.is_pipe:
            continue

        if neighbour_tile != previous_tile:
            next_tile = neighbour_tile
            previous_tile = current_tile
            current_tile = next_tile
            path_length += 1

            if current_tile.shape == "S":
                back_at_start = True
            break

print("Result =", path_length / 2)


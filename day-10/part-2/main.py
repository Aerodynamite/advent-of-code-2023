from dataclasses import dataclass

filename = "sample2.txt"
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
        self.part_of_loop = False
        self.is_corner = True

        if shape == "|":
            self.possible_neighbours = [NORTH, SOUTH]
            self.is_corner = False
        elif shape == "-":
            self.possible_neighbours = [EAST, WEST]
            self.is_corner = False
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
starting_tile.part_of_loop = True


def get_new_coords(current: XY, diff: XY):
    return XY(current.x + diff.x, current.y + diff.y)


current_tile = tiles[starting_tile.x][starting_tile.y]
previous_tile = None
back_at_start = False
while not back_at_start:
    # print(current_tile)
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
            current_tile.part_of_loop = True

            if current_tile.shape == "S":
                back_at_start = True
            break

def print_loop():
    for row in tiles:
        for tile in row:
            if tile.part_of_loop:
                print(tile.shape, end='')
            else:
                print(".", end='')
        print("")

# print_loop()


# def in_loop(pipes_encountered, corner_sections_encountered):
#     if pipes_encountered:
#         pipes_encountered += corner_sections_encountered
#     else:
#         return False
#
#     return pipes_encountered % 2 != 0



num_enclosed = 0
enclosed_tiles = []
for x in range(len(tiles)):
    for y in range(len(tiles[x])):
        tile = tiles[x][y]
        if tile.part_of_loop:
           continue

        # cast ray to the right
        in_loop = False
        corner_sections_encountered = 0
        encountered_corner = False
        corner = None
        for i in range(0, y+1):
            ray_tile = tiles[x][i]
            if ray_tile.part_of_loop and ray_tile.shape == "|":
                in_loop = not in_loop
            elif ray_tile.part_of_loop and encountered_corner and ray_tile.shape == "-":
                continue
            elif ray_tile.part_of_loop and not encountered_corner and ray_tile.is_corner:
                encountered_corner = True
                corner = ray_tile.shape
            elif ray_tile.part_of_loop and encountered_corner and ray_tile.is_corner:
                encountered_corner = False
                other_corner = ray_tile.shape
                if (corner == "F" and other_corner == "J") or (corner == "L" and other_corner == "7") :
                    in_loop = not in_loop

        if in_loop:
            num_enclosed += 1
            enclosed_tiles.append(tile)

for x in enclosed_tiles:
    print(x)
print(num_enclosed)

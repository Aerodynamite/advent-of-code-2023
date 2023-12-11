import math

filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

EMPTY = "."
GALAXY = "#"


def pivot(image, times=1):
    result = image
    for i in range(times):
        result = [list(reversed(x)) for x in zip(*result)]
    return result

def expand_1d(image):
    expanded_galaxy = []
    for i, row in enumerate(image):
        split = row.copy()
        expanded_galaxy.append(split)
        if all(x == EMPTY for x in split):
            expanded_galaxy.append(split.copy())
    return expanded_galaxy


def expand_2d(galaxy):
    hor_expanded = expand_1d(galaxy)
    pivoted = pivot(hor_expanded)
    ver_expanded = expand_1d(pivoted)
    return pivot(ver_expanded, 3)


def print_image(image):
    for row in image:
        for col in row:
            print(col, end="")
        print("")


def find_galaxies(galaxy):
    galaxy_locations = []
    for i, row in enumerate(galaxy):
        for j, val in enumerate(row):
            if val == GALAXY:
                galaxy_locations.append((i, j))
    return galaxy_locations

# def distance(galaxy_1, galaxy_2):


image = []
for row in content:
    new_row = []
    for col in row:
        new_row.append(col)
    image.append(new_row)

expanded_image = expand_2d(image)
# print_image(expanded_image)
galaxy_locations = find_galaxies(expanded_image)
# print(galaxy_locations)
sum = 0
for i, galaxy in enumerate(galaxy_locations):
    for j in range(i, len(galaxy_locations)):
        other = galaxy_locations[j]

        # distance = math.sqrt( pow(other[0] - galaxy[0], 2) + pow(other[1] - galaxy[1], 2) )
        distance = abs(other[0] - galaxy[0]) + abs(other[1] - galaxy[1])
        # print(galaxy, other, distance)

        sum += distance

print(sum)
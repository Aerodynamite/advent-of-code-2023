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

def get_empty_rows(image):
    empty_row_ids = []
    for i, row in enumerate(image):
        if all(x == EMPTY for x in row):
            empty_row_ids.append(i)
    return empty_row_ids


def get_empty_rows_cols(image):
    empty_rows = get_empty_rows(image)
    pivoted = pivot(image)
    empty_cols = get_empty_rows(pivoted)
    return (empty_rows, empty_cols)


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

def process_input(input):
    image = []
    for row in input:
        new_row = []
        for col in row:
            new_row.append(col)
        image.append(new_row)
    return image

EXPANSION_FACTOR = 999999
def get_diff(i, j, empty_lines):
    diff = abs(j - i)
    for line in empty_lines:
        if i < line < j or j < line < i:
            diff += EXPANSION_FACTOR
    return diff

image = process_input(content)

empty_rows_cols = get_empty_rows_cols(image)
empty_rows = empty_rows_cols[0]
empty_cols = empty_rows_cols[1]
galaxy_locations = find_galaxies(image)


sum = 0
for i, galaxy in enumerate(galaxy_locations):
    for j in range(i + 1, len(galaxy_locations)):
        other = galaxy_locations[j]

        distance = get_diff(galaxy[0], other[0], empty_rows) + get_diff(galaxy[1], other[1], empty_cols)
        # distance = abs(other[0] - galaxy[0]) + abs(other[1] - galaxy[1])
        print(i+1, j+1, distance)

        sum += distance

print(sum)
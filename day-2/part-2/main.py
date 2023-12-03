filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

RED = 'red'
GREEN = 'green'
BLUE = 'blue'

id_sum = 0

for line in content:
    # print(line)
    game = line.split(':')
    game_id = int(game[0].split(' ')[1])
    rounds = game[1].strip().split(';')

    found_impossible_round = False

    for round in rounds:
        cubes = round.strip().split(',')
        for cube in cubes:
            parts = cube.strip().split(' ')
            amount = int(parts[0])
            color = parts[1]
            impossible = ((color == RED and amount > MAX_RED)
                          or (color == GREEN and amount > MAX_GREEN)
                          or (color == BLUE and amount > MAX_BLUE))

            found_impossible_round = found_impossible_round or impossible

    if not found_impossible_round:
        # print(game_id)
        id_sum += game_id

print(id_sum)
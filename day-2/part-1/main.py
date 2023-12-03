filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()


RED = 'red'
GREEN = 'green'
BLUE = 'blue'

power_sum = 0

for line in content:
    print(line)
    game = line.split(':')
    game_id = int(game[0].split(' ')[1])
    rounds = game[1].strip().split(';')

    amounts = {
        'red': 0,
        'green': 0,
        'blue': 0
    }

    for round in rounds:
        cubes = round.strip().split(',')
        for cube in cubes:
            parts = cube.strip().split(' ')
            amount = int(parts[0])
            color = parts[1]

            amounts[color] = amount if amount > amounts[color] else amounts[color]

        power = amounts[RED] * amounts[GREEN] * amounts[BLUE]
        print(power)


    power_sum += power

print(power_sum)
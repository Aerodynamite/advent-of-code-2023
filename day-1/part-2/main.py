filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

numbers = {
    '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
}

sum = 0

for line in content:
    first = None
    last = None
    current = None
    builder = ""
    for i in range(0, len(line)):
        builder += line[i]
        for key in numbers.keys():
            if key in builder:
                current = numbers[key]
                if first is None:
                    first = current

                builder = builder[-1:]

    last = current
    sum += int(f"{first}{last}")
    print(line, first, last, sum)

print(sum)

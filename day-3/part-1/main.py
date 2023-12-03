import copy

filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

engine = content
has_adjacent_symbol_lookup = []

numbers_with_coords = []

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
not_symbols = ['.'] + numbers

clean_engine = []


def has_adjacent_symbol(engine, row, column):
    adjacent_offsets = [-1, 0, 1]

    for row_offset in adjacent_offsets:
        for col_offset in adjacent_offsets:
            row_index = row + row_offset
            col_index = column + col_offset
            if 0 <= row_index < len(engine) and 0 <= col_index < len(engine[0]):
                try:
                    is_symbol = engine[row_index][col_index] not in not_symbols
                except:
                    print(len(engine[0]), row_index, col_index)
                if is_symbol:
                    return True
    return False


def is_adjacent(x_1, y_1, x_2, y_2) -> bool:
    return -1 <= x_1 - x_2 <= 1 and -1 <= y_1 - y_2 <= 1


def combine_adjacent_numbers(numbers_with_coords):
    result = []
    for row in numbers_with_coords:
        new_number_with_coords = {'number': 0, 'coords': []}
        for set in row:
            number = int(f"{new_number_with_coords['number']}{set['number']}")
            new_number_with_coords['number'] = number
            new_number_with_coords['coords'].append(set['coord'])

        result.append(new_number_with_coords)
    return result


for row in range(0, len(engine)):
    has_adjacent_symbol_lookup.append([])
    buffer = []
    for column in range(0, len(engine[row])):
        has_adjacent_symbol_lookup[row].append(has_adjacent_symbol(engine, row, column))
        current = engine[row][column]
        if current in numbers:
            buffer.append({'number': current, 'coord': {'row': row, 'column': column}})
        elif len(buffer) != 0:
            numbers_with_coords.append(buffer)
            buffer = []
    if len(buffer) != 0:
        numbers_with_coords.append(buffer)

number_with_coords = combine_adjacent_numbers(numbers_with_coords)
# for x in number_with_coords:
#     print(x)

f = open("lookup.txt", "w")
buffer = ""
for row in has_adjacent_symbol_lookup:
    for col in row:
        buffer += "X" if col else "."
    buffer += "\n"
f.write(buffer)
f.close()

sum = 0
for number in number_with_coords:
    for coord in number['coords']:
        if has_adjacent_symbol_lookup[coord['row']][coord['column']]:
            sum += number['number']
            # print("Adding ", number['number'], "for", coord['row'], coord['column'])
            break

print(sum)

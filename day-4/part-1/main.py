filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

# numbers = []
sum = 0

for line in content:
    parts = line.split(":")

    number_parts = parts[1].strip().split("|")
    winning_numbers = list(filter(lambda x: x != "", [x.strip() for x in number_parts[0].strip().split(" ")]))
    my_numbers = list(filter(lambda x: x != "", [x.strip() for x in number_parts[1].strip().split(" ")]))

    # numbers.append({"winning": winning_numbers, "my": my_numbers})

    num_matches = 0
    for mine in my_numbers:
        if mine in winning_numbers:
            num_matches += 1
    if num_matches > 0:
        points = pow(2, num_matches-1)
        # print("This card is ", points, "points")
        sum += points

print(sum)
# print(numbers)
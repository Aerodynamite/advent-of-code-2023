filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

sum = 0

# Display the content.
for line in content:
    first = None
    last = None
    current = None
    for i in range(0, len(line)):
        if line[i] in numbers:
            current = line[i]
            if first is None:
                first = current
    last = current
    print(first, last)
    sum += int(f"{first}{last}")

print(sum)

filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

START = "AAA"
END = "ZZZ"

instructions = content[0]
network = content[2:]

left_map = {}
right_map = {}

for line in network:
    parts = line.split(" = ")
    key = parts[0]
    
    nodes = parts[1][1:-1].split(", ")
    left = nodes[0]
    right = nodes[1]
    
    left_map[key] = left
    right_map[key] = right
    
# print(left_map)
# print(right_map)

current_node = START
steps_taken = 0

while current_node != END:
    for direction in instructions:
        if direction == "L":
            current_node = left_map[current_node]
        elif direction == "R":
            current_node = right_map[current_node]
        else:
            print("WHAT")
        
        steps_taken += 1
        
print(steps_taken)
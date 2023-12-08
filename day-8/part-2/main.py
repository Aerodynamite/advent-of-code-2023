import math

filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

START = "A"
END = "Z"

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
    

starting_nodes = [x for x in left_map.keys() if x.endswith(START)]
print(starting_nodes)


finished_node_in_steps = [0 for x in starting_nodes]

for i in range(0, len(starting_nodes)):
    current_node = starting_nodes[i]
    steps_taken = 0
    
    while not current_node.endswith(END):
        for direction in instructions:
            if direction == "L":
                current_node = left_map[current_node]
            elif direction == "R":
                current_node = right_map[current_node]
            else:
                print("WHAT")
    
            steps_taken += 1
    
    finished_node_in_steps[i] = steps_taken

print(finished_node_in_steps)

print(math.lcm(*finished_node_in_steps))  # Inspired by reddit, because brute-force didn't work (:

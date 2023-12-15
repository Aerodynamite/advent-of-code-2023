filename = "input.txt"
with open(filename) as f:
    inputs = f.read().split(",")

def hash(value):
    hash = 0
    for char in value:
        hash += ord(char)
        hash *= 17
        hash = hash % 256
    return hash

hashed = sum([hash(x) for x in inputs])
print(hashed)
filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

times = [int(x) for x in content[0].split(":")[1].split(" ") if x != ""]
distance = [int(x) for x in content[1].split(":")[1].split(" ") if x != ""]

result = 1

for i in range(0, len(times)):
    race_duration = times[i]
    record_distance = distance[i]

    winning_ways = 0
    for hold in range(0, race_duration + 1):
        distance_traveled = hold * (race_duration - hold)
        if distance_traveled > record_distance:
            winning_ways += 1

    result *= winning_ways

print(result)
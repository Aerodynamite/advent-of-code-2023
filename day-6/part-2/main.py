filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

times = [x for x in content[0].split(":")[1].split(" ") if x != ""]
distances = [x for x in content[1].split(":")[1].split(" ") if x != ""]

race_duration = ""
for x in times:
    race_duration += x
race_duration = int(race_duration)

record_distance = ""
for x in distances:
    record_distance += x
record_distance = int(record_distance)


winning_ways = 0
for hold in range(0, race_duration + 1):
    if hold % 1000000 == 0:
        print(".", end='')
    distance_traveled = hold * (race_duration - hold)
    if distance_traveled > record_distance:
        winning_ways += 1


print(winning_ways)
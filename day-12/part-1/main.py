filename = "input2.txt"
with open(filename) as f:
    content = f.read().splitlines()

import itertools

BROKEN = "#"
UNKNOWN = "?"
WORKING = "."
class ConditionRecord:

    def __init__(self, line):
        self.damaged_record = line.split(" ")[0]
        self.spring_arrangements = [int(x) for x in line.split(" ")[1].split(",")]

    def calculate_possible_arrangements(self):
        total_springs = sum(self.spring_arrangements)
        known_broken_springs = self.damaged_record.count(BROKEN)

        remaining_springs = total_springs - known_broken_springs
        unknown_locations = len([i for i, letter in enumerate(self.damaged_record) if letter == UNKNOWN])
        working_springs = unknown_locations - remaining_springs

        elements = [BROKEN for x in range(remaining_springs)] + [WORKING for x in range(working_springs)]
        print(elements)
        permutations = set(itertools.permutations(elements))

        num_matches = 0
        for permutation in permutations:
            fixes = "".join(permutation)
            print("Fixes", fixes)
            fixed_record = self._fix_damaged_record(fixes)
            # print(fixed_record)
            if self._matches_arrangement(fixed_record):
                num_matches += 1

        return num_matches

    def _fix_damaged_record(self, fixes):
        fixed_record = self.damaged_record
        for i, thing in enumerate(self.damaged_record):
            if thing != UNKNOWN:
                continue

            fixed_record = fixed_record[:i] + fixes[0] + fixed_record[i+1:]
            fixes = fixes[1:]

        return fixed_record

    def _matches_arrangement(self, record: str):
        remaining_record = record

        for num in self.spring_arrangements:
            if not remaining_record:
                return False

            while remaining_record[0] == WORKING:
                remaining_record = remaining_record[1:]

            springs = num * BROKEN
            if remaining_record.startswith(springs + WORKING) or remaining_record == springs:
                remaining_record = remaining_record[len(springs + WORKING):]
                continue

            return False

        return len(remaining_record) == 0 or all(x == WORKING for x in remaining_record)


sum_possible_arrangements = 0
for i, record in enumerate(content):
    condition = ConditionRecord(record)
    sum_possible_arrangements += condition.calculate_possible_arrangements()

    if i % 10 == 0:
        print(".", end="")

print("")
print(sum_possible_arrangements)
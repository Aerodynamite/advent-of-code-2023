filename = "sample.txt"
with open(filename) as f:
    content = f.read().splitlines()


BROKEN = "#"
UNKNOWN = "?"
WORKING = "."
MULTIPLIER = 5
class ConditionRecord:

    def __init__(self, line):
        self.damaged_record = (line.split(" ")[0] + UNKNOWN) * MULTIPLIER
        arrangement = [int(x) for x in line.split(" ")[1].split(",")]
        self.spring_arrangements = []
        for r in range(MULTIPLIER):
            self.spring_arrangements += arrangement

        # print(self.damaged_record)
        # print(self.spring_arrangements)

    def calculate_possible_arrangements(self):
        return self._find_matches(self.damaged_record)

    def _find_matches(self, remaining_record, record_builder="", matches=0):
        if len(record_builder) == len(self.damaged_record):
            return 1 if self._matches_arrangement(record_builder) else 0

        if len(remaining_record) == 0:
            return 0

        if remaining_record[0] == UNKNOWN:
            matches += self._find_matches(remaining_record[1:], record_builder + BROKEN)
            matches += self._find_matches(remaining_record[1:], record_builder + WORKING)
            return matches

        return self._find_matches(remaining_record[1:], record_builder + remaining_record[0], matches)

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

            while len(remaining_record) and remaining_record[0] == WORKING:
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
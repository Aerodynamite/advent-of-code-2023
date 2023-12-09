filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

history = [line.split(" ") for line in content]


class OasisReport:
    def __init__(self, readings: list[str]):
        self.readings = [int(x) for x in readings]

    def predict_previous_value(self):
        current_level = self.readings
        first_numbers = []
        first_numbers.append(current_level[0])
        while not self._all_zero(current_level):
            diffs = []
            for i in range(len(current_level) - 1):
                diffs.append(current_level[i+1] - current_level[i])

            current_level = diffs
            first_numbers.append(current_level[0])
        first_numbers.reverse()
        # print(first_numbers)
        previous_value = 0
        for val in first_numbers[1:]:
            # print(val, previous_value)
            previous_value = val - previous_value
        return previous_value

    def _all_zero(self, diffs):
        return all(diff == 0 for diff in diffs)


reports = [OasisReport(reading) for reading in history]
sum = 0
for report in reports:
    sum += report.predict_previous_value()

print(sum)
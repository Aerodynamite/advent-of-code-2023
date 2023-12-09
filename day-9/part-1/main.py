filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()

history = [line.split(" ") for line in content]


class OasisReport:
    def __init__(self, readings: list[str]):
        self.readings = [int(x) for x in readings]

    def predict_next_value(self):
        current_level = self.readings
        last_numbers = []
        last_numbers.append(current_level[-1])
        while not self._all_zero(current_level):
            diffs = []
            for i in range(len(current_level) - 1):
                diffs.append(current_level[i+1] - current_level[i])

            current_level = diffs
            last_numbers.append(current_level[-1])
        # print(last_numbers)
        last_numbers.reverse()
        sum = 0
        for i in range(1, len(last_numbers)):
            sum += last_numbers[i]
            # print(sum)
        return sum

    def _all_zero(self, diffs):
        return all(diff == 0 for diff in diffs)


reports = [OasisReport(reading) for reading in history]
sum = 0
for report in reports:
    sum += report.predict_next_value()

print(sum)
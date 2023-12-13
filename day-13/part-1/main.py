filename = "input.txt"
with open(filename) as f:
    content = f.read().split("\n\n")

import numpy as np

class Pattern:
    def __init__(self, input):
        self.pattern = []
        for pattern_row in input.split("\n"):
            columns = [x for x in pattern_row]
            self.pattern.append(columns)

        # print(self.pattern)

    def get_num_lines_left_of_vertical_reflection(self):
        # print(self.pattern)
        arr = np.array(self.pattern)
        transposed = np.transpose(arr)
        # print(transposed.tolist())
        return self._get_num_lines_above_horizontal_reflection(transposed.tolist())

    def get_num_lines_above_horizontal_reflection(self):
        return self._get_num_lines_above_horizontal_reflection(self.pattern)

    def _get_num_lines_above_horizontal_reflection(self, pattern):
        for i, row in enumerate(pattern):
            if i < len(pattern) - 1 and row == pattern[i + 1]:
                # Found a matching row, reverse what we have until now and see if it matches the next rows as well
                rows = pattern[:i+1]
                rows.reverse()
                other = pattern[i+1:]
                # print(rows, other)
                if self._are_rows_equal(rows, other):
                    return i + 1

        return None

    def _are_rows_equal(self, rows, other):
        min_len = min(len(rows), len(other))
        for i in range(min_len):
            if rows[i] != other[i]:
                return False
        return True



patterns = [Pattern(input) for input in content]

vertical_reflections = [pattern.get_num_lines_left_of_vertical_reflection() for pattern in patterns]
horizontal_reflections = [pattern.get_num_lines_above_horizontal_reflection() for pattern in patterns]

# print(horizontal_reflections)
# print(vertical_reflections)

sum_columns = sum([x for x in vertical_reflections if x is not None])
sum_rows = sum([100 * x for x in horizontal_reflections if x is not None])

print(sum_columns + sum_rows)
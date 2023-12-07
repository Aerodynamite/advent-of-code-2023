filename = "input.txt"
with open(filename) as f:
    content = f.read().splitlines()


class Hand:
    _CARD_MAPPING = {
        'A': 14,
        'K': 13,
        'Q': 12,
        'T': 11,
        '9': 10,
        '8': 9,
        '7': 8,
        '6': 7,
        '5': 6,
        '4': 5,
        '3': 4,
        '2': 3,
        'J': 2
    }
    rank = 0

    def __init__(self, line):
        parts = line.split(" ")
        self.cards = [self._CARD_MAPPING[card] for card in parts[0]]
        self.bid = int(parts[1])
        self._determine_score()

    def _determine_score(self):
        card_count = {}
        jokers = 0
        for card in self.cards:
            if card == 2:
                jokers += 1
                continue

            if card in card_count:
                card_count[card] += 1
            else:
                card_count[card] = 1

        sorted_counts = sorted(card_count.values(), reverse=True)
        if len(sorted_counts) > 0:
            sorted_counts[0] += jokers
        else:
            sorted_counts.append(jokers)

        if sorted_counts == [5]:
            self.score = [7]
        elif sorted_counts == [4, 1]:
            self.score = [6]
        elif sorted_counts == [3, 2]:
            self.score = [5]
        elif sorted_counts == [3, 1, 1]:
            self.score = [4]
        elif sorted_counts == [2, 2, 1]:
            self.score = [3]
        elif sorted_counts == [2, 1, 1, 1]:
            self.score = [2]
        elif sorted_counts == [1, 1, 1, 1, 1]:
            self.score = [1]

        self.score = self.score + self.cards

    def __lt__(self, other):
        for i in range(0, len(self.score)):
            if self.score[i] == other.score[i]:
                continue

            if self.score[i] < other.score[i]:
                return True

            return False


def calculate_total_winnings(input):
    hands = [Hand(line) for line in input]
    hands.sort()

    total_winnings = 0
    for i in range(0, len(hands)):
        rank = i + 1
        total_winnings += hands[i].bid * rank

    return total_winnings


print(calculate_total_winnings(content))

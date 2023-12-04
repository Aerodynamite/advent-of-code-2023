class Scratchcard:
    def __init__(self, card_id: str, winning_numbers: [str], my_numbers: [str]):
        self.card_id = int(card_id)
        self.winning_numbers = winning_numbers
        self.my_numbers = my_numbers

    def __str__(self):
        return f"Card {self.card_id}"

def parse_scratchcards(input):
    original_scratchcards = []
    for line in input:
        parts = line.split(":")

        id = [x.strip() for x in parts[0].strip().split(" ") if x != ""][1]
        number_parts = parts[1].strip().split("|")
        winning_numbers = list(filter(lambda x: x != "", [x.strip() for x in number_parts[0].strip().split(" ")]))
        my_numbers = list(filter(lambda x: x != "", [x.strip() for x in number_parts[1].strip().split(" ")]))
        original_scratchcards.append(Scratchcard(id, winning_numbers, my_numbers))
    return  original_scratchcards


def get_number_of_scratchcards(scratchcards: [Scratchcard], full_set: [Scratchcard]) -> int:
    amount = len(scratchcards)
    for i in range(0, len(scratchcards)):
        card = scratchcards[i]
        num_matches = 0
        for number in card.my_numbers:
            if number in card.winning_numbers:
                num_matches += 1
        # print(num_matches)
        if num_matches > 0:
            to_copy_ids = range(card.card_id, card.card_id + num_matches)
            copies = []
            for to_copy_id in to_copy_ids:
                # print("Copying", to_copy_id)
                # print(full_set[to_copy_id])
                copies.append(full_set[to_copy_id])
            amount += get_number_of_scratchcards(copies, full_set)
    print(amount)
    return amount


def run():
    filename = "input.txt"
    with open(filename) as f:
        content = f.read().splitlines()

    originals = parse_scratchcards(content)

    return get_number_of_scratchcards(originals, originals)


print(run())

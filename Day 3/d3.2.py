import sys
from pathlib import Path
import string


def ruck_sack(input):
    rucksack_items = input.split("\n")

    alphabet = string.ascii_letters
    priority = {}
    sum = 0
    group_value = []

    for i in range(len(alphabet)):
        priority[alphabet[i]] = i + 1

    for item in range(0, len(rucksack_items), 3):
        for letter in rucksack_items[item]:
            if letter in rucksack_items[item + 1]:
                if letter in rucksack_items[item + 2]:
                    sum += priority[letter]
                    break
    print(sum)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        ruck_sack(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

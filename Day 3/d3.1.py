import sys
from pathlib import Path


def ruck_sack(input):
    rucksack_items = input.split("\n")

    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priority = {}
    sum = 0

    for i in range(len(alphabet)):
        priority[alphabet[i]] = i + 1

    for items in rucksack_items:
        left_half, right_half = items[:len(items)//2], items[len(items)//2:]
        for item in left_half:
            if item in right_half:
                sum += priority[item]
                break

    print(sum)

    # split in left half and right half
    # nested for loop if each letter in left half is in right half


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        ruck_sack(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

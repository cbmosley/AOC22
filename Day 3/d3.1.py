import sys
from pathlib import Path


def ruck_sack(input):
    rucksack_items = input.split("\n")
    compartment_one = []
    compartment_two = []
    for ruck in rucksack_items:
        first_half, second_half = ruck[:len(
            ruck)/2], ruck[len(ruck)//2:]
        
        
            


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        ruck_sack(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

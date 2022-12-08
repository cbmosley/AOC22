import sys
from pathlib import Path
import re


def clean_up(input):
    data = input.split('\n')
    count = 0
    for i in data:
        revised_data = re.sub('\D', ' ', i)
        section_data = list(map(int, revised_data.split()))
        group_one = set(range(section_data[0], section_data[1]+1))
        group_two = set(range(section_data[2], section_data[3]+1))
        if group_one.intersection(group_two):
            count += 1
    print(count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        clean_up(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

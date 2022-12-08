import sys
from pathlib import Path
import re


def clean_up(input):
    data = input.replace("-", ",")
    revised_data = data.replace("\n", ",")
    section_data = revised_data.split(",")
    pair_count = 0
    for i in range(0, (len(section_data))//4):
        if section_data[i] <= section_data[i + 2] and section_data[i + 1] >= section_data[i + 3] or section_data[i] >= section_data[i + 2] and section_data[i + 1] <= section_data[i + 3]:
            pair_count += 1
    print(pair_count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        clean_up(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

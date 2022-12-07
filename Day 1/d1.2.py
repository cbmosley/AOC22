import sys
from pathlib import Path


def most_calories(input):
    calories = input.split('\n')
    cal_count = 0
    elf_total = []
    for cals in calories:
        if cals != "":
            cal_count += int(cals)
        if cals == "":
            elf_total.append(cal_count)
            cal_count = 0
    elf_total.sort()
    top_three = elf_total[-3:]
    total_top_three = 0
    for elf in top_three:
        total_top_three += elf
    print(top_three)
    print(total_top_three)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        most_calories(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

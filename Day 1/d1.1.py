import sys
from pathlib import Path


def MostCalories(input):
    calories = input.split('\n')
    cal_count = 0
    elf_total = []
    for cals in calories:
        if cals != "":
            cal_count += int(cals)
        if cals == "":
            elf_total.append(cal_count)
            cal_count = 0
    print(elf_total)
    print(max(elf_total))


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        MostCalories(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

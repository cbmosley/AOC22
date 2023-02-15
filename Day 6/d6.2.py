import sys
from pathlib import Path


def tuning(input):
    window_size = 14
    for i in range(len(input) - window_size + 1):
        group = input[i: i + window_size]
        if len(group) == len(set(group)):
            print(i + window_size)

            break


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        tuning(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

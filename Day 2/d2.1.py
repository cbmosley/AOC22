import sys
from pathlib import Path

# A and X = Rock 1 lose
# B and Y = Paper 2 draw
# C and Z = Scissors 3 win


def rock_paper_scissors(input):
    scores = input.split("\n")
    my_count = 0
    for score in scores:
        if score == "A X":
            my_count += 4
        elif score == "A Y":
            my_count += 8
        elif score == "A Z":
            my_count += 3
        elif score == "B X":
            my_count += 1
        elif score == "B Y":
            my_count += 5
        elif score == "B Z":
            my_count += 9
        elif score == "C X":
            my_count += 7
        elif score == "C Y":
            my_count += 2
        else:
            my_count += 6

    print(my_count)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        rock_paper_scissors(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

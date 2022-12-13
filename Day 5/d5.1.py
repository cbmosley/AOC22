import sys
from pathlib import Path
from collections import deque


def supply_stack(input):
    initial_stack, instuctions = (i.splitlines()
                                  for i in input.strip("\n").split(("\n\n")))

    stacks = {int(digit): [] for digit in initial_stack[-1]. replace(" ", "")}

    indexes = [index for index, char in enumerate(
        initial_stack[-1]) if char != " "]

    for string in initial_stack[:-1]:
        stack_num = 1
        for index in indexes:
            if string[index] != " ":
                stacks[stack_num].insert(0, string[index])
            stack_num += 1

    for instruction in instuctions:
        instruction = instruction.replace("move", "").replace(
            "from ", "").replace("to ", "").strip().split(" ")
        instruction = [int(i) for i in instruction]

        crates = instruction[0]
        from_stack = instruction[1]
        to_stack = instruction[2]

        for crate in range(crates):
            crate_removed = stacks[from_stack].pop()
            stacks[to_stack].append(crate_removed)

    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]

    print(answer)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        supply_stack(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

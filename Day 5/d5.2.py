import sys
from pathlib import Path


def crates(input):
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

        crates_to_remove = stacks[from_stack][-crates:]
        stacks[from_stack] = stacks[from_stack][:-crates]

        for crate in crates_to_remove:
            stacks[to_stack].append(crate)

    answer = ""
    for stack in stacks:
        answer += stacks[stack][-1]

    print(answer)


if __name__ == "__main__":
    file = Path(sys.argv[1])
    if Path.is_file(file):
        crates(Path.read_text(file))
    else:
        raise TypeError("This is not a file")

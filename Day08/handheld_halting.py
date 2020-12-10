import re


def read_instructions():
    with open("instructions.txt", "r") as f:
        instructions = enumerate(f.read().splitlines())
    return list(instructions)


def parse(instruction):
    command, operator, argument = re.match(r"(\w+) ([+-])(\d+)", instruction[1]).groups()
    return command, operator, int(argument)


def process_instructions(index, accumulator, processed_instructions, instructions):
    if index >= len(instructions):
        return accumulator, True
    if index in processed_instructions:
        return accumulator, False
    processed_instructions.append(index)
    command, operator, argument = parse(instructions[index])
    if command == "nop":
        index += 1
    elif command == "acc":
        accumulator = accumulator + argument if operator == "+" else accumulator - argument
        index += 1
    else:
        index = index + argument if operator == "+" else index - argument
    return process_instructions(index, accumulator, processed_instructions, instructions)


def main():
    instructions = read_instructions()
    print("Part one:", process_instructions(0, 0, [], instructions)[0])
    for i, line in instructions:
        altered_instructions = list(instructions)
        if line.startswith("jmp"):
            altered_instructions[i] = (i, line.replace("jmp", "nop"))
        elif line.startswith('nop'):
            altered_instructions[i] = (i, line.replace('nop', 'jmp'))
        else:
            continue
        accumulator, terminated = process_instructions(0, 0, [], altered_instructions)
        if terminated:
            print("Part two:", accumulator)


main()

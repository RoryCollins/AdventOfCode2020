import re

with open("instructions.txt", "r") as f:
    instructions = [(x, int(y)) for (x, y) in [re.match(r"(\w)(\d*)", line).groups() for line in f.read().splitlines()]]

ns_pos = 0
ew_pos = 0
direction = "E"


def turn_left(times):
    global direction
    while times > 0:
        if direction == "E":
            direction = "N"
        elif direction == "S":
            direction = "E"
        elif direction == "W":
            direction = "S"
        elif direction == "N":
            direction = "W"
        times -= 1


def turn_right(times):
    global direction
    while times > 0:
        if direction == "E":
            direction = "S"
        elif direction == "S":
            direction = "W"
        elif direction == "W":
            direction = "N"
        elif direction == "N":
            direction = "E"
        times -= 1


def process_instruction(command, value):
    global ns_pos, ew_pos
    if command == "N":
        ns_pos += value
    elif command == "S":
        ns_pos -= value
    elif command == "E":
        ew_pos += value
    elif command == "W":
        ew_pos -= value
    elif command == "F":
        process_instruction(direction, value)
    elif command == "L":
        turn_left(value / 90)
    elif command == "R":
        turn_right(value / 90)


for instruction in instructions:
    process_instruction(instruction[0], instruction[1])

print(abs(ns_pos) + abs(ew_pos))

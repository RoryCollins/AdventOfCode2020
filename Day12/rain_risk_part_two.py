import re

with open("instructions.txt", "r") as f:
    instructions = [(x, int(y)) for (x, y) in [re.match(r"(\w)(\d*)", line).groups() for line in f.read().splitlines()]]

ns_pos = 0
ew_pos = 0

wp_ns_pos = 1
wp_ew_pos = 10


def turn_right(times):
    global wp_ns_pos, wp_ew_pos
    while times > 0:
        new_ns_pos = wp_ew_pos * -1
        new_ew_pos = wp_ns_pos
        wp_ns_pos = new_ns_pos
        wp_ew_pos = new_ew_pos
        times -= 1


def turn_left(times):
    global wp_ns_pos, wp_ew_pos
    while times > 0:
        new_ns_pos = wp_ew_pos
        new_ew_pos = wp_ns_pos * -1
        wp_ns_pos = new_ns_pos
        wp_ew_pos = new_ew_pos
        times -= 1


def process_instruction(command, value):
    global ns_pos, ew_pos, wp_ew_pos, wp_ns_pos
    if command == "N":
        wp_ns_pos += value
    elif command == "S":
        wp_ns_pos -= value
    elif command == "E":
        wp_ew_pos += value
    elif command == "W":
        wp_ew_pos -= value
    elif command == "F":
        ew_pos += wp_ew_pos * value
        ns_pos += wp_ns_pos * value
    elif command == "L":
        turn_left(value / 90)
    elif command == "R":
        turn_right(value / 90)


for instruction in instructions:
    process_instruction(instruction[0], instruction[1])

print(abs(ns_pos) + abs(ew_pos))

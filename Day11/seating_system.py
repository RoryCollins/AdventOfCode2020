import itertools as it
import numpy as np

with open("floor_plan.txt", "r") as f:
    floor_plan = np.array([[x for x in r] for r in f.read().splitlines()])
max_row = len(floor_plan) - 1
max_col = len(floor_plan[0]) - 1


def is_occupied(row, col):
    if row < 0 or col < 0:
        return False
    if row > max_row or col > max_col:
        return False
    return floor_plan[row][col] == '#'


def count_occupied_neighbours(row, col):
    neighbours = list(it.product(range(row - 1, row + 2), range(col - 1, col + 2)))
    neighbours.remove((row, col))
    return sum([is_occupied(r, c) for (r, c) in neighbours])


def update_status(row, col):
    current_status = floor_plan[row][col]
    if current_status == ".":
        return "."
    elif current_status == "L" and count_occupied_neighbours(row, col) == 0:
        return "#"
    elif current_status == "#" and count_occupied_neighbours(row, col) >= 4:
        return "L"
    return current_status


def part_one():
    global floor_plan
    while True:
        next_stage = []
        for row in range(max_row + 1):
            next_stage.append("".join(map(lambda col: update_status(row, col), range(max_col + 1))))
        current_plan = np.array(next_stage)
        if floor_plan.tobytes() == current_plan.tobytes():
            break
        floor_plan = current_plan
    return sum(map(occupied_seats_in_row, range(max_row + 1)))


def part_two():
    while True:
        neighbours = np.array(
            [[count_occupied_neighbours_v2(x, y) for y in range(max_col + 1)] for x in range(max_row + 1)])
        previous = np.copy(floor_plan)
        floor_plan[(floor_plan == "L") & (neighbours == 0)] = "#"
        floor_plan[(floor_plan == "#") & (neighbours >= 5)] = "L"
        if (floor_plan == previous).all():
            break
    return np.count_nonzero(floor_plan == "#")


def occupied_seats_in_row(row):
    return sum(map(lambda col: is_occupied(row, col), range(max_col + 1)))


def main():
    # print("Part one:", part_one())
    print("Part two:", part_two())


def closest_seat_coord(coord, offset):
    curr_loc = (coord[0] + offset[0], coord[1] + offset[1])
    while 0 <= curr_loc[0] <= max_row and 0 <= curr_loc[1] <= max_col and floor_plan[curr_loc] == ".":
        curr_loc = (curr_loc[0] + offset[0], curr_loc[1] + offset[1])
    return curr_loc


def count_occupied_neighbours_v2(row, col):
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    return sum([is_occupied(r, c) for (r, c) in [closest_seat_coord((row, col), d) for d in directions]])


main()

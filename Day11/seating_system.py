import itertools as it

with open("floor_plan.txt", "r") as f:
    floor_plan = tuple(f.read().splitlines())
max_row = len(floor_plan) - 1
max_col = len(floor_plan[0]) - 1


def is_valid(row, col):
    if row < 0 or col < 0:
        return False
    if row > max_row or col > max_col:
        return False
    return True


def is_occupied(row, col):
    return floor_plan[row][col] == '#'


def count_occupied_neighbours(row, col):
    neighbours = list(it.product(range(row - 1, row + 2), range(col - 1, col + 2)))
    neighbours.remove((row, col))
    return sum(map(lambda rc: is_valid(rc[0], rc[1]) and is_occupied(rc[0], rc[1]), neighbours))


def update_status(row, col):
    current_status = floor_plan[row][col]
    if current_status == ".":
        return "."
    elif current_status == "L" and count_occupied_neighbours_v2(row, col) == 0:
        return "#"
    elif current_status == "#" and count_occupied_neighbours_v2(row, col) >= 4:
        return "L"
    return current_status


def part_one():
    global floor_plan
    current_hash = 0
    previous_hash = hash(floor_plan)
    while current_hash != previous_hash:
        next_stage = []
        for row in range(max_row + 1):
            next_stage.append("".join(map(lambda col: update_status(row, col), range(max_col + 1))))
        floor_plan = tuple(next_stage)
        previous_hash = current_hash
        current_hash = hash(floor_plan)


def occupied_seats_in_row(row):
    return sum(map(lambda col: is_occupied(row, col), range(max_col + 1)))


def main():
    part_one()
    print(sum(map(occupied_seats_in_row, range(max_row + 1))))


def all_seats_up_right(row, col):
    seats = []
    while row >= 0 and col <= max_col:
        seats.append((row, col))
        row -= 1
        col += 1
    return seats


def all_seats_down_right(row, col):
    seats = []
    while row <= max_row and col <= max_col:
        seats.append((row, col))
        row += 1
        col += 1
    return seats


def all_seats_up_left(row, col):
    seats = []
    while row >= 0 and col >= 0:
        seats.append((row, col))
        row -= 1
        col -= 1
    return seats


def all_seats_down_left(row, col):
    seats = []
    while row <= max_row and col >= 0:
        seats.append((row, col))
        row += 1
        col -= 1
    return seats


print(all_seats_up_right(2, 4))


def count_occupied_neighbours_v2(row, col):
    up = any(map(lambda x: is_occupied(x, col), range(row)))
    down = any(map(lambda x: is_occupied(x, col), range(row + 1, max_row + 1)))
    right = any(map(lambda x: is_occupied(row, x), range(col + 1, max_col + 1)))
    left = any(map(lambda x: is_occupied(row, x), range(col)))
    up_right = any(map(lambda rc: is_occupied(rc[0], rc[1]), all_seats_up_right(row, col)))
    down_right = any(map(lambda rc: is_occupied(rc[0], rc[1]), all_seats_down_right(row, col)))
    up_left = any(map(lambda rc: is_occupied(rc[0], rc[1]), all_seats_up_left(row, col)))
    down_left = any(map(lambda rc: is_occupied(rc[0], rc[1]), all_seats_down_left(row, col)))
    return sum([up, down, right, left, up_left, up_right, down_left, down_right])


main()

with open("floor_plan.txt", "r") as f:
    floor_plan = f.read().splitlines()
max_row = len(floor_plan) - 1
max_col = len(floor_plan[0]) - 1


def is_occupied(row, col):
    if row < 0 or col < 0:
        return False
    if row > max_row or col > max_col:
        return False
    return floor_plan[row][col] == '#'


def count_occupied_neighbours(row, col):
    neighbours = [(row - 1, col - 1), (row - 1, col), (row - 1, col + 1),
                  (row, col - 1), (row, col + 1),
                  (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)]
    return sum(map(lambda rc: is_occupied(rc[0], rc[1]), neighbours))


def update_status(row, col):
    if floor_plan[row][col] == ".":
        return "."
    if count_occupied_neighbours(row, col) == 0:
        return "#"
    if count_occupied_neighbours(row, col) >= 4:
        return "L"
    return floor_plan[row][col]


current_hash = 0
previous_hash = hash(tuple(floor_plan))
while current_hash != previous_hash:
    next_stage = []
    for row in range(max_row + 1):
        next_stage.append("".join(map(lambda col: update_status(row, col), range(max_col + 1))))
    floor_plan = next_stage
    previous_hash = current_hash
    current_hash = hash(tuple(floor_plan))

print(sum(map(lambda row: sum(map(lambda col: is_occupied(row, col), range(max_col + 1))), range(max_row + 1))))

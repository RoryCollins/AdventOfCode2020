import re


def main():
    all_seat_ids = list(map(find_seat_id, read_boarding_passes()))
    max_seat_id = max(all_seat_ids)
    min_seat_id = min(all_seat_ids)
    my_seat_id = set(range(min_seat_id, max_seat_id, 1)) - set(all_seat_ids)

    print("Part one:", max_seat_id)
    print("Part two:", my_seat_id)


def read_boarding_passes():
    f = open("./boarding_passes.txt", "r")
    boarding_passes = f.read().splitlines()
    f.close()
    return boarding_passes


def find_seat_id(command):
    row, column = re.match(r"^([FB]+)([RL]+)$", command).groups()
    row_id = find_row_id(row)
    column_id = find_column_id(column)

    return row_id * 8 + column_id


def find_row_id(row):
    return binary_search(row, 127, "B", "F")


def find_column_id(column):
    return binary_search(column, 7, "R", "L")


def binary_search(row, upper_bound, upper_command, lower_command):
    upper_bound = upper_bound + 1
    lower_bound = 0
    for command in row:
        if command == lower_command:
            upper_bound = int((upper_bound - lower_bound) / 2) + lower_bound
        elif command == upper_command:
            lower_bound = upper_bound - int(upper_bound - lower_bound) / 2
    return int(lower_bound)


if __name__ == "__main__":
    main()

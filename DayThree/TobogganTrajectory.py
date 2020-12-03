f = open("geography.txt")
lines = f.read().splitlines()
f.close()


def check_slope(right, down):
    x_position = 0
    y_position = 0
    trees = 0
    while y_position <= len(lines) - 1:
        line = lines[y_position]
        if line[x_position] == '#':
            trees += 1
        x_position = (x_position + right) % len(line)
        y_position += down
    return trees


route_one = check_slope(1, 1)
route_two = check_slope(3, 1)
route_three = check_slope(5, 1)
route_four = check_slope(7, 1)
route_five = check_slope(1, 2)

print("Part one:", route_two)
print("Part two:", route_one * route_two * route_three * route_four * route_five)

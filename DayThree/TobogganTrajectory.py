f = open("geography.txt")
lines = f.read().splitlines()
f.close()
width = len(lines[0])
height = len(lines) - 1


def check_slope(right, down):
    return recursive_check_slope(right, down, 0, 0, 0)


def recursive_check_slope(right, down, x, y, trees):
    if y > height:
        return trees
    total_trees_hit = (trees + 1) if lines[y][x] == '#' else trees
    return recursive_check_slope(right, down, (x + right) % width, y + down, total_trees_hit)


route_one = check_slope(1, 1)
route_two = check_slope(3, 1)
route_three = check_slope(5, 1)
route_four = check_slope(7, 1)
route_five = check_slope(1, 2)

print("Part one:", route_two)
print("Part two:", route_one * route_two * route_three * route_four * route_five)

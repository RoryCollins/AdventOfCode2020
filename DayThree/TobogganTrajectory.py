from functools import reduce
from operator import mul

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


print("Part one:", check_slope(3, 1))

all_slopes = (1, 1), (3, 1), (5, 1), (7, 1), (1, 2)
trees_in_slopes = map(lambda rd: check_slope(rd[0], rd[1]), all_slopes)
product_of_trees_in_slopes = reduce(mul, trees_in_slopes, 1)
print("Part two:", product_of_trees_in_slopes)

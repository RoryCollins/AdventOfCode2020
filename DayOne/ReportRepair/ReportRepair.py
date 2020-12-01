import itertools
from functools import reduce
from operator import mul


def product_of_records(number_of_records):
    f = open("expenseReport.txt")
    records = list(map(int, f.read().splitlines()))
    f.close()
    combinations = list(itertools.combinations(records, number_of_records))
    for combination in combinations:
        if sum(combination) == 2020:
            return reduce(mul, combination, 1)


print("Part one:", product_of_records(2))
print("Part two:", product_of_records(3))

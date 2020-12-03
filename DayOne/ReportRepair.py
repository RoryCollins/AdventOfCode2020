import itertools as it
from functools import reduce
from operator import mul


def product_of_records(number_of_records, records):
    all_combinations = list(it.combinations(records, number_of_records))
    combination = next(x for x in all_combinations if sum(x) == 2020)
    return reduce(mul, combination, 1)


def read_expense_records():
    f = open("expenseReport.txt", "r")
    records = list(map(int, f.read().splitlines()))
    f.close()
    return records


expense_records = read_expense_records()
print("Part one:", product_of_records(2, expense_records))
print("Part two:", product_of_records(3, expense_records))

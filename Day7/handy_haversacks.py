import re

f = open("rules.txt", "r")
rules = dict(map(lambda x: re.match(r"^(.*) bags contain (.*)\.$", x).groups(), f.read().splitlines()))
f.close()


def main():
    print("Part one:", sum(map(can_contain_shiny_gold_bag, rules)))
    print("Part two:", bags_inside("shiny gold") - 1)


def can_contain_shiny_gold_bag(bag):
    nested_bags = re.findall(r"\d?\s?(\w+ \w+) bag", rules[bag])
    if "shiny gold" in nested_bags:
        return True
    if "no other" in nested_bags:
        return False
    return any(map(can_contain_shiny_gold_bag, nested_bags))


def bags_inside(bag):
    nested_bags = re.findall(r"(\d) (\w+ \w+) bag", rules[bag])
    return 1 + sum(map(lambda x: int(x[0]) * bags_inside(x[1]), nested_bags))


main()

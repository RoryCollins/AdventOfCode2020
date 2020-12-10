import itertools as it

with open("port_data.txt", "r") as f:
    lines = list(map(int, f.read().splitlines()))


def get_weak_element():
    for i in range(26, len(lines) - 1):
        if not any(x for x in (it.combinations(lines[i - 25:i], 2)) if sum(x) == lines[i]):
            return lines[i]


weak_element = get_weak_element()
print("Part one:", weak_element)
a = 0
b = 1
while True:
    result = sum(lines[a:b+1])
    if result < weak_element:
        b += 1
        continue
    elif result > weak_element:
        a += 1
        continue
    else:
        print("Part two:", min(lines[a:b+1]) + max(lines[a:b+1]))
        break


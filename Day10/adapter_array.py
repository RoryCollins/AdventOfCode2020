from collections import defaultdict

with open("jolts.txt", "r") as f:
    jolts = list(map(int, f.read().splitlines()))
jolts.sort()

differences = {1: 1, 3: 1}
for i in range(1, len(jolts)):
    difference = jolts[i] - jolts[i - 1]
    differences[difference] += 1

print("Part one:", differences[1] * differences[3])

routes = defaultdict(int)
routes[jolts[-1]] = 1
for i in jolts[-2::-1]:
    routes[i] = routes[i + 1] + routes[i + 2] + routes[i + 3]
print("Part two:", routes[1] + routes[2] + routes[3])

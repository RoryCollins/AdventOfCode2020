import re

with open("bus_notes.txt", "r") as f:
    time = int(f.readline())
    buses = [int(bus) for bus in re.findall(r"\d*", f.readline()) if len(bus) != 0]

print(buses)
waiting_times = dict((bus, (bus - (time % bus))) for bus in buses)
next_bus = min(waiting_times.keys(), key=(lambda k: waiting_times[k]))
print("Part one:", next_bus * waiting_times[next_bus])


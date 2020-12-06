import re

f = open("customs_responses.txt", "r")
group_responses = map(lambda x: x.replace("\n", ""), list(re.split("\n\n", f.read())))
f.close()

print("Part one:", sum(list(map(lambda x: len(''.join(set(x))), group_responses))))


import re


def read_responses():
    f = open("customs_responses.txt", "r")
    group_responses = list(re.split("\n\n", f.read()))
    f.close()
    return group_responses


print("Part one:", sum(list(map(lambda x: len(''.join(set(x))), map(lambda x: x.replace("\n", ""), read_responses())))))


def count_common_answers(group_response):
    return len([x for x in filter(lambda x: all(x in response for response in group_response), group_response[0])])


print("Part two:", sum(map(count_common_answers, map(lambda x: re.split("\n", x), read_responses()))))

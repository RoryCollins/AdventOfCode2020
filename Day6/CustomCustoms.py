import re


def read_responses():
    f = open("customs_responses.txt", "r")
    group_responses = map(lambda x: re.split("\n", x), list(re.split("\n\n", f.read())))
    f.close()
    return group_responses


def concatenated_responses(responses):
    return map(lambda x: ''.join(x), responses)


print("Part one:", sum(map(lambda x: len(''.join(set(x))), concatenated_responses(read_responses()))))


def count_common_answers(group_response):
    return len([x for x in filter(lambda x: all(x in response for response in group_response), group_response[0])])


print("Part two:", sum(map(count_common_answers, read_responses())))

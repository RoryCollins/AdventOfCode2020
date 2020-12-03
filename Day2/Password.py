import re


class Password:
    def __init__(self, record):
        (num1, num2, self.requirement, self.password) = re.search('([0-9]+)-([0-9]+) ([a-z]): ([a-z]+)', record).groups()
        self.num1 = int(num1)
        self.num2 = int(num2)

    def validate_part_one(self):
        return self.num1 <= self.password.count(self.requirement) <= self.num2

    def validate_part_two(self):
        return (self.password[self.num1 - 1] == self.requirement) ^ (self.password[self.num2 - 1] == self.requirement)

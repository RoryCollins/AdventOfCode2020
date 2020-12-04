import re

from . import BirthYearValidator, IssueYearValidator, ExpirationYearValidator, HairColourValidator, \
    EyeColourValidator, PassportIdValidator, HeightValidator

f = open("passport_records.txt", "r")
records = re.split("\n\n", f.read())
f.close()


class Passport:
    def __init__(self, record):
        self.record = dict(re.findall(r"(\S+):(\S+)", record))

    def validate(self):
        validators = [
            BirthYearValidator(self.record.get("byr")),
            IssueYearValidator(self.record.get("iyr")),
            ExpirationYearValidator(self.record.get("eyr")),
            HeightValidator(self.record.get("hgt")),
            HairColourValidator(self.record.get("hcl")),
            EyeColourValidator(self.record.get("ecl")),
            PassportIdValidator(self.record.get("pid")),
        ]
        return all(map(lambda x: x.is_valid(), validators))

    def validate_item(self, item):
        return self.record.get(item) is not None

    def validate_byr(self):
        byr = self.record.get("byr")
        return byr is not None and 1920 <= int(byr) <= 2002


part_one = sum(map(lambda x: Passport(x).validate(), records))
print("Part one:", part_one)

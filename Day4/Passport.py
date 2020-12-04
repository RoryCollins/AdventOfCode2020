import re

from Day4 import BirthYearValidator, IssueYearValidator, ExpirationYearValidator, HeightValidator, HairColourValidator, \
    EyeColourValidator, PassportIdValidator


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

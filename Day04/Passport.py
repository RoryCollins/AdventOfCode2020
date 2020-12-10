import re

from Day04 import BirthYearValidator, IssueYearValidator, ExpirationYearValidator, HeightValidator, HairColourValidator, \
    EyeColourValidator, PassportIdValidator


class Passport:
    def __init__(self, record):
        self.record = dict(re.findall(r"(\S+):(\S+)", record))

    def validate(self):
        valid_fields = [
            BirthYearValidator().is_valid(self.record.get("byr")),
            IssueYearValidator().is_valid(self.record.get("iyr")),
            ExpirationYearValidator().is_valid(self.record.get("eyr")),
            HeightValidator().is_valid(self.record.get("hgt")),
            HairColourValidator().is_valid(self.record.get("hcl")),
            EyeColourValidator().is_valid(self.record.get("ecl")),
            PassportIdValidator().is_valid(self.record.get("pid")),
        ]
        return all(valid_fields)

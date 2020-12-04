import re

from Day4.Validators.Validator import Validator


class YearValidator(Validator):
    def __init__(self, min_year, max_year, value):
        self.min_year = min_year
        self.max_year = max_year
        super().__init__(value)

    def additional_validation(self):
        return \
            re.match(r"(\d){4}", self.value) is not None and \
            self.min_year <= int(self.value) <= self.max_year

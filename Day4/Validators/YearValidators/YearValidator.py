import re

from Day4.Validators.ValidatorBase import ValidatorBase


class YearValidator(ValidatorBase):
    def __init__(self, min_year, max_year):
        self.min_year = min_year
        self.max_year = max_year
        super().__init__()

    def additional_validation(self, value):
        return \
            re.match(r"(\d){4}", value) is not None and \
            self.min_year <= int(value) <= self.max_year

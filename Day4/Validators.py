import re
from abc import ABC, abstractmethod


class Validator(ABC):
    def __init__(self, value):
        self.value = value

    def is_valid(self):
        return self.value is not None and self.additional_validation()

    @abstractmethod
    def additional_validation(self):
        pass


class YearValidator(Validator):
    def __init__(self, min_year, max_year, value):
        self.min_year = min_year
        self.max_year = max_year
        super().__init__(value)

    def additional_validation(self):
        return \
            re.match(r"(\d){4}", self.value) is not None and \
            self.min_year <= int(self.value) <= self.max_year


class BirthYearValidator(YearValidator):
    min_year = 1920
    max_year = 2002

    def __init__(self, value):
        super().__init__(self.min_year, self.max_year, value)


class IssueYearValidator(YearValidator):
    min_year = 2010
    max_year = 2020

    def __init__(self, value):
        super().__init__(self.min_year, self.max_year, value)


class ExpirationYearValidator(YearValidator):
    min_year = 2020
    max_year = 2030

    def __init__(self, value):
        super().__init__(self.min_year, self.max_year, value)


class HeightValidator(Validator):
    def additional_validation(self):
        return self.is_between_150_and_196_cm() or self.is_between_59_and_76_in()

    def is_between_150_and_196_cm(self):
        return re.match(r"^(1[5-8][0-9]|19[0-3])cm$", self.value) is not None

    def is_between_59_and_76_in(self):
        return re.match(r"^(59|6[0-9]|7[0-6])in$", self.value) is not None


class HairColourValidator(Validator):
    def additional_validation(self):
        return re.match("^#[0-9a-f]{6}$", self.value) is not None


class EyeColourValidator(Validator):
    def additional_validation(self):
        valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.value in valid_colours


class PassportIdValidator(Validator):
    def additional_validation(self):
        return re.match("^[0-9]{9}$", self.value) is not None

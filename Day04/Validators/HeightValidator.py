import re

from Day04.Validators.ValidatorBase import ValidatorBase


class HeightValidator(ValidatorBase):
    def additional_validation(self, value):
        return self.is_between_150_and_193_cm(value) or self.is_between_59_and_76_in(value)

    @staticmethod
    def is_between_150_and_193_cm(value):
        return re.match(r"^(1[5-8][0-9]|19[0-3])cm$", value) is not None

    @staticmethod
    def is_between_59_and_76_in(value):
        return re.match(r"^(59|6[0-9]|7[0-6])in$", value) is not None

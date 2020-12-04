import re

from Day4.Validators.Validator import Validator


class HeightValidator(Validator):
    def additional_validation(self):
        return self.is_between_150_and_196_cm() or self.is_between_59_and_76_in()

    def is_between_150_and_196_cm(self):
        return re.match(r"^(1[5-8][0-9]|19[0-3])cm$", self.value) is not None

    def is_between_59_and_76_in(self):
        return re.match(r"^(59|6[0-9]|7[0-6])in$", self.value) is not None

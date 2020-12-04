import re

from Day4.Validators.Validator import Validator


class PassportIdValidator(Validator):
    def additional_validation(self):
        return re.match("^[0-9]{9}$", self.value) is not None
import re

from Day4.Validators.Validator import Validator


class HairColourValidator(Validator):
    def additional_validation(self):
        return re.match("^#[0-9a-f]{6}$", self.value) is not None
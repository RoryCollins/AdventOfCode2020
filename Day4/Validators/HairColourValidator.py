import re

from Day4.Validators.ValidatorBase import ValidatorBase


class HairColourValidator(ValidatorBase):
    @staticmethod
    def additional_validation(value):
        return re.match("^#[0-9a-f]{6}$", value) is not None

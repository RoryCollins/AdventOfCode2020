import re

from Day04.Validators.ValidatorBase import ValidatorBase


class PassportIdValidator(ValidatorBase):
    @staticmethod
    def additional_validation(value):
        return re.match("^[0-9]{9}$", value) is not None

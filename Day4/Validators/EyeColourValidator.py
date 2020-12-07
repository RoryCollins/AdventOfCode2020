from Day4.Validators.ValidatorBase import ValidatorBase


class EyeColourValidator(ValidatorBase):
    @staticmethod
    def additional_validation(value):
        valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return value in valid_colours

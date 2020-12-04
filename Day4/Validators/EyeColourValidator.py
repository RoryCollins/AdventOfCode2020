from Day4.Validators.Validator import Validator


class EyeColourValidator(Validator):
    def additional_validation(self):
        valid_colours = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
        return self.value in valid_colours
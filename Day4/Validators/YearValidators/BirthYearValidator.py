from Day4.Validators.YearValidators.YearValidator import YearValidator


class BirthYearValidator(YearValidator):
    min_year = 1920
    max_year = 2002

    def __init__(self):
        super().__init__(self.min_year, self.max_year)

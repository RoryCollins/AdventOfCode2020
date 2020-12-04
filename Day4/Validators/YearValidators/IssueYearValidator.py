from Day4.Validators.YearValidators.YearValidator import YearValidator


class IssueYearValidator(YearValidator):
    min_year = 2010
    max_year = 2020

    def __init__(self, value):
        super().__init__(self.min_year, self.max_year, value)
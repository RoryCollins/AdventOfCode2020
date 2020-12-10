import unittest
from . import BirthYearValidator, HeightValidator, PassportIdValidator, HairColourValidator, EyeColourValidator


class ValidatorTests(unittest.TestCase):
    def test_valid_birth_year(self):
        birth_year_validator = BirthYearValidator()
        self.assertEqual(birth_year_validator.is_valid(value="2002"), True)
        self.assertEqual(BirthYearValidator().is_valid("1920"), True)
        self.assertEqual(BirthYearValidator().is_valid("1988"), True)

    def test_invalid_birth_year(self):
        self.assertEqual(BirthYearValidator().is_valid(None), False)
        self.assertEqual(BirthYearValidator().is_valid("2003"), False)
        self.assertEqual(BirthYearValidator().is_valid("1919"), False)
        self.assertEqual(BirthYearValidator().is_valid("nineteen-ninety-four"), False)

    def test_valid_height(self):
        self.assertEqual(HeightValidator().is_valid("160cm"), True)
        self.assertEqual(HeightValidator().is_valid("60in"), True)

    def test_invalid_height(self):
        self.assertEqual(HeightValidator().is_valid("160in"), False)
        self.assertEqual(HeightValidator().is_valid("160"), False)

    def test_valid_hair_colour(self):
        self.assertEqual(HairColourValidator().is_valid("#123abc"), True)

    def test_invalid_hair_colour(self):
        self.assertEqual(HairColourValidator().is_valid("#123abz"), False)
        self.assertEqual(HairColourValidator().is_valid("123abc"), False)

    def test_valid_eye_colour(self):
        self.assertEqual(EyeColourValidator().is_valid("brn"), True)

    def test_invalid_eye_colour(self):
        self.assertEqual(EyeColourValidator().is_valid("wat"), False)

    def test_valid_passport_id(self):
        self.assertEqual(PassportIdValidator().is_valid("000000001"), True)

    def test_invalid_passport_id(self):
        self.assertEqual(PassportIdValidator().is_valid("0123456789"), False)


if __name__ == '__main__':
    unittest.main()

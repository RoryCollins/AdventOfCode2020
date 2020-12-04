import unittest
from . import BirthYearValidator, HeightValidator, PassportIdValidator, HairColourValidator, EyeColourValidator


class ValidatorTests(unittest.TestCase):
    def test_valid_birth_year(self):
        self.assertEqual(BirthYearValidator("2002").is_valid(), True)
        self.assertEqual(BirthYearValidator("1920").is_valid(), True)
        self.assertEqual(BirthYearValidator("1988").is_valid(), True)

    def test_invalid_birth_year(self):
        self.assertEqual(BirthYearValidator(None).is_valid(), False)
        self.assertEqual(BirthYearValidator("2003").is_valid(), False)
        self.assertEqual(BirthYearValidator("1919").is_valid(), False)
        self.assertEqual(BirthYearValidator("nineteen-ninety-four").is_valid(), False)

    def test_valid_height(self):
        self.assertEqual(HeightValidator("160cm").is_valid(), True)
        self.assertEqual(HeightValidator("60in").is_valid(), True)

    def test_invalid_height(self):
        self.assertEqual(HeightValidator("160in").is_valid(), False)
        self.assertEqual(HeightValidator("160").is_valid(), False)

    def test_valid_hair_colour(self):
        self.assertEqual(HairColourValidator("#123abc").is_valid(), True)

    def test_invalid_hair_colour(self):
        self.assertEqual(HairColourValidator("#123abz").is_valid(), False)
        self.assertEqual(HairColourValidator("123abc").is_valid(), False)

    def test_valid_eye_colour(self):
        self.assertEqual(EyeColourValidator("brn").is_valid(), True)

    def test_invalid_eye_colour(self):
        self.assertEqual(EyeColourValidator("wat").is_valid(), False)

    def test_valid_passport_id(self):
        self.assertEqual(PassportIdValidator("000000001").is_valid(), True)

    def test_invalid_passport_id(self):
        self.assertEqual(PassportIdValidator("0123456789").is_valid(), False)


if __name__ == '__main__':
    unittest.main()

import unittest

from Day05.BinaryBoarding import find_seat_id, find_row_id, find_column_id


class BinaryBoardingTests(unittest.TestCase):
    def test_find_seat_id(self):
        self.assertEqual(357, find_seat_id("FBFBBFFRLR"))
        self.assertEqual(567, find_seat_id("BFFFBBFRRR"))
        self.assertEqual(119, find_seat_id("FFFBBBFRRR"))
        self.assertEqual(820, find_seat_id("BBFFBBFRLL"))

    def test_find_row_id(self):
        self.assertEqual(44, find_row_id("FBFBBFF"))
        self.assertEqual(70, find_row_id("BFFFBBF"))
        self.assertEqual(14, find_row_id("FFFBBBF"))
        self.assertEqual(102, find_row_id("BBFFBBF"))

    def test_find_column_id(self):
        self.assertEqual(5, find_column_id("RLR"))
        self.assertEqual(7, find_column_id("RRR"))
        self.assertEqual(4, find_column_id("RLL"))


if __name__ == '__main__':
    unittest.main()

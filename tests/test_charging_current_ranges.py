from unittest import TestCase

from src.charging_current_ranges import (
    current_ranges_and_count,
    output_to_csv_format
)


class TestChargingCurrentRange(TestCase):
    def test_range_with_two_values(self):
        self.assertEqual([('4-5', '2')], current_ranges_and_count([4, 5]))

    def test_output_to_string(self):
        self.assertEqual('Range, Readings\n4-5, 2\n', output_to_csv_format([4, 5]))
        self.assertEqual('Range, Readings\n4-5, 2\n8-8, 1\n', output_to_csv_format([4, 5, 8]))
        self.assertEqual('Range, Readings\n3-5, 4\n10-12, 3\n', output_to_csv_format([3, 3, 5, 4, 10, 11, 12]))
        self.assertEqual('Range, Readings\n-3--2, 2\n3-5, 3\n10-12, 3\n', output_to_csv_format([-3, -2, 3, 5, 4, 10, 11, 12]))

from unittest import TestCase

from src.charging_current_ranges import current_ranges_and_count


class TestChargingCurrentRange(TestCase):
    def test_range_with_two_values(self):
        self.assertEqual('4-5, 2', current_ranges_and_count([4, 5]))

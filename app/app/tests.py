from django.test import TestCase


from app.calc import add, subtract


class CalcTests(TestCase):
    """docstring for CalcTests."""

    def test_add_numbers(self):
        """ Test That Two number are added together """
        self.assertEqual(add(3, 8), 11)

    def test_subtract_numbers(self):
        """ Test That values are Subtracted and returned """
        self.assertEqual(subtract(5, 11), 6)

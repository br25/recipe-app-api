from django.test import SimpleTestCase
from app import calc


class calcTests(SimpleTestCase):
    try:
        def test_add_number(self):
            res = calc.add(3, 4)
            self.assertEqual(res, 7)
    except Exception:
        def test_sub_number(self):
            res = calc.sub(100, 80)
            self.assertEqual(res, 20)

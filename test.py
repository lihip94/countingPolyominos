import unittest
from counting_polyominos import counting_poly


class TestCounting(unittest.TestCase):
    def test_sum(self):
        """
        test that it can calculate sum of fixed polyominos from number x
        """
        up_to_1 = counting_poly({(0, 0)}, set(), [], 1)
        up_to_2 = counting_poly({(0, 0)}, set(), [], 2)
        up_to_3 = counting_poly({(0, 0)}, set(), [], 3)
        up_to_4 = counting_poly({(0, 0)}, set(), [], 4)
        up_to_5 = counting_poly({(0, 0)}, set(), [], 5)
        up_to_6 = counting_poly({(0, 0)}, set(), [], 6)
        up_to_7 = counting_poly({(0, 0)}, set(), [], 7)
        up_to_8 = counting_poly({(0, 0)}, set(), [], 8)
        up_to_9 = counting_poly({(0, 0)}, set(), [], 9)
        up_to_10 = counting_poly({(0, 0)}, set(), [], 10)
        up_to_11 = counting_poly({(0, 0)}, set(), [], 11)
        up_to_12 = counting_poly({(0, 0)}, set(), [], 12)
        up_to_13 = counting_poly({(0, 0)}, set(), [], 13)
        up_to_14 = counting_poly({(0, 0)}, set(), [], 14)

        fixed_2 = up_to_2 - up_to_1
        fixed_3 = up_to_3 - up_to_2
        fixed_4 = up_to_4 - up_to_3
        fixed_5 = up_to_5 - up_to_4
        fixed_6 = up_to_6 - up_to_5
        fixed_7 = up_to_7 - up_to_6
        fixed_8 = up_to_8 - up_to_7
        fixed_9 = up_to_9 - up_to_8
        fixed_10 = up_to_10 - up_to_9
        fixed_11 = up_to_11 - up_to_10
        fixed_12 = up_to_12 - up_to_11
        fixed_13 = up_to_13 - up_to_12
        fixed_14 = up_to_14 - up_to_13

        self.assertEqual(fixed_2, 2, "should be 2")
        self.assertEqual(fixed_3, 6, "should be 6")
        self.assertEqual(fixed_4, 19, "should be 19")
        self.assertEqual(fixed_5, 63, "should be 63")
        self.assertEqual(fixed_6, 216, "should be 216")
        self.assertEqual(fixed_7, 760, "should be 760")
        self.assertEqual(fixed_8, 2725, "should be 2725")
        self.assertEqual(fixed_9, 9910, "should be 9910")
        self.assertEqual(fixed_10, 36446, "should be 36446")
        self.assertEqual(fixed_11, 135268, "should be 135268")
        self.assertEqual(fixed_12, 505861, "should be 505861")
        self.assertEqual(fixed_13, 1903890, "should be 1903890")
        self.assertEqual(fixed_14, 7204874, "should be 7204874")


if __name__ == '__main__':
    unittest.main()
    print("Everything passed")

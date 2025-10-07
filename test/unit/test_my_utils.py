#how to run the test: python3 test/unit/test_my_utils.py

import sys
import unittest
import random
import statistics

sys.path.append('src/')  # noqa

import my_utils
import tempfile
import os

class TestGetColumn(unittest.TestCase):
    def setUp(self):
        # Create a temporary CSV file for testing
        self.test_file = tempfile.NamedTemporaryFile(mode="w+", delete=False)
        self.test_file.write("UK,5\n")
        self.test_file.write("UK,30\n")
        self.test_file.write("USA,1000\n")
        self.test_file.write("JAPAN,-2\n")
        self.test_file.write("JAPAN,-4\n")
        self.test_file.close()
        self.file_name = self.test_file.name


    def tearDown(self):
        # Clean up the temporary file after each test
        os.remove(self.file_name)

    # positive values
    def test_match_positive(self):
        result = my_utils.get_column(self.file_name, 0, "UK", 1)
        self.assertEqual(result, [5, 30])
    
    # negative values
    def test_match_negative(self):
        result = my_utils.get_column(self.file_name, 0, "JAPAN", 1)
        self.assertEqual(result, [-2, -4])

    # no matching country
    def test_no_match(self):
        result = my_utils.get_column(self.file_name, 0, "CANADA", 1)
        self.assertEqual(result, [])

    # file not found
    def test_bad_file(self):
        with self.assertRaises(SystemExit):
            my_utils.get_column("non_existent_file.csv", 0, "USA", 1)


    def test_not_a_number(self):
        # Rewrite test file with a string in the second column
        with open(self.file_name, "w") as f:
            f.write("USA,not_a_number\n")

        with self.assertRaises(SystemExit):
            my_utils.get_column(self.file_name, 0, "USA", 1)


    def test_bad_index(self):
        # Query column index out of bounds
        with self.assertRaises(SystemExit):
            my_utils.get_column(self.file_name, 100, "USA", 1)

        # Result column index out of bounds
        with self.assertRaises(SystemExit):
            my_utils.get_column(self.file_name, 0, "UK", 100)


class TestMean(unittest.TestCase):
    def test_mean(self):
        # positive and negative number tests
        self.assertEqual(my_utils.mean([1, 2, 3, 4]), 2.5)
        self.assertEqual(my_utils.mean([10, 0]), 5.0)
        self.assertEqual(my_utils.mean([-1, -2, -3, -4]), -2.5)
        self.assertEqual(my_utils.mean([-10, -6, 6, 10]), 0.0)

        # the mean should always be between min and max
        arr = [random.randint(-100, 100) for _ in range(50)]
        m = my_utils.mean(arr)
        self.assertTrue(min(arr) <= m <= max(arr))

        # Error case
        self.assertRaises(SystemExit, my_utils.mean, [])


class TestMedian(unittest.TestCase):
    def test_median(self):
        # Odd length
        self.assertEqual(my_utils.median([3, 1, 2]), 2)

        # Even length
        self.assertEqual(my_utils.median([4, 6, 2, 3]), 3.5)

        # repeated values odd length
        self.assertEqual(my_utils.median([1, 2, 2, 2, 3]), 2)

        # repeated values even length
        self.assertEqual(my_utils.median([1, 2, 2, 2, 3, 3]), 2.0)

        # for odd length, median must be an element
        arr = [random.randint(-50, 50) for _ in range(51)]
        med = my_utils.median(arr)
        self.assertIn(med, arr)

        # for even length, median must be average of two elements
        arr = [random.randint(-50, 50) for _ in range(50)]
        sorted_arr = sorted(arr)
        mid = len(sorted_arr) // 2
        expected = (sorted_arr[mid - 1] + sorted_arr[mid]) / 2
        self.assertEqual(my_utils.median(arr), expected)

        # Error case
        self.assertRaises(SystemExit, my_utils.median, [])


class TestSTDev(unittest.TestCase):
    def test_stdev(self):
        # no variation
        self.assertEqual(my_utils.stdev([5, 5, 5, 5]), 0)

        # negatives
        self.assertAlmostEqual(my_utils.stdev([-2, -4, -4, -4]), 0.8660254)

        # mixed neg and positives
        self.assertAlmostEqual(my_utils.stdev([1, 2, 0, -1]), 1.11803399)

        # standard deviation is always non-negative
        arr = [random.randint(-20, 20) for _ in range(30)]
        std = my_utils.stdev(arr)
        self.assertGreaterEqual(std, 0)

        # Error case
        self.assertRaises(SystemExit, my_utils.stdev, [])


if __name__ == '__main__':
    unittest.main()

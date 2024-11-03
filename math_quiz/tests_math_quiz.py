import unittest
import math_quiz as mq


class TestMathGame(unittest.TestCase):
    def test_generate_integer_in_range(self):
        # Test if random numbers generated are within the specified range
        num_ranges = [
            (0, 0),
            (0.0, 0.0),
            (1, 1),
            (1.0, 1.0),
            (1, 10),
            (1, 10.0),
            (1.0, 5.0),
            (-1, -1),
            (-1.0, -1.0),
            (-1, 5),
            (-1, 5.0),
            (-1.0, 5.0),
            (-4, -1),
            (-4, -1.0),
            (-4.0, -1.0),
            (-4.1, -1),
            (-4.0, -1),
            (-3.9, -1),
            (-4.5, -1),
            (-4.4, -1),
            (-4.6, -1),
            (-4, -1.1),
            (-4, -1.0),
            (-4, -0.9),
            (-4, -1.5),
            (-4, -1.4),
            (-4, -1.6),
            (-4.0, -1.1),
            (-3.9, -1.0),
            (-4.5, -0.9),
            (-4.4, -1.5),
            (-4.6, -1.4),
            (-4.1, -1.6),
            (1, 5),
            (1, 5.1),
            (1, 5.0),
            (1, 4.9),
            (1, 5.5),
            (1, 5.4),
            (1, 5.6),
            (1.0, 5.0),
            (1.1, 5.0),
            (0.9, 5.0),
            (1.5, 5.0),
            (1.4, 5.0),
            (1.6, 5.0),
            (1.0, 5.0),
            (1.1, 4.9),
            (0.9, 5.1),
            (1.5, 5.4),
            (1.4, 5.5),
            (1.6, 5.6),
            (-4, 1),
            (-4, 1.1),
            (-4, 1.0),
            (-4, 0.9),
            (-4, 1.5),
            (-4, 1.4),
            (-4, 1.6),
            (-4.0, 1.1),
            (-4.1, 1.0),
            (-3.9, 0.9),
            (-4.5, 1.5),
            (-4.4, 1.4),
            (-4.6, 1.6),
        ]
        for min_val, max_val in num_ranges:
            for _ in range(1000):  # Test a large number of random values
                rand_num = mq.generate_integer_in_range(min_val, max_val)
                fail_msg = f"{rand_num} is not in ({min_val}, {max_val})"
                self.assertTrue(min_val <= rand_num <= max_val, fail_msg)

        # Test if ValueError is raised for ranges where min > max
        num_ranges = [(-5, -7), (1, -5), (0, -5), (5, 1), (5, 0)]
        for min_val, max_val in num_ranges:
            fail_msg = f"ValueError not raised for ({min_val}, {max_val})"
            # Display the error message if the test fails
            with self.assertRaises(ValueError, msg=fail_msg):
                mq.generate_integer_in_range(min_val, max_val)

        # Test if ValueError is raised for ranges with no integers
        num_ranges = [
            (-3.9, -3.6),
            (-3.6, -3.5),
            (-3.5, -3.4),
            (-3.4, -3.3),
            (-3.1, -3.1),
            (1.6, 1.9),
            (1.5, 1.6),
            (1.4, 1.5),
            (1.3, 1.4),
            (1.1, 1.1),
        ]
        for min_val, max_val in num_ranges:
            fail_msg = f"ValueError not raised for ({min_val}, {max_val})"
            # Display the error message if the test fails
            with self.assertRaises(ValueError, msg=fail_msg):
                mq.generate_integer_in_range(min_val, max_val)

        # Test if TypeError is raised for invalid input types
        num_ranges = [
            (0, " "),
            (0, ""),
            (0, "a"),
            (0, " x"),
            (0, "y "),
            (0, "v 1 "),
            (0, "1"),
            (0, " 1.0"),
            (0, "1.1 "),
            (0, "1.5"),
            (0, " 1.6 "),
            (" ", 0),
            ("", 0),
            ("a", 0),
            (" x", 0),
            ("y ", 0),
            ("v 1 ", 0),
            ("1", 0),
            (" 1.0", 0),
            ("1.1 ", 0),
            ("1.5", 0),
            (" 1.6 ", 0),
            (" ", " n"),
        ]
        for min_val, max_val in num_ranges:
            fail_msg = f"TypeError not raised for ({min_val}, {max_val})"
            # Display the error message if the test fails
            with self.assertRaises(TypeError, msg=fail_msg):
                mq.generate_integer_in_range(min_val, max_val)

    def test_generate_arithmetic_operation(self):
        # Test if the generated arithmetic operation is valid
        for _ in range(1000):  # Test a large number of random values
            operation = mq.generate_arithmetic_operation()
            fail_msg = f"Invalid operation: {operation}"
            self.assertIn(operation, ["+", "-", "*"], fail_msg)

    def test_apply_arithmetic_operation(self):
        # Test if returned values are as expected
        test_cases = [
            (5, 2, "+", "5 + 2", 7),
            (5, 2, "-", "5 - 2", 3),
            (5, 2, "*", "5 * 2", 10),
        ]

        for n1, n2, operator, expected_prob, expected_ans in test_cases:
            problem, answer = mq.apply_arithmetic_operation(n1, n2, operator)
            fail_msg = f"Expected Problem: {expected_prob}, Given: {problem}"
            self.assertEqual(problem, expected_prob, fail_msg)
            fail_msg = f"Expected Answer: {expected_ans}, Given: {answer}"
            self.assertEqual(answer, expected_ans, fail_msg)

        # Test if TypeError is raised for invalid input types
        params = [
            (5, " ", "+"),
            (5, "", "-"),
            (5, "a", "*"),
            (5, " x", "+"),
            (5, "y ", "-"),
            (5, "v 1 ", "*"),
            (5, "1", "+"),
            (5, " 1.0", "-"),
            (5, "1.1 ", "*"),
            (5, "1.5", "+"),
            (5, " 1.6 ", "-"),
            (" ", 2, "+"),
            ("", 2, "-"),
            ("a", 2, "*"),
            (" x", 2, "+"),
            ("y ", 2, "-"),
            ("v 1 ", 2, "*"),
            ("1", 2, "+"),
            (" 1.0", 2, "-"),
            ("1.1 ", 2, "*"),
            ("1.5", 2, "+"),
            (" 1.6 ", 2, "-"),
            (" ", "n", "+"),
            (5, 2, 9),
            (5, 2, 9.1),
            (5, 2, 0.0),
            (5, 2, -9.5),
        ]

        for n1, n2, operator in params:
            fail_msg = f"TypeError not raised for ({n1}, {n2}, {operator})"
            # Display the error message if the test fails
            with self.assertRaises(TypeError, msg=fail_msg):
                mq.apply_arithmetic_operation(n1, n2, operator)

        # Test if ValueError is raised for invalid operators
        operators = [" ", "", "a", " x", "y ", "v 1 ", "1", " 1.0"]
        for operator in operators:
            fail_msg = f"ValueError not raised for {operator}"
            # Display the error message if the test fails
            with self.assertRaises(ValueError, msg=fail_msg):
                mq.apply_arithmetic_operation(5, 2, operator)


if __name__ == "__main__":
    unittest.main()

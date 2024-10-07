class Solution:
    def romanToInt(self, s: str) -> int:
        # Map of Roman numeral characters to their integer values
        roman_map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        
        total = 0
        prev_value = 0
        
        # Iterate through each character in the string from right to left
        for char in reversed(s):
            current_value = roman_map[char]
            
            # If the current value is less than the previous value, subtract it
            if current_value < prev_value:
                total -= current_value
            else:
                total += current_value
            
            # Update the previous value to current
            prev_value = current_value
        
        return total

# Test code
import unittest

class TestRomanToInt(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example1(self):
        self.assertEqual(self.solution.romanToInt("III"), 3)

    def test_example2(self):
        self.assertEqual(self.solution.romanToInt("LVIII"), 58)

    def test_example3(self):
        self.assertEqual(self.solution.romanToInt("MCMXCIV"), 1994)

    def test_single_roman_digit(self):
        self.assertEqual(self.solution.romanToInt("X"), 10)

    def test_subtraction_rule(self):
        self.assertEqual(self.solution.romanToInt("IV"), 4)
        self.assertEqual(self.solution.romanToInt("IX"), 9)

    def test_large_number(self):
        self.assertEqual(self.solution.romanToInt("MMMCMXCIX"), 3999)

    def test_empty_string(self):
        self.assertEqual(self.solution.romanToInt(""), 0)

if _name_ == '_main_':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
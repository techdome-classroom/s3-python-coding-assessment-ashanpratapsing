class Solution(object):
   def romanToInt(s: str) -> int:

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
  
    for char in reversed(s):
        current_value = roman_map[char]
        
        # If the current value is less than the previous value, we subtract it (for cases like IV, IX, etc.)
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        
        # Update the previous value for the next iteration
        prev_value = current_value
    
    return total
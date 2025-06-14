'''
2025/06/14 daily challenge

brute force approach

iterate all possible digits and maximize/minimize the value.
'''


class Solution:
    def minMaxDifference(self, num: int) -> int:
        s = str(num)
        digits = set(s)
        # shortcut: if there's only one digit,
        # then the max difference is the same length number with only digit 9.
        if len(digits) == 1:
            return int("9" * len(s))

        max_val = 0
        min_val = float('inf')
        for digit in digits:
            remapped = int(s.replace(digit, "9"))
            max_val = max(max_val, remapped)
            remapped = int(s.replace(digit, "0"))
            min_val = min(min_val, remapped)

        return max_val - min_val


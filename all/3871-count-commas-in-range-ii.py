'''
2026/09/09 daily challenge

count commas in ranges
'''


class Solution:
    def countCommas(self, n: int) -> int:
        if n < 1000:
            return 0

        low, high = 1_000, 1_000_000
        comma = 1  # commas of current level
        total = 0

        while n >= high:
            total += comma * (high - low)
            low, high = high, high * 1_000
            comma += 1

        total += comma * (n - low + 1)
        return total


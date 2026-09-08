'''
2026/09/08 daily challenge

since there's a maximum of 100,000,
it means each number in [1000, 100000] has only one comma and
no more conditions.
'''


class Solution:
    def countCommas(self, n: int) -> int:
        return max(0, n - 999)


'''
2025/09/08 daily challenge

brute-force approach
'''


class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        # exhaustive search [a, b] pair
        for a in range(1, n // 2 + 1):
            if "0" in str(a):
                continue
            b = n - a
            if "0" not in str(b):
                return [a, b]


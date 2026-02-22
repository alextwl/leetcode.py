'''
2026/02/22 daily challenge
'''


class Solution:
    def binaryGap(self, n: int) -> int:
        i = 0
        prev = -1
        max_gap = 0
        while n:
            if n & 1:
                if prev >= 0:
                    max_gap = max(max_gap, i - prev)
                prev = i
            i += 1
            n >>= 1
        return max_gap


'''
2024/10/28 daily challenge

exhaustive method approach

iterate all possible square roots and try starting streaks.
we only need to check the existance of roots & squares by set,
no need to sort each subsequence.
'''


import math


class Solution:
    def longestSquareStreak(self, nums: List[int]) -> int:
        keys = set(nums)
        max_val = max(keys)
        max_sqrt = math.floor(max_val ** 0.5)

        max_len = 1
        for root in range(2, max_sqrt + 1):
            if root not in keys:
                continue
            length = 1
            while root < max_val:
                root = root * root
                if root not in keys:
                    break
                length += 1
            max_len = max(max_len, length)

        return max_len if max_len > 1 else -1


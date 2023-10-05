'''
Counter + sort approach
'''

import collections


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)

        candidates = sorted([(k, v) for k, v in counts.items() if k & 1 == 0], key=lambda x: (-x[1], x[0]))

        if not candidates:
            return -1

        return candidates[0][0]


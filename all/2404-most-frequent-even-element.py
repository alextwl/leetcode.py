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

'''
non-sorting two-pass ver
'''

import collections


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        
        ans = 100002
        max_freq = 0
        
        for k, v in counts.items():
            if k & 1:
                continue
            if v > max_freq or (v == max_freq and k < ans):
                ans = k
                max_freq = v

        return ans if ans <= 100000 else -1


'''
2025/10/30 daily challenge

increment by difference

2 conditions to determine if we need to initialize a new subarray to increment:
(1) if target[i-1] >= target[i], we can just extend some or all parts of
    subarrays ending at target[i-1] and form target[i].
(2) if target[i-1] < target[i], we can extend only some parts of subarrays
    ending at target[i-1] and need to initialize new subarrays starting from
    target[i].
'''


import itertools


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        ans = target[0]
        for a, b in itertools.pairwise(target):
            if a < b:
                ans += b - a
        return ans


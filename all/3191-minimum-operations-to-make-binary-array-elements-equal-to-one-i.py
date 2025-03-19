'''
2025/03/19 daily challenge

sliding window approach
'''


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        it = iter(nums)
        v0 = next(it)
        v1 = next(it)
        flips = 0
        for v2 in it:
            if v0 == 0:
                flips += 1
                v0 = v1 ^ 1
                v1 = v2 ^ 1
            else:
                v0, v1 = v1, v2
        if not v0 or not v1:
            return -1
        return flips


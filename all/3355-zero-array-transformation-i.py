'''
2025/05/20 daily challenge

prefix difference approach
'''


class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        offsets = [0] * (len(nums) + 1)
        for l, r in queries:
            offsets[l] -= 1
            offsets[r + 1] += 1
        
        diff = 0
        for v, offset in zip(nums, offsets):
            diff += offset
            v += diff
            if v > 0:
                return False
        return True


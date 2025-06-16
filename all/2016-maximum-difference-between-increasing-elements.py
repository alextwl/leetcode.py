'''
2025/06/16 daily challenge

track the minimal value we've seen and maximize the difference.
'''


class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_val = nums[0]
        max_diff = -1
        for v in nums:
            if v < min_val:
                min_val = v
            elif v > min_val:
                max_diff = max(max_diff, v - min_val)
        return max_diff


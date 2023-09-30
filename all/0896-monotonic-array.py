'''
2023/09/29 daily challenge

brute force approach
'''

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        prev = nums[0]
        last_diff = 0
        for v in nums:
            diff = v - prev
            if diff:
                if (diff > 0 and last_diff < 0) or (diff < 0 and last_diff > 0):
                    return False
                last_diff = diff
            prev = v
        return True


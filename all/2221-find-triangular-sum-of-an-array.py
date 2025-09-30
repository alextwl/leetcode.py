'''
2025/09/30 daily challenge

brute force approach
'''


class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        n = len(nums)
        for width in range(n, 0, -1):
            for i in range(width - 1):
                nums[i] = (nums[i] + nums[i + 1]) % 10
        return nums[0]


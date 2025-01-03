'''
2025/01/03 daily challenge

prefix sum approach
'''


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr_sum = 0
        ans = 0
        for v in nums[:-1]:
            curr_sum += v
            if curr_sum >= total_sum - curr_sum:
                ans += 1
        return ans


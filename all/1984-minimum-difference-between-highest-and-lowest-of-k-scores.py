'''
2026/01/25 daily challenge

sliding window approach
'''


class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        ans = 100_001
        nums.sort()
        for i in range(len(nums) - k + 1):
            ans = min(ans, nums[i + k - 1] - nums[i])
        return ans


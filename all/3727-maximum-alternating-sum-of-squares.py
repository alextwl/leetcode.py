'''
2026/10/13 daily challenge

sorting by absolute value approach
'''


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort(key=abs, reverse=True)

        ans = 0
        for i in range(n // 2 + (n & 1)):
            ans += nums[i] * nums[i]
        for i in range(n // 2 + (n & 1), n):
            ans -= nums[i] * nums[i]

        return ans


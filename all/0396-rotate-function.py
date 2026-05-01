'''
2026/05/01 daily challenge

dynamic programming approach

F(0) = 0 * nums[0] + 1 * nums[1] + ... + (n-1) * nums[n - 1]
F(1) = 1 * nums[0] + 1 * nums[1] + ... + (n-1) * nums[n - 2] + 0 * nums[n - 1]
     = F(0) + sum(nums) - n * nums[n - 1]
F(2) = F(1) + sum(nums) - n * nums[n - 2]
...
F(k) = F(k-1) + sum(nums) - n * nums[n - k]
'''


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total = sum(nums)
        fk = sum(i * v for i, v in enumerate(nums))

        ans = fk
        for i in range(n - 1, 0, -1):
            fk = fk + total - n * nums[i]
            ans = max(ans, fk)

        return ans


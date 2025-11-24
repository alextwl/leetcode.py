'''
2025/11/24 daily challenge

modular arithmetic approach

keeping only the remainder part of prefix speeds up.

induction:
x0 = rem0 since x0 is always < 5.

x1 = rem1 since x1 is always < 5.

x2 % 5 = (x1 << 1 + nums[2]) % 5
       = (x1 << 1) % 5 + nums[2] % 5
rem2 = (rem1 << 1 + nums[2]) % 5
     = ((x1 % 5) << 1 + nums[2]) % 5
     = ((x1 % 5) << 1) % 5 + nums[2] % 5
     = (x1 << 1) % 5 + nums[2] % 5
     = (x1 << 1) % 5 + nums[2] % 5
x2 % 5 == rem2, and so on.
'''


class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        v = 0
        ans = []
        for b in nums:
            v = ((v << 1) + b) % 5
            ans.append(v == 0)
        return ans


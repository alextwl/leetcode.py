'''
2025/04/02 daily challenge

exhaustive method approach
'''


class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, ival in enumerate(nums):
            for j in range(i + 1, n - 1):
                i_j = ival - nums[j]
                for k in range(j + 1, n):
                    kval = nums[k]
                    if i_j ^ kval < 0:
                        continue
                    ans = max(ans, i_j * kval)
        return ans


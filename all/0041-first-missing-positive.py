'''
2024/03/26 daily challenge

cycle sort approach

learnt from official solution 3
https://leetcode.com/problems/first-missing-positive/solution/
'''


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        i = 0
        # move positive number < n to the correct index
        while(i < n):
            j = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        
        for i, v in enumerate(nums):
            if v != i + 1:
                return i + 1

        # 1..n exist, so the smallest missing positive number is n + 1
        return n + 1


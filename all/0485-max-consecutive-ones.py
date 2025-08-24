'''
two pointers approach
'''


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        i = -1
        for j, v in enumerate(nums):
            if v == 0:
                longest = max(longest, j - i - 1)
                i = j
        return max(longest, j - i) if nums[-1] else longest


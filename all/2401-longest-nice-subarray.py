'''
2025/03/18 daily challenge

sliding window approach
'''


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        longest = 1
        i = 0
        curr_and = 0
        for j, v in enumerate(nums):
            if curr_and & v:
                longest = max(longest, j - i)
                # shrink the window until no duplicate bits in bitwise AND.
                while i < j and curr_and & v:
                    curr_and -= nums[i]
                    i += 1
            curr_and += v
        return max(longest, len(nums) - i)


'''
sliding window approach
'''


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        longest = 0
        ones = zeros = 0

        i = 0
        for j, v in enumerate(nums):
            if v:
                ones += 1
            else:
                longest = max(longest, ones + zeros)
                zeros += 1
                k -= 1
                while k < 0:
                    if nums[i]:
                        ones -= 1
                    else:
                        zeros -= 1
                        k += 1
                    i += 1

        return max(longest, ones + zeros)


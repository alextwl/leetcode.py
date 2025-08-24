'''
2023/07/05 daily challenge
2025/08/24 daily challenge

sliding window approach
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        last_zero = None
        ans = ones = 0
        
        for right, v in enumerate(nums):
            if v == 0:
                if last_zero is not None:
                    # when we found 2nd and later zeroes, update the max ans.
                    ans = max(ans, ones)
                    ones = right - last_zero - 1

                last_zero = right
            else:
                ones += 1

        if last_zero is None:
            return ones - 1  # we must delete 1 element even if there's no zero.

        return max(ans, ones)


'''
dynamic programming approach
'''


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        longest = 0
        dp0 = dp1 = 0  #  len([1,1,1,...]), one 0's, len([1,1,1,...])

        for v in nums:
            if v:
                dp1 += 1
            else:
                longest = max(longest, dp0 + dp1)
                dp0, dp1 = dp1, 0
        # summarize last subarray
        longest = max(longest, dp0 + dp1)

        if longest == len(nums):
            # must delete one element
            return len(nums) - 1
        return longest


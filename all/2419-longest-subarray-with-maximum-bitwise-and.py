'''
counter approach

bitwise AND of two different numbers will always be lesser than max(two numbers),
so our actual target is to find a longest subarray with consecutive same maximum **value**.

it's similar to problem 2038.
'''

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        max_val = 0
        max_len = 0

        prev = 0
        run_len = 0

        for v in nums:
            if v == prev:
                run_len += 1
            else:
                if prev > max_val or (prev == max_val and run_len > max_len):
                    max_val = prev
                    max_len = run_len
                # new subarray
                run_len = 1
            prev = v
        
        # check if last subarray prevails.
        if prev > max_val or (prev == max_val and run_len > max_len):
            max_len = run_len

        return max_len


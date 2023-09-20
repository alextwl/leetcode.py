'''
2023/09/20 daily challenge

sliding window approach

the actual problem is to find the longest subarray where its sum = sum(nums) - x.
'''


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        # the target of sum of the longest subarray (window)
        target = sum(nums) - x
        # the maximum length of target subarray, -1 indicates not found.
        max_len = -1
        # current sliding window sum
        window_sum = 0
        # sliding window pointers
        left = 0
        for right, val in enumerate(nums):
            # always add val (== nums[right]) to window_sum
            window_sum += val
            
            # shrink the window from left until window_sum <= target.
            while(left <= right and window_sum > target):
                window_sum -= nums[left]
                left += 1
            
            # target hit?
            if window_sum == target:
                # found a valid window
                max_len = max(max_len, right - left + 1)
        
        if max_len == -1:
            # impossible to find an answer
            return -1
        
        # the answer is the minimum length of prefix subarray + suffix subarray == full length of array - the window.
        return len(nums) - max_len


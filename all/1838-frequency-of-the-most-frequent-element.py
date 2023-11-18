'''
2023/11/18 daily challenge

sliding window approach

learnt from official solution
https://leetcode.com/problems/frequency-of-the-most-frequent-element/solution/

there's a proof that shows the most frequent element is guaranteed in the array,
so we can try to choose each element as a target to evaluate if it could be
the most frequent by sliding window.
'''


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        left = 0  # sliding window pointers
        window_sum = 0
        max_freq = 0
        
        # let each nums[right] as the target we want to increment elements to.
        for right, target in enumerate(nums):
            window_sum += target
            
            # shrink the sliding window to make sure
            # needed operations (== the diffs between each elements and target within the window)
            # are equal or smaller than k.
            while (window_size := (right - left + 1)) * target - window_sum > k:
                window_sum -= nums[left]
                left += 1

            max_freq = max(max_freq, window_size)

        return max_freq


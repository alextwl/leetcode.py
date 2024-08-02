'''
2024/08/02 daily challenge

sliding window approach
'''


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        swaps = n  # init with a large number which is never valid

        ones_max = sum(nums)
        
        # init with sliding window of i-to-j inclusive: nums[0:1]
        ones_count = nums[0]
        j = 0
        for i in range(n):
            if i != 0:
                ones_count -= nums[i - 1]

            while (j - i + 1) < ones_max:
                j += 1
                ones_count += nums[j % n]  # back to leftside if out-of-bound
    
            swaps = min(swaps, ones_max - ones_count)
    
        return swaps


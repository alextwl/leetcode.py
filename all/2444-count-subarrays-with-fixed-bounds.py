'''
2023/03/04 daily challenge

sliding window approach
'''

class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        ans = 0  # counts of valid subarrays
        left = right = -1  # init with negative so that further max() won't return it if it's not yet assigned.
        '''
        keep the last index of number which cannot be included in a subarray
        between minK and maxK.
        '''
        invalid_left_bound = -1

        for i, v in enumerate(nums):
            if v == minK:
                left = i
            if v == maxK:
                right = i
            if not(minK <= v <= maxK):
                invalid_left_bound = i
            
            '''
            ans is incremented only if:
            
            the current range forms valid subarrays:
            [... , nums[left or right], ..., nums[left or right]]
            and both left & right are greater than invalid_left_bound.

            ans is not incremented (i.e. max() returns zero) if:

            (1) invalid_left_bound is beyond left & right.
            no subarray is formed.

            (2) left < invalid_left_bound < right.
            no subarray is formed until a newer left (minK) is found after invalid_left_bound.
            '''
            ans += max(0, min(left, right) - invalid_left_bound)
        
        return ans


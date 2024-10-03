'''
2024/10/03 daily challenge

prefix sum modulo p approach

learnt from official solution 2:
https://leetcode.com/problems/make-sum-divisible-by-p/solution/

derive the equations of prefix sum modulo p:

target remainder to remove = sum % p

(prefix_sum_i - prefix_sum_j) % p = target

prefix_sum_j = (prefix_sum_i - target) % p

needed = (curr_sum - target) % p

needed = (curr_sum - target + p) % p
'''


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        n = len(nums)
        target = sum(nums) % p
        
        if target == 0:
            return 0
        
        # prefix_mod[key] = the index of the last seen mod in nums[].
        # key=mod, key=0 indicates the whole array is selected to be removed.
        prefix_mod = {0: -1}
        
        curr_sum = 0  # with modulo p
        min_len = n
        for i, v in enumerate(nums):
            curr_sum = (curr_sum + v) % p
            remainder = (curr_sum - target + p) % p  # +p is to prevent negative result.
            
            if remainder in prefix_mod:
                min_len = min(min_len, i - prefix_mod[remainder])

            prefix_mod[curr_sum] = i
        
        return -1 if min_len == n else min_len


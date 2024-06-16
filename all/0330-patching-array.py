'''
2024/06/16 daily challenge

greedy method approach
'''


class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss = 1   # the next number we might miss in the array
        patch = 0  # the minimum number of patches required
        
        i = 0
        while miss <= n:
            # try to extend the range can be formed
            if i < len(nums) and nums[i] <= miss:
                # we can extend the range to [1, miss + nums[i])
                miss += nums[i]
                i += 1
            else:
                # add/patch miss to the array to extend the range to [1, miss * 2)
                miss <<= 1
                patch += 1

        return patch


'''
2026/08/18 daily challenge

conditional classification approach
'''


import collections


class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        if k == 1:
            # each element is a subarray, find uniquely largest
            ctr = collections.Counter(nums)
            for v in sorted(ctr.keys(), reverse=True):
                if ctr[v] == 1:
                    return v
            return -1
        elif k == len(nums):
            # there's only one subarray
            return max(nums)
        elif nums[0] == nums[-1]:
            # although the first and the last elements appear in one subarray
            # respectively, but it's invalid because its values are the same.
            return -1
        else:
            # and we need to check if the first and the last didn't appear in
            # other subarrays or not.
            max_val = -1
            if nums[0] not in nums[1:]:
                max_val = nums[0]
            if nums[-1] not in nums[:-1]:
                max_val = max(max_val, nums[-1])
            return max_val


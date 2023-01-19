'''
leetcode 75 lv2 day 12

dynamic programming approach

learnt from
https://leetcode.com/problems/partition-equal-subset-sum/solutions/1624939/c-python-5-simple-solutions-w-explanation-optimization-from-brute-force-to-dp-to-bitmask/
'''

import functools


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        @functools.cache
        def isSubsetValid(rem_sum, i):
            '''
            :param rem_sum: remained summation to be subtracted
            :param i: the index of i to be added to a subset
            '''
            if rem_sum == 0:
                '''
                if remained summation reached zero,
                it means a subset formed from the caller is equal to half sum(nums).
                '''
                return True
            if i >= len(nums) or rem_sum < 0:
                '''
                insufficient num to form a valid subset
                or we cannot get a sum of subset which is half sum(nums).
                '''
                return False
            '''
            subset with nums[i] vs subset without nums[i].
            '''
            return isSubsetValid(rem_sum - nums[i], i+1) or isSubsetValid(rem_sum, i+1)

        '''
        if the array can be partitioned into 2 subsets,
        sum(nums) must be even, that means each subset's sum is half sum(nums).

        if we could find one subset's sum == half sum(nums),
        the another subset's sum must be half sum(nums) too,
        so we can just find one subset with half sum(nums).
        '''
        full_sum = sum(nums)
        return full_sum & 1 == 0 and isSubsetValid(full_sum >> 1, 0)


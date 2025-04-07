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


'''
2025/04/07 daily challenge

knapsack + dynamic programming approach
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        half = total >> 1

        # dp[i] = availability of subset sum i.
        dp = [False] * (total + 1)
        dp[0] = True  # base case: not picking any number

        for v in nums:
            for curr_sum in range(half, v - 1, -1):
                dp[curr_sum] = dp[curr_sum] or dp[curr_sum - v]

        return dp[half]


'''
bitwise knapsack approach

consider the previous approach,
the inner loop is actually doing shiftings to the right side of dp space,
we can simplify it by bitwise operations.

for example of [1,5,11], half=11.

dp[0] = True  # base case
dp == [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...
   == 0b1

i=0, v=1:
dp[11] ... dp[2] remain False.
dp[1] = dp[1] | dp[0] = False | True = True
dp == [1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, ...
   == (0b1 << 1) | 1 == 0b11

i=1, v=5:
dp[11] ... dp[7] remain False
dp[6] = dp[6] | dp[6-5] = False | True = True
dp[5] = dp[5] | dp[5-5] = True
dp == [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, ...
   == (0b11 << 5) | 0b11 = 0b0b110011

i=2, v=11:
dp[11] = dp[11] | dp[11-11] = False | True = True
dp == [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, ...
   == (0b110011 << 11) | 0b0b110011
   == 0b11001100000110011

i=3, v=5:
dp[11] = True
dp[10] = dp[10] | dp[10-5] = False | True = True
dp[9] ... dp[7] remain False
dp[6], dp[5] remain True
dp == [1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 1, 1, ...
   == (0b11001100000110011 << 5) | 0b11001100000110011
   == 0b1100111001111001110011

the answer is dp[11] == bool(0b1100111001111001110011 & (1 << 11)).
'''


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total & 1:
            return False
        half = total >> 1

        dp = 1
        for v in nums:
            dp |= dp << v
        
        return (dp & (1 << half)) > 0


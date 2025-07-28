'''
2024/10/18 daily challenge
2025/07/28 daily challenge

dynamic programming approach (nearly TLE)

iterate all possible bits and OR each element from nums.
'''


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val = 0
        dp = [0] * (1 << 17)  # the bit-length of maximum possible value 10**5 is 17-bit
        
        dp[0] = 1  # base case: 1 empty subset
        
        for v in nums:
            for i in range(max_val, -1, -1):
                # add the combinations of current subset i to another subset with OR v.
                dp[i | v] += dp[i]
            # the maximum value is always bitwise-OR all nums.
            max_val |= v

        return dp[max_val]


'''
iterate all possible mask approach
'''


import functools


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_val = functools.reduce(int.__or__, nums)
        
        n = 1 << len(nums)  # the number of possible subsets
        ans = 0
        
        # check all subsets
        for mask in range(n):
            subset_val = 0
            for i, v in enumerate(nums):
                # check if the element was to be included or not.
                if (mask >> i) & 1:
                    subset_val |= v
            if subset_val == max_val:
                ans += 1

        return ans


'''
combinatorial approach
'''


import collections
import functools
import itertools


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        d = collections.defaultdict(int)

        for cnt in range(1, len(nums) + 1):
            for subset in itertools.combinations(nums, cnt):
                mask = functools.reduce(int.__or__, subset)
                d[mask] += 1

        return d[functools.reduce(int.__or__, nums)]


'''
yet another dynamic programming approach (bottom up ver)

runtime=3ms!
'''


class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        dp = {0: 1}  # base case: 1 empty subset
        max_val = 0

        # add each element of nums to existed subsets
        for v in nums:
            max_val |= v
            for mask, count in dp.copy().items():
                mask |= v
                dp[mask] = dp.get(mask, 0) + count

        return dp[max_val]


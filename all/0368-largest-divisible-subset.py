'''
2024/02/09 daily challenge
2025/04/06 daily challenge

dynamic programming approach (recursive ver)

hint: if nums[j] % nums[i] == 0,
then all factors of nums[i] are also the factors of nums[j].
we can extend the subset by appending smaller factors.
'''

import functools


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # the order is not important, sort it to make finding pairs easily
        nums.sort()
        
        @functools.cache
        def dp(pos):
            divisor = nums[pos]
            max_sub = list()
            
            # iterate all values (as a dividend) larger than nums[pos] (as a divisor)
            for i in range(pos+1, n):
                if nums[i] % divisor == 0:
                    sub = dp(i)
                    if len(sub) > len(max_sub):
                        max_sub = sub
            
            # note each element can be a valid subset of single element
            # because the question does not mention index i cannot be index j.
            return [divisor] + max_sub
        
        ans = list()
        
        # iterate all subsets within nums[i:]
        for i in range(n):
            sub = dp(i)
            if len(sub) > len(ans):
                ans = sub

        return ans


'''
dynamic programming approach (bottom-up ver)
'''


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums.sort()

        dp = [[v] for v in nums]

        for i in range(n - 2, -1, -1):
            div = nums[i]
            max_subset = []
            for j in range(i + 1, n):
                if len(dp[j]) > len(max_subset) and nums[j] % div == 0:
                    max_subset = dp[j]
            dp[i].extend(max_subset)

        return max(dp, key=len)


'''
yet another top-down ver
'''


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        dp = {}  # dp[subset_len] = [subset_1, subset_2, ...]
        nums.sort()

        max_len = 1
        it = iter(nums)
        dp[1] = [[next(it)]]

        for v in it:
            appended = False
            # try to find existed largest subset and append it.
            for sub_len in range(max_len, 0, -1):
                next_len = sub_len + 1
                for sub_list in dp[sub_len]:
                    if v % sub_list[-1] == 0:
                        if next_len > max_len:
                            max_len = next_len
                            dp[next_len] = [sub_list + [v]]
                        else:
                            dp[next_len].append(sub_list + [v])
                        appended = True
                        break
                if appended:
                    break
                # add a new subset of only v itself.
                if sub_len == 1:
                    dp[1].append([v])
        # return the first (any) largest subset
        return dp[max_len][0]


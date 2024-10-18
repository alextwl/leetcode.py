'''
2024/10/18 daily challenge

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


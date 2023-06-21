'''
2023/06/21 daily challenge

prefix sum approach

learnt from official solution 1
https://leetcode.com/problems/minimum-cost-to-make-array-equal/solution/
'''

class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        nums_cost = sorted(zip(nums, cost))
        
        # pre-calculate the prefix & suffix sums of cost
        prefix = [0] * n
        prefix[0] = prev = nums_cost[0][1]
        for i in range(1, n):
            prefix[i] = prev + nums_cost[i][1]
            prev = prefix[i]

        suffix = [0] * n
        suffix[-1] = prev = nums_cost[-1][1]
        for i in range(n-2, -1, -1):
            suffix[i] = prev + nums_cost[i][1]
            prev = suffix[i]
        
        # try to set the equal value to nums[0]
        total_cost = 0
        it = iter(nums_cost)
        equal_value = next(it)[0]
        for v, c in it:
            total_cost += c * (v - equal_value)
        
        # minimize the total cost from nums[1] to nums[-1]
        min_cost = total_cost
        for i in range(1, n):
            diff = nums_cost[i][0] - nums_cost[i-1][0]
            # add (previous prefix - current suffix)
            total_cost += (prefix[i-1] - suffix[i]) * diff
            min_cost = min(min_cost, total_cost)
        
        return min_cost


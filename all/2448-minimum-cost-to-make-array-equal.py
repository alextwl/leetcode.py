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
        '''
        given nums = [1,2,3,5] and we know nums[0]=1,
        convert it to [1,1,1,1] and calculate the total cost.
        '''
        total_cost = 0
        it = iter(nums_cost)
        equal_value = next(it)[0]
        for v, c in it:
            total_cost += c * (v - equal_value)
        
        # minimize the total cost from nums[1] to nums[-1]
        min_cost = total_cost
        for i in range(1, n):
            '''
            the current value of total_cost is
            the total cost for converting original nums to
            [nums[i-1], nums[i-1], ..., nums[i-1]].

            imagine that we want to convert it
            to [nums[i], nums[i], ..., nums[i]],
            we need to do more operations to the element 0..i-1
            (by adding prefix sum to the cost)
            and cancel more operations to the element i..n-1
            (by substracting suffix sum from the cost
            because the total cost includes operations costs for
            converting all elements to nums[i-1].)
            '''
            diff = nums_cost[i][0] - nums_cost[i-1][0]
            # add (previous prefix - current suffix)
            total_cost += (prefix[i-1] - suffix[i]) * diff
            min_cost = min(min_cost, total_cost)
        
        return min_cost


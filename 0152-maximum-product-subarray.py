'''
the idea is similar to Kadane's but maintains 2 products including max & min.
the min part is to track if a negative becomes maximum positive later.

the subarray restarts if iterated num was bigger/smaller than current max/min.
'''

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        g = iter(nums)
        ans = maxprod = minprod = next(g)  # init with first number
        
        for num in g:
            maxprod, minprod = max(num, num*maxprod, num*minprod), min(num, num*maxprod, num*minprod)
            ans = max(ans, maxprod)
        
        return ans

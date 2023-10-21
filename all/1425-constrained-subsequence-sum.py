'''
2023/10/21 daily challenge

max heap + modified Kadane's approach
'''

from heapq import heappush, heappop


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        it = enumerate(nums)
        
        # a max heap containing subset sums, with first element as an initial subset sum
        h = [(-next(it)[1], 0)]  # (negative subset sum, index)
        max_sum = -h[0][0]
        
        for i, var in it:
            # pop elements outside of sliding window from the maximum sum in the heap.
            while i - h[0][1] > k:
                heappop(h)
            
            # modified Kadane's algorithm
            curr_sum = max(-h[0][0], 0) + var
            max_sum = max(max_sum, curr_sum)
            heappush(h, (-curr_sum, i))

        return max_sum


'''
dynamic programming approach (TLE)
'''


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        dp = [0] * len(nums)

        for i, var in enumerate(nums):
            prev_sum = max(dp[max(0, i-k):i], default=0)
            dp[i] = max(prev_sum + var, var)

        return max(dp)


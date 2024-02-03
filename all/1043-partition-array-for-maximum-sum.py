'''
2024/02/03 daily challenge

dynamic programming approach
'''


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0] * (n+1)
        
        # iterate in bottom-up order
        for left in range(n-1, -1, -1):
            right = min(n, left + k)
            max_val = 0
            
            # evaluate all partition's maximum in arr[left:right] range
            for i in range(left, right):
                max_val = max(max_val, arr[i])
                dp[left] = max(dp[left], dp[i+1] + max_val * (i-left+1))

        return dp[0]


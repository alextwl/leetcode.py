'''
2026/09/17 daily challenge

sliding window + dynamic programming approach
'''


MAX_LEN = 100_001  # arr.length <= 10**5


class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        curr_sum = 0
        ans = MAX_LEN

        # dp[i] = the shortest length of subarray with target sum in arr[:i]
        dp = [MAX_LEN] * (n + 1)
        left = 0
        for right, v in enumerate(arr):
            curr_sum += v

            # shrink the window until current sum <= target
            while curr_sum > target:
                curr_sum -= arr[left]
                left += 1

            dp[right + 1] = dp[right]
            if curr_sum == target:
                # length of current window which meets target sum requirement
                curr_len = right - left + 1
                # plus the previous shortest one (if < MAX_LEN)
                # so that we have two non-overlapping subarrays
                ans = min(ans, curr_len + dp[left])
                dp[right + 1] = min(dp[right], curr_len)
        
        if ans == MAX_LEN:
            # subarrays not found
            return -1
        return ans


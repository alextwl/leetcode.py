'''
2025/11/27 daily challenge

prefix sum approach (Kadane's algorithm)

learnt from official editorial:
https://leetcode.com/problems/maximum-subarray-sum-with-length-divisible-by-k/editorial/#approach-prefix-sum
'''


INF = float('inf')


class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        pfx = 0  # running prefix sum
        max_sum = -INF
        # ksum[rem] = minimum prefix sum when rem = (i - j + 1) % k
        ksum = [INF] * k
        # init for the first k-length subarray sum = pfx[k-1] - pfx[0],
        # there's no previous subarray with the same remainder
        # so the initial minimum subarray sum of remainder (k-1) is 0.
        ksum[-1] = 0

        for i, v in enumerate(nums):
            pfx += v
            rem = i % k
            if ksum[rem] is not INF:
                # pfx - ksum[rem] stands for the maximum subarray sum
                # excluding *previous* minimum k-length subarray sum
                # with the same remainder.
                max_sum = max(max_sum, pfx - ksum[rem])
                # minimize for further case with the same remainder
                ksum[rem] = min(ksum[rem], pfx)
            else:
                ksum[rem] = pfx

        return max_sum


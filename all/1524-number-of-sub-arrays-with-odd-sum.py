'''
2025/02/25 daily challenge

prefix sum approach
'''


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0
        # counters of parity of prefix sum
        odds = 0
        evens = 1  # initial zero sum is also an even sum
        prefix_sum = 0

        for v in arr:
            prefix_sum += v
            if prefix_sum & 1:
                # odd sum prefix
                # we can append current number to all previous even sum subarrays
                # to make subarray sums to be odd
                ans += evens
                odds += 1
            else:
                # even sum prefix
                # we can append current number to all previous odd sum subarrays
                ans += odds
                evens += 1
            ans = ans % 1_000_000_007
        return ans


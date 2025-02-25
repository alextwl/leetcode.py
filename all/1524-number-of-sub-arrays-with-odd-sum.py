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


'''
simplified ver
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
                odds += 1
            else:
                evens += 1
        return odds * evens % 1_000_000_007


'''
dynamic programming approach (bottom-up ver)
'''


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)

        #dp0/dp1[i] = count of even/odd sum subarrays ending at arr[i]
        dp0 = [0] * n
        dp1 = [0] * n

        # init from the last element of arr
        if arr[-1] & 1:
            dp1[-1] = 1
        else:
            dp0[-1] = 1

        for i in range(n - 2, -1, -1):
            if arr[i] & 1:
                # current element: an odd number
                # (current + previous even sum subarrays) and current itself are new odd sum subarrays
                dp1[i] = (dp0[i+1] + 1) % 1_000_000_007
                # current + previous odd sum subarrays = equal number of even sum subarrays
                dp0[i] = dp1[i+1]
            else:
                # current element: an even number
                # (current + previous odd sum subarrays) and current itself are new even sum subarrays
                dp0[i] = (dp0[i+1] + 1) % 1_000_000_007
                # current + previous odd sum subarrays = equal number of odd sum subarrays
                dp1[i] = dp1[i+1]

        return sum(dp1) % 1_000_000_007


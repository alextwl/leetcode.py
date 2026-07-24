'''
2026/07/24 daily challenge

O(n**3) brute force approach (time limit exceeded)
'''


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set()
        for i, v0 in enumerate(nums):
            for j in range(i, n):
                v01 = v0 ^ nums[j]
                for k in range(j, n):
                    seen.add(v01 ^ nums[k])
        return len(seen)


'''
O(n**2 + n*max_xor) enumeration approach
'''


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)

        # find max value and max possible XOR value
        # (which is the maximum available bit length we can manipulate)
        max_val = max(nums)
        k = 1 << max_val.bit_length()
        # seen XOR values of (a, b)
        seen0 = [False] * k

        # precompute (a, b) pairs
        for i, v0 in enumerate(nums):
            for j in range(i, n):
                seen0[v0 ^ nums[j]] = True

        # seen XOR value of (a, b, c)
        seen1 = [False] * k
        # enumerate all possible XOR values (**NOT** nums)
        for xor01, seen_flag in enumerate(seen0):
            if seen_flag:
                for v2 in nums:
                    seen1[xor01 ^ v2] = True

        return sum(seen1)


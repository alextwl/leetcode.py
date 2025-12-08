'''
O(n**3) brute-force approach
'''


class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        for i, v0 in enumerate(nums):
            for j in range(i + 1, n - 1):
                v1 = nums[j]
                if v0 == v1:
                    continue
                for k in range(j + 1, n):
                    v2 = nums[k]
                    if v0 != v2 and v1 != v2:
                        ans += 1
        return ans


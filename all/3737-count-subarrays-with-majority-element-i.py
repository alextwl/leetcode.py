'''
2026/06/25 daily challenge

brute force approach

1831ms, Beats 40.89%
time=O(n**2)
'''


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = 0
            for j in range(i, n):
                if nums[j] == target:
                    seen += 1
                if seen > ((j - i + 1) >> 1):
                    ans += 1
        return ans


'''
slightly optimized brute force ver
'''


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = 0
        for i in range(n):
            seen = 0
            for j in range(i, n):
                if nums[j] == target:
                    seen += 1
                else:
                    seen -= 1
                if cnt > 0:
                    ans += 1
        return ans


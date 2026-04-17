'''
2026/04/17 daily challenge

memorization approach
'''


class Solution:
    def minMirrorPairDistance(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        # since 0 <= i < j and reverse(nums[i]) == nums[j],
        # the closest reversed value is always the last seen in the left of j.
        prev = dict()
        for j, v in enumerate(nums):
            if v in prev:
                ans = min(ans, j - prev[v])
            prev[int(str(v)[::-1])] = j
        return ans if ans < n else -1


'''
2025/06/24 daily challenge
'''


class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        for j, v in enumerate(nums):
            if v != key:
                continue
            # scan left & right k-distant indices, except those were already in the ans.
            for i in range(max(j - k, (ans[-1] + 1) if ans else 0), min(len(nums), j + k + 1)):
                ans.append(i)
        return ans


'''
2026/05/14 daily challenge

counter approach
'''


class Solution:
    def isGood(self, nums: List[int]) -> bool:
        max_val = len(nums) - 1
        cnt = [0] * len(nums)

        for v in nums:
            if v > max_val:
                return False
            if (v == max_val and cnt[max_val] == 2) or (v < max_val and cnt[v] == 1):
                return False
            cnt[v] += 1

        return True


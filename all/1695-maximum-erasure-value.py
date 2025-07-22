'''
2025/07/22 daily challenge

two pointers approach
'''


import collections


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        cnt = collections.defaultdict(int)

        score = 0
        max_score = 0
        i = 0
        for j, v in enumerate(nums):
            score += v
            cnt[v] += 1
            while i < j and cnt[v] > 1:
                score -= nums[i]
                cnt[nums[i]] -= 1
                i += 1
            max_score = max(max_score, score)
        return max_score


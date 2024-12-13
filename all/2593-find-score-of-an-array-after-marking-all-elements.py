'''
2024/12/13 daily challenge

min heap approach
'''


import heapq


class Solution:
    def findScore(self, nums: List[int]) -> int:
        mark = [False] * len(nums)
        h = []
        for i, v in enumerate(nums):
            heapq.heappush(h, (v, i))

        end = len(nums) - 1
        score = 0
        while h:
            v, i = heapq.heappop(h)
            if mark[i]:
                continue
            score += v
            if i > 0:
                mark[i-1] = True
            mark[i] = True
            if i < end:
                mark[i+1] = True
        return score


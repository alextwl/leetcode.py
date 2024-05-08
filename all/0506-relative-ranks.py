'''
2024/05/08 daily challenge

heap approach
'''

import heapq


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        n = len(score)
        h = []
        ans = [None] * n

        for i, val in enumerate(score):
            heapq.heappush(h, (-val, i))

        for rank_name in ["Gold Medal", "Silver Medal", "Bronze Medal"]:
            if h:
                ans[heapq.heappop(h)[1]] = rank_name
            else:
                return ans

        for i in range(4, n + 1):
            ans[heapq.heappop(h)[1]] = str(i)

        return ans


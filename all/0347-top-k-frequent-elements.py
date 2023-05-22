'''
2023/05/22 daily challenge

heap approach
'''

import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = collections.Counter(nums)
        h = []  # max heap (min heap with negatived counter)

        for key, count in freq.items():
            heapq.heappush(h, (-count, key))

        ans = []
        for _ in range(k):
            _, key = heapq.heappop(h)
            ans.append(key)

        return ans


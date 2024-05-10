'''
2024/05/10 daily challenge

exhaustive approach
'''

import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)
        h = []
        
        for j in range(1, n):
            for i in range(j):
                heapq.heappush(h, (arr[i] / arr[j], arr[i], arr[j]))
        
        for _ in range(k - 1):
            heapq.heappop(h)

        return heapq.heappop(h)[1:]


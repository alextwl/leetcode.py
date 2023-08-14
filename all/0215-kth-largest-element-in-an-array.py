'''
2023/08/14 daily challenge

heap approach
'''

import heapq


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        h = []
        for v in nums:
            # convert to max-heap
            heapq.heappush(h, -v)
        
        for _ in range(k):
            curr = heapq.heappop(h)
        
        return -curr


'''
2023/05/23 daily challenge

heap approach

the idea is to build a min heap and keep its length <= k
so that the smallest element (h[0]) is always the k-th largest element.
'''

from heapq import heappush, heapreplace


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.h = []

        # push nums into the heap by the method of add.
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        '''
        if the length of heap was lesser than k,
        just push the new element.
        '''
        if len(self.h) < self.k:
            heappush(self.h, val)
        elif val > self.h[0]:
            '''
            pop the smallest (aka the k-th largest element) and push the new val.
            we can alway discard the smallest because when we push any new val
            if it's greater than the smallest.
            '''
            heapreplace(self.h, val)
        return self.h[0]


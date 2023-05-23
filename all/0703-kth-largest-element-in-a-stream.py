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

        # push the first k-1 elements into the heap.
        it = iter(nums)
        for _ in range(k-1):
            heappush(self.h, next(it))
        
        # push the remainings by the method of add.
        for num in it:
            self.add(num)

    def add(self, val: int) -> int:
        '''
        if the length of heap was lesser than k,
        just push the new element.
        the check is only needed once because
        the question guarantees that there will be at least k elements when searching.
        '''
        self.add = self.add2
        if len(self.h) < self.k:
            heappush(self.h, val)
            return self.h[0]
        return self.add2(val)

    def add2(self, val: int) -> int:
        '''
        pop the smallest (aka the k-th largest element) and push the new val.
        we can alway discard the smallest because when we push any new val
        if it's greater than the smallest.
        '''
        if val > self.h[0]:
            heapreplace(self.h, val)
        return self.h[0]


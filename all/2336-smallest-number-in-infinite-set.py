'''
2023/04/25 daily challenge

use min heap and memorize the boundary
to reduce the access and prevent from searching the heap.

Runtime 119 ms Beats 77.75%
'''

from heapq import heappush, heappop


class SmallestInfiniteSet:

    def __init__(self):
        self.h = []  # a min heap for added integers which were once removed.
        self.s = set()  # a set for querying the existance of a positive integer.
        self.heap_max_bound = 1  # the number next to the maximum number once added to the heap.

    def popSmallest(self) -> int:
        if self.h:
            '''
            if the heap is not empty, it must contain the smallest number
            because these numbers had been removed at least once.
            '''
            ret = heappop(self.h)
            self.s.remove(ret)
            return ret

        # grow the bound
        ret = self.heap_max_bound
        self.heap_max_bound += 1
        return ret

    def addBack(self, num: int) -> None:
        if num < self.heap_max_bound and num not in self.s:
            '''
            if the num equals to or is greater than self.heap_max_bound,
            it is in the infinite set because it was neither once removed nor re-added to the heap,
            so that we can feel free to skip it.
            '''
            self.s.add(num)
            heappush(self.h, num)


'''
search the removed numbers from the heap and guess the smallest.
with poor score Runtime 5136 ms Beats 5.22% :'(
'''

from heapq import heappush, heappop


class SmallestInfiniteSet:

    def __init__(self):
        self.h = []  # a min heap for removed integers
        '''
        a set for querying the absence of a positive integer.
        if an integer was in the set, the integer has been removed.
        '''
        self.s = set()

    def popSmallest(self) -> int:
        q = []
        smallest = 1
        while(self.h):
            popped = heappop(self.h)
            q.append(popped)
            if popped == smallest:
                # the popped is already removed
                smallest += 1
            elif popped > smallest:
                # the minimum can be popped
                break
        # recover the heap
        while(q):
            heappush(self.h, q.pop())
        # add the removed smallest to the heap & the set.
        heappush(self.h, smallest)
        self.s.add(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num in self.s:
            self.s.remove(num)
            q = []
            # remove num from the heap
            while((popped := heappop(self.h)) != num):
                q.append(popped)
            while(q):
                heappush(self.h, q.pop())


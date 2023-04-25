'''
2023/04/25 daily challenge

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


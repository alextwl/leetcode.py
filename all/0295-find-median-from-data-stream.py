'''
2022/11/12 daily challenge

heap approach

learnt from
https://leetcode.com/problems/find-median-from-data-stream/discuss/1330646/C%2B%2BJavaPython-MinHeap-MaxHeap-Solution-Picture-explain-Clean-and-Concise

use two heaps (max/min) to store low/high numbers,
and the popped value or the mean of values will be the median.

note the python heap is provided as min heap.
'''

from heapq import heappush, heappop


class MedianFinder:

    def __init__(self):
        self.lows = []  # stores low numbers (converted negative ver)
        self.highs = []  # store high numbers 
        
    def addNum(self, num: int) -> None:
        # always push input to lows and move the maximum num of lows to highs.
        heappush(self.lows, -num)
        heappush(self.highs, -heappop(self.lows))
        '''
        maintain the balance of 2 heaps.
        
        always let low numbers be longer than the highs if possible,
        and the maximum num of lows will be always the median.
        '''
        if len(self.highs) > len(self.lows):
            heappush(self.lows, -heappop(self.highs))
        
    def findMedian(self) -> float:
        if len(self.lows) > len(self.highs):
            '''
            the size of total values is odd,
            so the maximum number of lows is the median.
            '''
            return -self.lows[0]  # -(-median) = median
        '''
        the size of total values is even, no middle value exists.
        the median is the mean of (max lows + min highs).
        '''
        return (-self.lows[0] + self.highs[0]) / 2


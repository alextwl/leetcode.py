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


'''
heap + math approach

reduced calculation by skipping those fractions
which are impossible to be the answer.

for [n1, n2, n3, n4, n5], possible answers are in:

n1/n5, n1/n4, n1/n3, n1/n2
n2/n5, n2/n4, n2/n3
n3/n5, n3/n4
n4/n5

learnt from official solution 2:
https://leetcode.com/problems/k-th-smallest-prime-fraction/solution/
'''

import heapq


class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # note arr is already sorted.
        n = len(arr)
        h = []  # (fraction, index of numerator, index of denominator)

        # calculate fractions of each numerator with largest denominator
        for i in range(n - 1):
            heapq.heappush(h, (arr[i] / arr[-1], i, n - 1))

        for _ in range(k - 1):
            _, i, j = heapq.heappop(h)
            # while we are popping arr[i]/arr[j],
            # we can ensure a fraction of the same numerator with smaller denominator
            # is always larger than the current fraction if it exists.
            # let's push it.
            j -= 1
            if j > i:
                heapq.heappush(h, (arr[i] / arr[j], i, j))

        return [arr[v] for v in heapq.heappop(h)[1:]]


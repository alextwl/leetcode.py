'''
generate n-th ugly number approach

learnt from a nice explanation:
https://leetcode.com/problems/ugly-number-ii/discuss/69373/Short-and-O(n)-Python-and-C%2B%2B

walrus op used for speedup, python 3.8+ required.
'''


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # sequence of generated ugly numbers
        ugly = [1]
        '''
        the indexes of n-th ugly number to be multiplied by 2/3/5 respectively.
        
        e.g. when 6 is the last generated ugly number,
        the next indexes may be:
        i2=3, ugly[3] = 4, next candidate: ugly[i2]*2 = 8
        i3=2, ugly[2] = 3, next candidate: ugly[i3]*3 = 9
        i5=1, ugly[1] = 2, next candidate: ugly[i5]*5 = 10
        
        the minimum one of the above candidates is the next ugly number, which is ugly[i2]*2 = 8.
        '''
        i2 = i3 = i5 = 0
        
        while len(ugly) < n:
            '''
            try to multiply by one of prime factors to go over the last ugly number.
            '''
            while (c2 := ugly[i2] * 2) <= ugly[-1]:
                i2 += 1
            while (c3 := ugly[i3] * 3) <= ugly[-1]:
                i3 += 1
            while (c5 := ugly[i5] * 5) <= ugly[-1]:
                i5 += 1
            # get the minimum of next ugly candidates.
            ugly.append(min(c2, c3, c5))

        return ugly[-1]


'''
2024/08/18 daily challenge

min heap approach

always generate the ugly number in the sorted order of multiplications:
2 * 2 * 2 * ... * 3 * 3 * ... * 5,
maintain 3 heaps and merge it.
'''


import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        
        h2 = [2]
        h3 = [3]
        h5 = [5]
        
        for _ in range(1, n):
            if h2[0] < h3[0] and h2[0] < h5[0]:
                # next ugly has only 1 prime factor which is 2.
                current = heapq.heappop(h2)
                heapq.heappush(h2, current * 2)
                heapq.heappush(h3, current * 3)
                heapq.heappush(h5, current * 5)
            elif h3[0] < h5[0]:
                # next ugly has 2 prime factors which are 2 & 3.
                current = heapq.heappop(h3)
                heapq.heappush(h3, current * 3)
                heapq.heappush(h5, current * 5)
            else:
                # next ugly has 3 prime factors including 2, 3 & 5.
                current = heapq.heappop(h5)
                heapq.heappush(h5, current * 5)

        return current


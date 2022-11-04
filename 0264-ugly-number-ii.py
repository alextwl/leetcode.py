'''
generate n-th ugly number approach

learnt from a nice explanation:
https://leetcode.com/problems/ugly-number-ii/discuss/69373/Short-and-O(n)-Python-and-C%2B%2B
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
            while ugly[i2] * 2 <= ugly[-1]:
                i2 += 1
            while ugly[i3] * 3 <= ugly[-1]:
                i3 += 1
            while ugly[i5] * 5 <= ugly[-1]:
                i5 += 1
            # get the minimum of next ugly candidates.
            ugly.append(min(ugly[i2]*2, ugly[i3]*3, ugly[i5]*5))
        
        return ugly[-1]

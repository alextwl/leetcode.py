'''
2022/08/06 daily challenge

learnt from official hint 3 & @DBabichev's explanation:
https://leetcode.com/problems/poor-pigs/discuss/935112/Python-Math-solution-detailed-expanations

another explanation:
https://leetcode.com/problems/poor-pigs/discuss/94266/Another-explanation-and-solution

Hint 3 is obviously the solution where we find minumum `x` as the answer.

derivation:
(1) (T+1)**x >= N
(2) log((T+1)**x) >= log(N)
(3) x * log(T+1) >= log(N)
(4) x >= log(N) / log(T+1)
(5) x >= log(N) of base=T+1
(6) since it's an inequation of '>=', math.ceil(x) will be the minumum integer answer.

note: do not use python's math.log due to floating point precision issue that
      an exact integer answer will not equal to the floating point which math.log returns.
      ref.: https://stackoverflow.com/a/63974394
'''

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        t = minutesToTest//minutesToDie + 1  # the maximum number of tests can be done
        
        # calculate ceil(log(buckets, base=t)) manually
        quo = buckets
        x = 0  # the minimum number of pigs needed
        while(quo > 1.0):
            quo /= t
            x += 1
        
        return x


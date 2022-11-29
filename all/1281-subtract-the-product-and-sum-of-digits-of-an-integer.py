'''
programming skills lv1 day 2
'''

import math

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        seq = [int(c) for c in str(n)]
        return math.prod(seq) - sum(seq)


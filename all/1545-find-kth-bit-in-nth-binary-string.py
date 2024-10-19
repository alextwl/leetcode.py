'''
2024/10/19 daily challenge

recursion (simulation) approach
'''


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def f_si(i: int) -> list:
            if i == 1:
                return [0]
            si_1 = f_si(i - 1)
            return si_1 + [1] + list(map(lambda x: x ^ 1, reversed(si_1)))
        sn = f_si(n)
        return str(sn[k-1])


'''
recursion with shortcuts ver
'''


class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        if n == 1:
            return "0"
        
        middle = 1 << (n - 1)  # the position of Sn middle
        
        if middle == k:
            # the middle bit is always 1
            return "1"
        elif middle > k:
            # the query bit is in the left part, need to recurse Sn-1
            return self.findKthBit(n - 1, k)
        # middle < k shortcut: the query bit is in the right part,
        # but we can find it in the left part of Sn-1 and invert it.
        target_bit = self.findKthBit(n - 1, (middle << 1) - k)
        return "1" if target_bit == "0" else "0"


'''
2024/03/13 daily challenge

prefix sum approach
'''


class Solution:
    def pivotInteger(self, n: int) -> int:
        suffix = (n * (n + 1)) // 2
        
        prefix = 0
        for x in range(n + 1):
            prefix += x
            if prefix == suffix:
                return x
            suffix -= x

        return -1


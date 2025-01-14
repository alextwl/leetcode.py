'''
2025/01/14 daily challenge

set approach
'''


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        set_a = set()
        set_b = set()
        C = []
        for a, b in zip(A, B):
            set_a.add(a)
            set_b.add(b)
            C.append(len(set_a & set_b))
        return C


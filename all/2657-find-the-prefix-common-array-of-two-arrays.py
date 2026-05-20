'''
2025/01/14 daily challenge
2026/05/20 daily challenge

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


'''
counter (frequency array) approach
'''


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        cnt = [0] * (len(A) + 1)
        common_prefix = 0
        C = []
        for a, b in zip(A, B):
            cnt[a] += 1
            cnt[b] += 1
            if a == b:
                common_prefix += 1
            else:
                common_prefix += (cnt[a] == 2) + (cnt[b] == 2)
            C.append(common_prefix)
        return C


'''
2024/08/05 daily challenge

counter approach
'''


import collections


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ctr = collections.Counter(arr)
        distincts = [k for k, v in ctr.items() if v == 1]
        j = 1
        for sub in arr:
            if sub in distincts:
                if j == k:
                    return sub
                j += 1
        
        return ""

